import random

# Finding out the Highest Score.
print("Enter scores of all Subjects:")
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(f"List of student scores: {student_scores}")

highest_score = 0
for score in student_scores:
    if highest_score < score:
        highest_score = score

print(f"The highest score in the class: {highest_score}")

# Adding even numbers.
print("Enter a number between 0 and 1000.")
target = int(input()) + 1  # Increment for last digit in range.
sum = 0

if target >= 1002:
    print("Enter a number which is <= 1000.")
else:
    for even in range(0, target, 2):
        sum += even

print(f"The sum of even numbers: {sum}")

# Password Generator.
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "?"]

print("Customize your own Password with PyPass!")
pass_letters = int(input("How many letters would you like in your Password?\n"))
pass_numbers = int(input("How many numbers would you like in your Password?\n"))
pass_symbols = int(input("How many symbols would you like in your Password?\n"))

password_list = []
for char in range(0, pass_letters):
    password_list += random.choice(letters)

for num in range(0, pass_numbers):
    password_list += random.choice(numbers)

for sym in range(0, pass_symbols):
    password_list += random.choice(symbols)


password = ""
random.shuffle(password_list)
for chars in password_list:
    password += chars


print(f"Random Password: {password}")
