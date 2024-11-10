# START
# a
def my_avg(x: int, y: int):
    """gets 2 parameters type int and returns the average type float"""
    average: float = (x + y) // 2
    return average


avg1 = my_avg(90, 99)
print(avg1)


# b
def my_headline(line: str):
    """gets a parameter type str and returns it in capital letters and adds exclamation mark """
    capital: str = line.upper() + "!"
    return capital


head1 = my_headline("python has concurred the world")
print(head1)
print(head1)


# c
def contact_list(x: list[int], y: list[int], z: list[int]):
    """gets three list type int and returns one big list that contains all three lists """
    big_list: list[int] = x + y + z
    return big_list


res_con = contact_list([1, 2], [3, 4, 5, 6], [7, 8, 9])
print(res_con)
print(len(res_con))

help(my_headline("x"))

# Stop
