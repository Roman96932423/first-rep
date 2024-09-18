# Calculator

user_first_num = int(input("Enter first number: "))
user_second_num = int(input("Enter second number: "))
user_action = input("Enter action (+, -, *, /): ")

if user_action == '+':
    result = user_first_num + user_second_num

if user_action == '-':
    result = user_first_num - user_second_num

if user_action == '*':
    result = user_first_num * user_second_num

if user_action == '/':
    result = user_first_num / user_second_num

print(f'Result {user_first_num} {user_action} {user_second_num}: {result}')
