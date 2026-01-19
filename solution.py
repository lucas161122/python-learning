# p1t21
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}")


# greet("Lucas", greeting="Good morning")

# p1t22
# def add_numbers(*args):
#     sum = 0
#     for number in args:
#         sum += number
#     return sum


# print(add_numbers(1, 2, 3))
# print(add_numbers(10, 20, 30, 40)


# p1t25
# def add_numbers(*args):
#     sum = 0
#     for number in args:
#         sum += number
#     return sum


# def main():
#     nums = input()
#     nums = nums.split()
#     nums_int = []
#     for num in nums:
#         nums_int.append(int(num))

#     return add_numbers(*nums_int)


# print(main())


# p1t26

answer1 = "you can go a scary ride!"
answer2 = "maybe try a smaller ride."

user_name = input("What is your name?")
user_age = int(input("How old are you?"))
question = input("are you brave?(yes/no)")
if question == "yes" and user_age >= 10:
    print(f"{user_name},{answer1}")
else:
    print(f"{user_name},{answer2}")
