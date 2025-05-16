# Password Manager

A simple and secure password manager built with Python and Tkinter. This app allows you to generate strong passwords, save them along with website and email/username details, and search for saved credentials easily.

## Features

- **Password Generation:** Instantly generate strong, random passwords with a single click.
- **Credential Storage:** Save website, email/username, and password details securely in a local JSON file.
- **Search Functionality:** Quickly search for saved credentials by website name.
- **Clipboard Support:** Generated passwords are automatically copied to your clipboard for convenience.
- **User-Friendly Interface:** Clean and intuitive GUI built with Tkinter.

## How It Works

1. Enter the website and email/username.
2. Click "Generate Password" to create a secure password, which is copied to your clipboard.
3. Click "Add" to save the credentials to a local `data.json` file.
4. Use the "Search" button to retrieve saved credentials for any website.

## Getting Started

### Prerequisites

- Python 3.x
- [pyperclip](https://pypi.org/project/pyperclip/) library  
  Install with:  

  ```bash
  pip install pyperclip
  ```

### Running the App

1. Clone or download this repository.
2. Ensure `logo.png` is in the project directory.
3. Run the script:

   ```bash
   python main.py
   ```

## Example

![Password Manager Screenshot](screenshot.png)

## License

This project is open source and free to use.
