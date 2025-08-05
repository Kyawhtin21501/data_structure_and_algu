import time
import os
import sys

heart = [
    "  **     **  ",
    " ****   **** ",
    "****** ******",
    " *********** ",
    "  *********  ",
    "   *******   ",
    "    *****    ",
    "     ***     ",
    "      *      "
]

letters = {
    'L': ["*    ","*    ","*    ","*    ","*****"],
    'O': [" *** ","*   *","*   *","*   *"," *** "],
    'V': ["*   *","*   *","*   *"," * * ","  *  "],
    'E': ["*****","*    ","**** ","*    ","*****"],
    'Y': ["*   *","*   *"," *** ","  *  ","  *  "],
    'U': ["*   *","*   *","*   *","*   *"," *** "],
    ' ': ["     ","     ","     ","     ","     "]
}

word = "LOVE YOU"

for _ in range(2):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in range(5):
        line = ""
        for char in word:
            line += letters[char][row] + "  "
        print(line)
        time.sleep(0.2)
    time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')
for row in heart:
    print(row)
    time.sleep(0.2)

print()
time.sleep(1)

message = "From the bottom of my heart..."
for char in message:
    print(char, end="", flush=True)
    time.sleep(0.08)

time.sleep(1.5)
print("\n")
confession = "I love you.\nWill you be mine?"
for char in confession:
    print(char, end="", flush=True)
    time.sleep(0.1)

print("\n❤️")
