import random


def checker(x, y, z):
    while x not in ["1", "2", "3"] or int(x) > int(y) or int(x) - int(y) == 0:
        if x not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
        elif int(x) > int(y):
            print("Too many pencils were taken")
        elif int(x) - int(y) == 0:
            print(z, "won!")
            break
        x = input()
    return x


# x should be filled with the current remaining pencils
def next_play(x):
    pencils = int(x) % 4
    if int(x) == 1:
        print(1)
        return 1
    elif pencils == 1:
        random_var = random.randrange(1, 4)
        print(random_var)
        return random_var
    elif pencils in [2, 3]:
        print(pencils - 1)
        return pencils - 1
    elif pencils == 0:
        print(3)
        return 3


# Question 1
print("How many pencils would you like to use:")
pencil_amount_wish = input()
while (pencil_amount_wish == "0") or pencil_amount_wish.isnumeric() is False:
    if pencil_amount_wish.isnumeric() is False:
        print("The number of pencils should be numeric")
    elif pencil_amount_wish == "0":
        print("The number of pencils should be positive")
    pencil_amount_wish = input()

# Question 2
player_1, player_2 = "John", "Jack"
print(f"Who will be the first ({player_1}, {player_2}):")
next_player = input()
while next_player not in [player_1, player_2]:
    print(f"Choose between '{player_1}' and '{player_2}'")
    next_player = input()

# Playing the sticks
remaining_pencils = int(pencil_amount_wish)
while int(remaining_pencils) > 0:
    if next_player == player_1:
        stick_amount = ("|" * remaining_pencils)
        print(stick_amount)
        print(next_player + "'s turn:")
        remaining_pencils -= int(checker(input(), remaining_pencils, player_2))
        next_player = player_2
    elif next_player == player_2:
        stick_amount = ("|" * remaining_pencils)
        print(stick_amount)
        print(next_player + "'s turn:")
        remaining_pencils -= int(checker(str(next_play(remaining_pencils)), remaining_pencils, player_1))
        next_player = player_1
