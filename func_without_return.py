# START
# a
import statistics


def my_ascending(x: int, y: int):
    """gets 2 parameters and prints the numbers between them in ascending order"""
    if x > y:
        for i in range(y, x + 1):
            print(i, end=" ")
    else:
        for i in range(x, y + 1):
            print(i, end=" ")


my_ascending(-12, 7)
print()


# b
def my_details(x: str):
    """gets a str parameter and prints the first character, the character in the middle and the last character"""
    print(f"First character: {x[0]}")
    print(f"The character in the middle is: {x[len(x) // 2]}")
    print(f"Last character: {x[-1]}")


my_details("AI is the best")


# c
def say_bool(x: bool):
    """gets a bool, if bool is True prints yes if bool is False prints no"""
    if x is True:
        print("yes")
    else:
        print("no")


say_bool(True)
say_bool(False)


# d
def print_zugi(even_odd: list[int]):
    """gets a list of numbers and prints even for the even numbers and odd for the odd numbers"""
    for i in even_odd:
        if i % 2 == 0:
            print("even", end=" ")
        else:
            print("odd", end=" ")


print_zugi([5, 3, 2, 10, 15, 14, 14])
print()


# e
def my_statistics(grades: list[int]):
    """gets a list of grades, prints the highest grade, the lowest grade, the amount of grades and the grades average"""
    print(f"The lowest grade was: {min(grades)}.")
    print(f"The highest grade was: {max(grades)}.")
    print(f"There are {len(grades)} grades. ")
    print(f"The average grade is {statistics.mean(grades)}.")


my_statistics([50, 23, 98, 76, 32])
grades_list: list[int] = []
while True:
    grade: int = int(input("Enter a grade: "))
    if grade == -99:
        break
    if 0 <= grade <= 100:
        grades_list.append(grade)
    else:
        print("Grade not in range")

my_statistics(grades_list)

# STOP
