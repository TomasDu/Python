# User Account Manager

## Project Overview
The **User Account Manager** is a Python-based command-line application that allows users to create accounts, log in, and manage their account balances. It ensures security by validating passwords for strength and stores user data in a JSON file, making it a lightweight and efficient user management system.

### Case Study
Imagine a small business wanting a simple tool for managing employee accounts. This project can serve as a prototype for a lightweight account management system. By enhancing the interface and integrating it with a web or mobile front end, the system could scale to support real-world use cases, such as expense tracking or payroll systems.

### Contributing
Feel free to contribute to the project by submitting pull requests or suggesting enhancements.

---

### Features
- **User Registration**: Create new accounts with secure password validation.
- **Login System**: Authenticate existing users with their username and password.
- **Balance Management**: Users can view and add to their account balance.
- **Cross-Platform Compatibility**: Works seamlessly on both Linux and Windows.

### Technologies Used
- **Python**: Core programming language.
- **JSON**: Storage for user data.
- **Regular Expressions (re)**: Used for password validation.
- **OS Module**: Ensures compatibility across operating systems.

---

## How It Works
1. **New Users**: 
   - Prompted to provide a username and a secure password.
   - Passwords are validated against criteria (e.g., minimum length, special characters, digits, uppercase/lowercase letters).
   - User data is stored in a JSON file.

2. **Existing Users**:
   - Log in by entering their username and password.
   - After authentication, users can view their balance and add funds.

3. **File Management**:
   - User data is saved in `users.json`, located in the current working directory.
   - Compatible with both Linux (`./users.json`) and Windows (`users.json`).

---

## Usage on Google Colab
If you wish to use this project in **Google Colab**, note the following:
- Google Colab does not use a local file system like a regular desktop environment.
- Update the `file_path` variable to point to a location in Colab's file system, such as:
  ```python
  file_path = '/content/users.json'
