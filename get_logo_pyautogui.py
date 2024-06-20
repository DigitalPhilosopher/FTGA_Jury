import pandas as pd
import pyperclip
import pyautogui
import time
import keyboard
# Read the Excel file
file_path = './FTGA/data/Fintech Germany Award 2024/questions.xlsx'
df = pd.read_excel(file_path)

# Extract all entries from the column "Please upload your startup logo"
logo_urls = df["Please upload your startup logo."].dropna().tolist()

def automate():
    time.sleep(0.5)  # Wait for the new tab to open
    # Switch to the browser window
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)

    for link in logo_urls:
        pyautogui.hotkey('ctrl', 't')
        time.sleep(0.5)  # Wait for the new tab to open
        pyperclip.copy(link)
        time.sleep(0.5)  # Wait for the new tab to open
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)  # Wait for the paste action to complete
        pyautogui.press('enter')  # Press Enter to navigate to the URL
        time.sleep(0.5)  # Wait for the paste action to complete
        # Move to the position to click
        pyautogui.moveTo(1835, 91, duration=0.2)
        pyautogui.click()
        time.sleep(1)  # Wait for the action to complete
        # Close the tab
        pyautogui.hotkey('ctrl', 'w')

# Run the automation
print("Press 's' to stop the script.")
automate()