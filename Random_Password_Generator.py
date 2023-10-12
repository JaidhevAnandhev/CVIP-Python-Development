import random
from string import punctuation

password = " "

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

print("~~~RANDOM PASSWORD GENERATOR~~~")
print("1.Password without Special Characters.")
print("2.Password with Special Characters.")

choice = int(input("Enter you Choice = "))
length = int(input("Enter the length of the string = "))

if choice == 1:
    char_choice = input("Do you wish to add the lowercase characters in your password (yes/no/both) = ")
    for i in range(length):
        if char_choice == 'yes':
            pwd1 = lower + numbers
            password = "".join(random.sample(pwd1, length))
        elif char_choice == 'no':
            pwd2 = upper + numbers
            password = "".join(random.sample(pwd2, length))
        elif char_choice == 'both':
            pwd3 = upper + lower + numbers
            password = "".join(random.sample(pwd3, length))
        else:
            print("Type correct option")
    print(f"Random Generated password = {password}")

elif choice == 2:
    char_choice = input("Do you wish to add the lowercase characters in your password (yes/no/both) = ")
    for i in range(length):
        if char_choice == 'yes':
            pwd1 = lower + numbers + punctuation
            password = "".join(random.sample(pwd1, length))
        elif char_choice == 'no':
            pwd2 = upper + numbers + punctuation
            password = "".join(random.sample(pwd2, length))
        elif char_choice == 'both':
            pwd3 = upper + lower + numbers + punctuation
            password = "".join(random.sample(pwd3, length))
        else:
            print("Type correct option")
    print(f"Random Generated password = {password}")

else:
    print("Please provide the correct option (1 / 2)!")