import json
import tkinter as tk
from tkinter import messagebox

def load_contacts():
    try:
        with open("contact.json", 'r') as file:
            return json.load(file)  
    except FileNotFoundError:
        return {}  

def save_contacts(contacts):
    with open("contact.json", "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    contact_name = name_entry.get()
    contact_number = number_entry.get()

    if contact_name and contact_number: 
        contacts = load_contacts() 
        contacts[contact_name] = contact_number  
        save_contacts(contacts)  
        messagebox.showinfo("Success", f"Contact {contact_name} saved successfully!")
        name_entry.delete(0, tk.END)  
        number_entry.delete(0, tk.END)
        display_contacts()  
    else:
        messagebox.showwarning("Input Error", "Please enter both name and number!")


def display_contacts():
    contacts_list.delete(0, tk.END)  
    contacts = load_contacts() 
    for name, number in contacts.items():
        contacts_list.insert(tk.END, f"{name}: {number}")

def contact_display():
    contact_name = search_entry.get()

    if contact_name:  
        contacts = load_contacts()  
        if contact_name in contacts:
            result_label.config(text=f"{contact_name}: {contacts[contact_name]}")
        else:
            result_label.config(text="Contact not found.")
    else:
        messagebox.showwarning("Input Error", "Please enter a contact name to search.")


def delete_contact():
    contact_name = delete_entry.get()

    if contact_name:  
        contacts = load_contacts()  

        if contact_name in contacts:
            del contacts[contact_name]  
            save_contacts(contacts)  
            messagebox.showinfo("Success", f"Contact {contact_name} deleted successfully!")
            delete_entry.delete(0, tk.END)  
            display_contacts()  
        else:
            messagebox.showwarning("Contact Not Found", "Contact not found.")
    else:
        messagebox.showwarning("Input Error", "Please enter a contact name to delete.")

root = tk.Tk()
root.title("Contact Saver")

tk.Label(root, text="Contact Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Contact Number:").grid(row=1, column=0, padx=10, pady=5)
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1, padx=10, pady=5)

save_button = tk.Button(root, text="Save Contact", command=add_contact)
save_button.grid(row=2, column=0, columnspan=2, pady=10)

contacts_list = tk.Listbox(root, width=40, height=10)
contacts_list.grid(row=3, column=0, columnspan=2, padx=10, pady=5)


tk.Label(root, text="Search Contact:").grid(row=4, column=0, padx=10, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=4, column=1, padx=10, pady=5)

search_button = tk.Button(root, text="Find Contact", command=contact_display)
search_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, pady=5)


tk.Label(root, text="Delete Contact:").grid(row=7, column=0, padx=10, pady=5)
delete_entry = tk.Entry(root)
delete_entry.grid(row=7, column=1, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=8, column=0, columnspan=2, pady=10)

display_contacts()

root.mainloop()
