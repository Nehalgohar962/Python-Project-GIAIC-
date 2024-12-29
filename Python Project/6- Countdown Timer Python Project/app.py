# Countdown Timer Python Project -6

import time

# Introduction
print("Welcome to the Countdown Timer!")
print("Enter the time in seconds, and I'll count down for you.\n")

# User se input lena
try:
    total_time = int(input("Enter the countdown time in seconds: "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

# Countdown logic
while total_time > 0:
    minutes, seconds = divmod(total_time, 60)  
    timer = f"{minutes:02d}:{seconds:02d}"  
    print(timer, end="\r") 
    time.sleep(1) 
    total_time -= 1

# Timer Ups!
print("Time's up!")
