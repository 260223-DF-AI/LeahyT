# contact_book.py - Contact Book Application
# Starter code for e003-exercise-data-structures

"""
Contact Book Application
------------------------
A simple contact management system using Python data structures.

Data Structure:
- Each contact is a dictionary with: name, phone, email, category, created_at
- All contacts are stored in a list

Complete the TODO sections below to finish the application.
"""

from datetime import datetime

# =============================================================================
# Initialize Contact Book
# =============================================================================
contacts = []


# =============================================================================
# TODO: Task 1 - Create the Contact Book
# =============================================================================
#contacts is the list of dictionaries, all other parameters are strings
def add_contact(contacts, name, phone, email, category):
    """
    Add a new contact to the contact book.
    
    Args:
        contacts: The list of all contacts
        name: Contact's full name
        phone: Contact's phone number
        email: Contact's email address
        category: One of: friend, family, work, other
    
    Returns:
        The created contact dictionary
    """
    newContact = {
        "name": name,
        "phone": phone,
        "email": email,
        "category": category,
        "created_at": datetime.now()
    }
    contacts.append(newContact)
    return newContact
    # TODO: Create a contact dictionary with all fields
    # TODO: Add created_at timestamp using datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # TODO: Append to contacts list
    # TODO: Return the new contact
    

# =============================================================================
# TODO: Task 2 - Display Contacts
# =============================================================================
#contacts is a list of dictionaries
def display_all_contacts(contacts):
    """
    Display all contacts in a formatted table.
    
    Output format:
    =============================================
                CONTACT BOOK (X contacts)        
    =============================================
    #  | Name            | Phone         | Category
    ---|-----------------|---------------|----------
    1  | Alice Johnson   | 555-123-4567  | friend
    ...
    """
    # TODO: Print header with contact count
    # TODO: Print table headers
    # TODO: Loop through contacts and print each row
    # TODO: Print footer
    print("=============================================")
    print(f"            CONTACT BOOK ({len(contacts)} contacts)")
    print("=============================================")
    print("#  | Name            | Phone         | Category")
    print("---|-----------------|---------------|----------")
    for i, contact in enumerate(contacts):
        print(f"{i}  | {contact["name"]} | {contact["phone"]} | {contact["category"]}")

def display_contact_details(contact):
    """
    Display detailed information for a single contact.
    
    Output format:
    --- Contact Details ---
    Name:     [name]
    Phone:    [phone]
    Email:    [email]
    Category: [category]
    Added:    [created_at]
    ------------------------
    """
    # TODO: Print formatted contact details
    print("--- Contact Details ---")
    print(f"Name:     [{contact["name"]}]")
    print(f"Phone:    [{contact["phone"]}]")
    print(f"Email:    [{contact["email"]}]")
    print(f"Category: [{contact["category"]}]")
    print(f"Added:    [{contact["created_at"].strftime("%Y-%m-%d %H:%M:%S")}]")
    print("-----------------------")

# =============================================================================
# TODO: Task 3 - Search Functionality
# =============================================================================

def search_by_name(contacts, query):
    """
    Find contacts whose name contains the query string.
    Case-insensitive search.
    
    Returns:
        List of matching contacts
    """
    foundNameList = []
    for i in range(len(contacts)):
        if contacts[i]["name"].lower() == query.lower():
            foundNameList.append(contacts[i])

    # TODO: Filter contacts where query is in name (case-insensitive)
    # Hint: Use list comprehension and .lower()
    return foundNameList


def filter_by_category(contacts, category):
    """
    Return all contacts in a specific category.
    
    Returns:
        List of contacts matching the category
    """
    sameCategoryList = []
    for i in range(len(contacts)):
        if contacts[i]["category"] == category:
            sameCategoryList.append(contacts[i])
    # TODO: Filter contacts by category
    return sameCategoryList


def find_by_phone(contacts, phone):
    """
    Find a contact by exact phone number.
    
    Returns:
        The contact dictionary if found, None otherwise
    """
    # TODO: Search for contact with matching phone
    samePhoneList = None
    for i in range(len(contacts)):
        if contacts[i]["phone"] == phone:
            samePhoneList = contacts[i]
    return samePhoneList


# =============================================================================
# TODO: Task 4 - Update and Delete
# =============================================================================

def update_contact(contacts, phone, field, new_value):
    """
    Update a specific field of a contact.
    
    Args:
        contacts: The list of all contacts
        phone: Phone number to identify the contact
        field: The field to update (name, phone, email, or category)
        new_value: The new value for the field
    
    Returns:
        True if updated, False if contact not found
    """
    updatedContact = find_by_phone(contacts, phone)
    if updatedContact != []:
        updatedContact[0][field] = new_value
    else:
        return False    
    # TODO: Find contact by phone
    # TODO: Update the specified field
    # TODO: Return success/failure
    return True


def delete_contact(contacts, phone):
    """
    Delete a contact by phone number.
    
    Returns:
        True if deleted, False if not found
    """
    
    deletedContact = find_by_phone(contacts, phone)
    if deletedContact != []:
        contacts.remove(deletedContact)
    else:
        return False    
    return True


# =============================================================================
# TODO: Task 5 - Statistics
# =============================================================================

def display_statistics(contacts):
    """
    Display statistics about the contact book.
    
    Output:
    --- Contact Book Statistics ---
    Total Contacts: X
    By Category:
      - Friends: X
      - Family: X
      - Work: X
      - Other: X
    Most Recent: [name] (added [date])
    -------------------------------
    """
    categoryCounts = {
        "friend": 0,
        "family": 0,
        "work": 0,
        "other": 0
    }
    for i in range(len(contacts)):
        categoryCounts[contacts[i]["category"]] += 1
    mostRecentContact = contacts[1]
    for i in range(len(contacts)):
        if contacts[i]["created_at"] > mostRecentContact["created_at"]:
            mostRecentContact = contacts[i]
    print("Total Contacts: " + str(len(contacts)))
    print("By Category:")
    print(f"  - Friends: {categoryCounts["friend"]}")
    print(f"  - Family: {categoryCounts["family"]}")
    print(f"  - Work: {categoryCounts["work"]}")
    print(f"  - Other: {categoryCounts["other"]}")
    print(f"Most Recent: [{mostRecentContact["name"]}] (added [{mostRecentContact["created_at"].strftime("%Y-%m-%d %H:%M:%S")}])")
    print("-------------------------------")
    
    pass


# =============================================================================
# STRETCH GOAL: Interactive Menu
# =============================================================================

def display_menu():
    """Display the main menu."""
    print("\n========== CONTACT BOOK ==========")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. View statistics")
    print("0. Exit")
    print("==================================")


def main():
    """Main function with interactive menu."""
    # TODO: Implement menu loop
    # Use while True and break on exit choice
    pass


# =============================================================================
# Test Code - Add sample data and test functions
# =============================================================================

if __name__ == "__main__":
    print("Contact Book Application")
    print("=" * 40)
    
    contacts = []
    add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    add_contact(contacts, "Mike Smith", "717-571-1752", "mike@example.com", "family")
    add_contact(contacts, "Aloacious OHare", "185-816-3782", "aloacious@example.com", "work")
    add_contact(contacts, "Squidward Tentacles", "246-125-1256", "squiddy@example.com", "friend")
    add_contact(contacts, "Harry Potter", "222-926-9817", "harry@example.com", "other")
    #display_all_contacts(contacts)
    #display_contact_details

    #results = find_by_phone(contacts, "222-926-9817")
    #print(results)
    
    #result = delete_contact(contacts, "222-926-9817")
    #print(contacts)
    #print(result)

    #display_statistics(contacts)
    
    #display_contact_details(contacts[4])
    
    display_all_contacts(contacts)

    # STRETCH: Uncomment to run interactive menu
    # main()
