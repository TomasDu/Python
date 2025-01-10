# User Account Manager

## Project Overview
The **User Account Manager** is a Python-based command-line application designed for managing user accounts in a lightweight and secure manner. It provides features such as user registration, authentication, and balance management while ensuring password security. User data is stored in a JSON file, making the system portable and efficient.

### Case Study
This project serves as a prototype for a small-scale account management system, ideal for use in scenarios such as:
- Managing employee accounts in a small business.
- Prototyping an expense tracking or payroll system.
- Teaching basic account management concepts in Python.

By extending the functionality and integrating a front-end interface, the system can scale to real-world applications.

---

## Features
- **User Registration**: Allows the creation of new accounts with secure password validation.
- **Login System**: Enables users to log in securely using their credentials.
- **Balance Management**: Users can view and update their account balance.
- **Cross-Platform Support**: Fully compatible with Linux and Windows environments.
- **Google Colab Adaptation**: A specialized version for running the project in Google Colab.

---

## Technologies Used
- **Python**: Core programming language.
- **JSON**: Used to store user data in a structured format.
- **Regular Expressions**: Validates password strength against predefined security criteria.
- **OS Module**: Ensures seamless operation across different operating systems.

---

## How It Works
### New Users
1. Enter a username and a secure password.
2. Passwords are validated for:
   - Minimum length of 8 characters.
   - At least one uppercase letter, one lowercase letter, one digit, and one special character.
3. Account information is saved in a JSON file.

### Existing Users
1. Log in by entering a valid username and password.
2. Upon successful authentication, view and update the account balance.

### File Management
- **Standard Version**: User data is stored in `users.json` in the current working directory. File paths are automatically adjusted for Linux and Windows.
- **Google Colab Version**: The `users.json` file is stored in Colab's file system (`/content/users.json`).

---

## Folder Structure
```
user-account-manager/
├── standard_version/
│   └── user_account_manager.py
├── colab_version/
│   └── user_account_manager.py
├── README.md
```

- **`standard_version/`**: Contains the script compatible with Linux and Windows.
- **`colab_version/`**: Contains a modified script for use in Google Colab.

---

## Usage Instructions

### Standard Version
1. Navigate to the `standard_version/` folder.
2. Run the script in your terminal:
   ```bash
   python user_account_manager.py
   ```

### Google Colab Version
1. Navigate to the `colab_version/` folder.
2. Upload the script to your Google Colab environment.
3. Ensure the `file_path` is set to:
   ```python
   file_path = '/content/users.json'
   ```
4. Execute the script in a Colab notebook.

---

## Contributing
We welcome contributions! Feel free to:
- Submit pull requests to improve the code or add new features.
- Report issues or suggest enhancements via the Issues tab.


---

## License
This project is open-source and available under the [MIT License](LICENSE).
