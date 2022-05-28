"""
1 - Write a program that counts up the number of vowels [a, e, i, o, u]
contained in the string
"""
v_count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
vowels = ''.join(vowels)
my_str = "ahmed galal is good"
for el in my_str:
    if el.lower() in vowels:
        v_count += 1
print(v_count)
"""
2 - Write a function that accepts two arguments (length, start) to generate
an array of a specific length filled with integer numbers increased by one
from start.
"""
def gen_len(length, start):
    return [x for x in range(start, start + length)]
print(gen_len(10, 5))
"""
3 - Fill an array of 5 elements from the user, Sort it in descending and
ascending orders then display the output
"""
x = ['b', 'c', 'm', 'l']
print(sorted(x, reverse=False))  # ascending
print(sorted(x, reverse=True))  # descending
"""
4 - write a function that takes a number as an argument and if the number
divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
divisible by both return "FizzBuzz"
"""

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "buzz"
fizz_buzz(30)
"""
5 - Write a function which has an input of a string from user then it will
return the same string reversed
"""


def reverse_string(name):
    #name = name[::-1]
    # return name.reverse()
    new_name = ''
    for i in range(0, len(name)):
        new_name += name[-(i + 1)]
    return new_name

reverse_string("ahmed")

"""
6 - Ask the user to enter the radius of a circle in order to alert its calculated
area and circumference
"""


def circle_area_circumference(radius):
    import math
    circle_area = math.pi * (radius ** 2)
    circle_circumference = 2 * radius * math.pi
    return f"area = {circle_area} " \
           f"and circumference = {circle_circumference} " \
           f"" % dict(circle_area=circle_area,
                      circle_circumference=circle_circumference)
circle_area_circumference(25)

"""
7 - Ask the user for his name then confirm that he has entered his name
(not an empty string/integers). then proceed to ask him for his email and
print all this data
- (Bonus) check if it is a valid email or not
"""

"""
8 - Write a program that prints the number of times the string 'iti' occurs in
"""
st = "itiian's are in love on iti"
count_iti = 0
for i in str.split(''):
    if 'iti' in i:
        count_iti +=1
print(count_iti)
# st.count('iti')

"""
(Bonus) 
9 - Write a function that takes a string and prints the longest
alphabetical ordered substring occured.
For example, if the string is 'abdulrahman' then the output is:
Longest substring in alphabetical order is: abdu
"""


def get_apha_order(name):
    new_apha = []
    alpha = ''
    for i in range(0, len(name)):
        if i < len(name)-1 and name[i] <= name[i + 1]:
            alpha += name[i]
        else:
            alpha += name[i]
            new_apha.append(alpha)
            alpha = ''
    return max(new_apha, key=len)
get_apha_order("abdulrahman")
