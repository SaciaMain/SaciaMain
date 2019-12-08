import random
import string
import time
import os
import sys

def randomStringDigits(stringLength=30):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
kak =input('generate key?:  ')
text = randomStringDigits()
if kak == "yes":
    print("")
    print("")
    print("")
    print(text)
    print("")
    print("")
    f = open('Keys.txt', 'a')
    f.write(text+ '\n')

os.system('git add Keys.txt')
os.system("git commit -m 'Update'")
os.system("git push origin master")
time.sleep(5)

