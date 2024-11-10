# Start
while True:
    try:
        num: int = int(input("Enter a number between 0-9999: "))
        if 0 <= num < 10:
            print("True")
            break
        if 9 < num < 9999:
            digits: str = str(num)
            if all(digit == digits[1] for digit in digits):
                print("True")
                break
            else:
                print("False")
    except ValueError:
        print("invalid input.")
# b
cost: float = float(input("How much did you pay?: "))
price: float = 0
if cost > 800:
    price += (cost - 800) * 0.5
    cost = 800
if cost > 500:
    price += (cost - 500) * 0.6
    cost = 500
if cost > 200:
    price += (cost - 200) * 0.7
    cost = 200
if cost > 100:
    price += (cost - 100) * 0.8
    cost = 100
price += cost * 0.9
print(f"The final price after discount is: {price}.")

# c
float_num1: float = float(input("Enter a decimal number:"))
float_num2:  float = float(input("Enter a decimal number:"))
float_num3:  float = float(input("Enter a decimal number:"))
if float_num1 + float_num2 == float_num3:
    print("True")
elif float_num1 + float_num3 == float_num2:
    print("True")
elif float_num2 + float_num3 == float_num1:
    print("True")
else: print("False")

# d
letter_list: list[str] = []
user_word: str = input("Enter a random word:")
while True:
    letter: str = input("Enter a letter:")
    if letter == "*":
        break
    else:
        letter_list.append(letter)
word_list: list[str] = list(user_word)
for letter in letter_list:
    if letter in word_list:
        print("True")
    else: print("False")

# Stop
