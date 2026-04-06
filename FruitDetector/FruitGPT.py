import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from PIL import Image
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.Resize(tuple((64,64))),   # resize images to 64x64
    transforms.RandomRotation(30),
    transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(), # convert images to PyTorch tensors
    transforms.Normalize((0.5,), (0.5,)) 
])


full_dataset = datasets.ImageFolder(root="data/fruits-360_original-size/fruits-360-original-size/Training", transform=transform)
test_dataset = datasets.ImageFolder(root="data/fruits-360_original-size/fruits-360-original-size/Test", transform=transform)

selected_classes = ["apple_red_1", "Banana 3", "Blackberry 1", "Carrot 1", "Cucumber 1", "Pepper Red 3", "Plum 4", "Strawberry 2"]  # only these classes

#selected_classes = ["Banana 3", "Blackberry 1", "Cucumber 1", "Plum 4"]  # only these classes
class_to_idx = full_dataset.class_to_idx
selected_indices = [class_to_idx[c] for c in selected_classes]

# Create remap dictionary
label_map = {old: new for new, old in enumerate(selected_indices)}

# Filter + remap
filtered_samples = [
    (path, label_map[label])
    for path, label in full_dataset.samples
    if label in selected_indices
]

# Replace dataset
full_dataset.samples = filtered_samples
full_dataset.targets = [s[1] for s in filtered_samples]
full_dataset.classes = selected_classes
full_dataset.class_to_idx = {c: i for i, c in enumerate(selected_classes)}

class_to_idx = test_dataset.class_to_idx
selected_indices = [class_to_idx[c] for c in selected_classes]

label_map = {old: new for new, old in enumerate(selected_indices)}

filtered_samples = [
    (path, label_map[label])
    for path, label in test_dataset.samples
    if label in selected_indices
]

test_dataset.samples = filtered_samples
test_dataset.targets = [s[1] for s in filtered_samples]
test_dataset.classes = selected_classes
test_dataset.class_to_idx = {c: i for i, c in enumerate(selected_classes)}

train_loader = DataLoader(full_dataset, batch_size=8,shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=8, shuffle=False)


class FruitGPT(nn.Module):
    def __init__(self):
        super(FruitGPT, self).__init__()
        self.flatten = nn.Flatten()
        # self.layers = nn.Sequential(
        #     nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1),
        #     nn.ReLU(),
        #     nn.MaxPool2d(2), 

        #     nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
        #     nn.ReLU(),
        #     nn.MaxPool2d(2), 

        #     nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
        #     nn.ReLU(),
        #     nn.MaxPool2d(2), 
        # )
        self.layers = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2), 

            # nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            # nn.BatchNorm2d(64),
            # nn.ReLU(),
            
            # nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            # nn.BatchNorm2d(128),
            # nn.ReLU(),
            # nn.MaxPool2d(2),

            # nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            # nn.BatchNorm2d(256),
            # nn.ReLU(),  
            # nn.MaxPool2d(2),
        )
        self.classify = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32768, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 8)
        )

    def forward(self, x):
        x = self.flatten(x)
        x = x.view(-1, 3, 64, 64)
        x = self.layers(x)
        return self.classify(x)


def train_one_epoch(model, dataloader, optimzer, criterion):
    # print()
    # print("--- Training One Epoch ---")
    
    model.train() # The model is ready to learn (and dropout is active)
    for batch, (x,y) in enumerate(dataloader):
        
        x, y = x.to(device), y.to(device)

        pred = model(x)
        loss = criterion(pred, y)
        optimzer.zero_grad()
        loss.backward()
        optimzer.step()

        if batch % 50 == 0:
            print(f"Batch {batch} - Loss: {loss}")

    #print(batch)

def evaluate(model, dataloader, criterion):
    print()
    print("--- Evaluating Model ---")
    
    model.eval() # The model is not learning, and dropout is inactive

    test_loss, correct = 0, 0
    with torch.no_grad():
        for x, y in dataloader:
            x, y = x.to(device), y.to(device)

            pred = model(x)
            test_loss += criterion(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    print(f"Test Loss: {test_loss:.4f}, Test Accuracy: {correct / len(dataloader.dataset):.4f}")
    
# check what the output of a picture is
def predict_folder(model, folder, transform, class_names, device):
    model.eval()

    with torch.no_grad():
        for file in os.listdir(folder):
            if not file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
                continue

            path = os.path.join(folder, file)

            # Load image
            img = Image.open(path).convert("RGB")

            # Apply transforms
            img = transform(img)

            # Add batch dimension
            img = img.unsqueeze(0).to(device)

            # Predict
            output = model(img)
            probs = torch.softmax(output, dim=1)

            pred = probs.argmax(1).item()
            confidence = probs.max().item()
            #top3String = "// "
            
            # for name, p in zip(class_names,probs):
            #     top3String += f"{name}: {p.item():.1%} / "
           
            class_name = class_names[pred]

            print(f"{file} -> {class_name} ({confidence:.2%})")
            #print(f"{file} -> {top3String}")
            

if __name__ == "__main__":
    modelCount = 3
    epochCount = 2
    for i in range(modelCount):
        model = FruitGPT().to(device)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.0005)
        print(f"Model #{i+1}:")
        for x in range(epochCount):
            print(f"Epoch #{x+1}")
            train_one_epoch(model, train_loader, optimizer, criterion)
        evaluate(model, test_loader, criterion)
        
        print(f"Model #{i+1}:")
        predict_folder(model, "my_data", transform, test_dataset.classes, device)
        print()
        print()