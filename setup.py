import pyautogui as pag
import time

# Define the coordinates and use the `actions` list
actions = [
    (456, 172, 4),  # change tab
    (362, 406, 4),  # type email
    (640, 408, 4),  # give access
    (658, 508, 4),  # install
]

# open secrets.txt 
secrets = {}
with open("secrets.txt") as file:
    for line in file:
        key, value = line.strip().split("=")
        secrets[key] = value


# Wait for a few seconds to give time to focus on the target application
time.sleep(10)
email = secrets["EMAIL_SECRET"]
    
for x, y, duration in actions:
    if (x, y, duration) == (362, 406, 4):
        pag.click(x, y, duration=duration)
        pag.typewrite(email)
    else:
        pag.click(x, y, duration=duration)

print("..........................................................")
print(".....Brought By The kifayatqadeer................................")
print("..........................................................")
print("Done !")

 
