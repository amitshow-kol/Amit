import time

timestamp = input("Enter the current time in HH:MM:SS format: ")

if timestamp < "12:00:00":
    print("Good morning!")

elif timestamp < "18:00:00":   
    print("Good afternoon!")

elif timestamp < "21:00:00":
    print("Good evening!")

else:
    print("Good night!")