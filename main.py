import random

def roll_die():
    return random.randint(1, 6)

def roll_dice(num_dice):
    rolls = []
    for _ in range(num_dice):
        rolls.append(roll_die())
    return rolls

def dice_simulator():
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll (1 to 10): "))
            if num_dice < 1 or num_dice > 10:
                print("Please enter a number between 1 and 10.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer between 1 and 10.")
            continue
        
        try:
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls < 1:
                print("Please enter a positive number of rolls.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer for the number of rolls.")
            continue
        
        for roll in range(num_rolls):
            print(f"Roll #{roll + 1}: {roll_dice(num_dice)}")
        
        play_again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for using the dice simulator!")
            break

dice_simulator()
