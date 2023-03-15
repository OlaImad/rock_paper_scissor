import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.pi)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f'your love score is {love_score}')

###########################################################

result = random.randint(0, 1)
if result == 1:
    print('Heads')
else:
    print('tail')

###########################################################

names = input("Give me every body's name separated by comma:\n")
names_list = names.split(',')

len_names_list = len(names_list) -1

index = random.randint(0, len_names_list )
result = names_list[index]

print(f'{result} is going to pay the bill.')

############################################################

row1 = ['✉️', '✉️', '✉️']
row2 = ['✉️', '✉️', '✉️']
row3 = ['✉️', '✉️', '✉️']
map = [row1, row2, row3]
place = input('where do you want to put the treasure ' )
first_index = int(place[0]) - 1
second_index = int(place[1]) - 1
map[first_index][second_index] = 'X'
print(f'{row1}\n{row2}\n{row3}')

############################################################
user_answer = int(input('What do you choose? type 0 for rock, 1 for paper or 2 for scissors.\n'))

choices = ['rock', 'paper', 'scissors']
user_choice = choices[user_answer]
# computer_choice = random.choices(choices)
computer_index = random.randint(0, 2)
computer_choice = choices[computer_index]

if user_answer > 2 or user_answer < 0:
    print('you have entered an invalid number')

else:
    print(f"computer's choice: {computer_choice}")
    print(f"user's choice: {user_choice}")
    if user_answer == 0 and computer_index == 2:
        print('you win')
    elif computer_index == 0 and user_answer == 2:
        print('you lose')
    elif computer_index > user_answer:
        print('you lose')
    elif user_answer > computer_index:
        print('you win')
    elif computer_index == user_answer:
        print('it is a draw')
