# 📞 Simple Contact Management System

This is a command-line application built in Python for basic contact management. It allows users to add, search, update, and display contacts, with data persisted using a JSON file.

## ✨ Features

* **Add Contact:** Store a new contact with a name, phone number, and email. Includes validation to ensure the name is unique and the phone number is digits-only.
* **Search Contact:** Quickly find a contact by name and display their details.
* **Update Contact:** Modify an existing contact's phone number or email.
* **Display All:** View a list of all saved contacts.
* **Data Persistence:** Contacts are automatically saved to a file named `contacts.json` upon exit and loaded when the program starts.

### Installation1.  **Clone the repository** to your local machine:    
     1.```bash
     git clone (https://github.com/Shreya-Pandey90/Techplement/tree/my-new-branch)
     cd ContactManager
     ```
     2.  **Run the application** from your terminal:
     ```bash
     python contactmanagement.py
     ``` 

## 🛠️ Usage

When you run the script, a main menu will appear, prompting you for a choice:

Follow the on-screen prompts for each option:

| Option | Command | Description |
| :---: | :---: | :--- |
| **1** | `Add Contact` | Prompts for Name, Phone Number, and Email. |
| **2** | `Search Contact` | Prompts for the Name of the contact to find. |
| **3** | `Update Contact` | Allows modification of Phone or Email for an existing contact. |
| **4** | `Display All Contacts` | Prints all stored contacts to the console. |
| **5** | `Exit` | Saves all current contacts to `contacts.json` and closes the program. |

## 📁 Project Structure

| File | Description |
| :--- | :--- |
| `contactmanagement.py` | The main Python script containing all contact management functions and the main loop. |
| `contacts.json` | (Generated file) Stores the contact data in JSON format for persistence. **This file is ignored by Git.** |
| `.gitignore` | Ensures the generated `contacts.json` file is not tracked by the repository. |
| `README.md` | This project documentation file. |

---

## 🤝 Contributing

Feel free to fork the repository, make improvements, and open a Pull Request. Any suggestions for new features or bug fixes are welcome!
