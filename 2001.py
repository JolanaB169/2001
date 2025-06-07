"""Game 2001 – The PC and the player take turns rolling dice. The winner is the one who reaches 2001 points first."""

import random


def roll_dice():
    pc_score = 0
    user_score = 0

    while True:
        input("Press Enter to roll the dice")

        # Player rolls
        rolls_user = [random.randint(1,6) for i in range(2)]
        user_roll_sum = sum(rolls_user)
        print(f"Your rolls: {rolls_user} -> {user_roll_sum}")

        if user_roll_sum == 7:
            user_score = user_score // 7
            print(f"You rolled a 7. Your score is divided by 7.")
        elif user_roll_sum == 11:
            user_score = user_score * 11
            print(f"You rolled an 11. Your score is multiplied by 11.")
        else:
            user_score += user_roll_sum

        # PC rolls
        rolls_pc = [random.randint(1,6) for i in range(2)]
        pc_roll_sum = sum(rolls_pc)
        print(f"PC rolls: {rolls_pc} -> {pc_roll_sum}")

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
        if pc_score >= 2001:
            print("PC wins!")
            break
        elif user_score >= 2001:
            print("You wins!")
            break
        elif pc_score >= 2001 and user_score >= 2001:
            print("It's a tie! Both reached 2001 points.")
            break


roll_dice()
