import pyautogui, time

time.sleep(5) # Hold on a few seconds to execute the program 

f = open("backstreetboys", "r") # Open the file and read

# Create a loop for any word in the file on f 
for word in f:
  pyautogui.typewrite(word) # Print the word 
  pyautogui.press("enter") # Send the word
