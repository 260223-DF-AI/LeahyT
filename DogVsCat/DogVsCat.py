import torch
import torch.nn as nn

class PetClassifierCNN(nn.Module):
    """
    Task 1: Build the CNN Architecture
    """
    def __init__(self):
        super(PetClassifierCNN, self).__init__()
        
        # 1. First Convolutional Block
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1) 
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # 2. Second Convolutional Block
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.relu2 = nn.ReLU()
        # You can reuse the pool layer or define a new one
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # 3. Fully Connected (Linear) Output Layer
        # Input image is 64x64. 
        # After Pool 1 -> 32x32
        # After Pool 2 -> 16x16
        # Flattened size = 32 channels * 16 * 16 spatial area
        flattened_size = 32 * 16 * 16
        
        self.fc = nn.Linear(flattened_size, 2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.relu2(x)   
        x = self.pool2(x)
        # Flatten the spatial dimensions into a 1D vector for the Linear layer
        nn.Flatten(x)
        # Output of pool2 is [Batch, 32, 16, 16]. We want [Batch, 32*16*16]
        x = x.view(x.size(0), -1) 
        
        x = self.fc(x)
        return x

def test_forward_pass():
    """
    Task 2: Test the Network Dimensionality
    """
    print("--- Testing CNN Forward Pass ---")
    
    # 1. Instantiate the model
    model = PetClassifierCNN()
    
    # 2. Create a dummy image batch (4 images, 3 channels, 64x64 size)
    dummy_input = torch.randn(4, 3, 64, 64)
    print(f"Input Shape: {dummy_input.shape}")
    
    # 3. Pass through the model
    output = model(dummy_input)
    
    # 4. Print the final shape
    if output is not None:
        print(f"Output Shape: {output.shape} (Expected: torch.Size([4, 2]))")
    else:
        print("Output is None — did you complete all the TODOs in the forward pass?")

if __name__ == "__main__":
    test_forward_pass()