# Auto-typer

Auto-typer is a Python GUI application that automatically types out text with variable speed, simulating human typing.  
It uses `tkinter` for the interface, `pyautogui` for keyboard automation, and `pyperclip` for clipboard management.

## Features

- Paste any text and have it typed out automatically.
- Adjustable minimum and maximum typing speed (in seconds per character).
- Countdown before typing starts, allowing you to switch to the target window.
- Simple, user-friendly interface.

## Requirements

- Python 3.x
- `pyautogui`
- `pyperclip`
- `tkinter` (usually included with Python)

Install dependencies with:

```sh
pip install pyautogui pyperclip
```