"""Game 2001 – The PC and the player take turns rolling dice.
Before each throw, the player chooses two dice from the following options: D3, D4, D6, D8, D10, D12, D20, or D100.
The winner is the first to reach 2001 points."""

import random
import re


def user_choose_dice():
    type_dice = {3, 4, 6, 8, 10, 12, 20, 100}
    pattern = r'^D(\d+)$'
    # first die
    while True:
        die1 = input("Choose the first die (D3, D4, D6, D8, D10, D12, D20, D100): ").upper()
        match1 = re.match(pattern, die1)
        if not match1:
            print("Wrong dice code format.")
            continue
        y1 = int(match1.group(1))
        if y1 not in type_dice:
            print(f"Wrong dice type: D{y1}")
            continue
        break # first die OK

    # second die
    while True:
        die2 = input("Choose the second die (D3, D4, D6, D8, D10, D12, D20, D100): ").upper()
        match2 = re.match(pattern, die2)
        if not match2:
            print("Wrong dice code format.")
            continue
        y2 = int(match2.group(1))
        if y2 not in type_dice:
            print(f"Wrong dice type: D{y2}")
            continue
        break # second die OK

    print(f"Your choice: {die1}, {die2}")
    return y1, y2

def pc_choose_dice():
    type_dice = [3, 4, 6, 8, 10, 12, 20, 100]
    x1 = random.choice(type_dice)
    x2 = random.choice(type_dice)
    print(f"PC choice: D{x1}, D{x2}")
    return x1, x2

def roll_dice():
    pc_score = 0
    user_score = 0
    y1, y2 = user_choose_dice()
    x1, x2 = pc_choose_dice()

    while True:
        input("Press enter to roll dice.")
       # Player rolls
        rolls_user1 = random.randint(1,y1)
        rolls_user2 = random.randint(1,y2)
        user_roll_sum = rolls_user1 + rolls_user2
        print(f"Your rolls: {rolls_user1}, {rolls_user2} -> {user_roll_sum}")

        if user_roll_sum == 7:
            user_score = user_score // 7
            print(f"You rolled a 7. Your score is divided by 7.")
        elif user_roll_sum == 11:
            user_score = user_score * 11
            print(f"You rolled an 11. Your score is multiplied by 11.")
        else:
            user_score += user_roll_sum

        # PC rolls
        rolls_pc1 = random.randint(1,x1)
        rolls_pc2 = random.randint(1,x2)
        pc_roll_sum = rolls_pc1 + rolls_pc2
        print(f"PC rolls: {rolls_pc1}, {rolls_pc2} -> {pc_roll_sum}")

        if pc_roll_sum == 7:
            pc_score = pc_score // 7
            print(f"PC rolled a 7. Its score is divided by 7.")
        elif pc_roll_sum == 11:
            pc_score = pc_score * 11
            print(f"PC rolled an 11. Its score is multiplied by 11.")
        else:
            pc_score += pc_roll_sum

        print(f"Current score -> pc: {pc_score} - user: {user_score}\n")

        # Check for victory
        if pc_score >= 2001 and user_score >= 2001:
            print("It's a tie! Both reached 2001 points.")
            break
        elif user_score >= 2001:
            print("You win!")
            break
        elif pc_score >= 2001:
            print("PC wins!")
            break


roll_dice()
