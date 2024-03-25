import random as r

def print_dice(die_value):
    dice = [
        "+-------+",
        "|       |",
        "|       |",
        "|       |",
        "+-------+"
    ]

    if die_value == 1:
        dice[2] = "|   •   |"
    elif die_value == 2:
        dice[1] = "|     • |"
        dice[3] = "| •     |"
    elif die_value == 3:
        dice[1] = "|     • |"
        dice[2] = "|   •   |"
        dice[3] = "| •     |"
    elif die_value == 4:
        dice[1] = "| •   • |"
        dice[3] = "| •   • |"
    elif die_value == 5:
        dice[1] = "| •   • |"
        dice[2] = "|   •   |"
        dice[3] = "| •   • |"
    elif die_value == 6:
        dice[1] = "| •   • |"
        dice[2] = "| •   • |"
        dice[3] = "| •   • |"

    for line in dice:
        print(line)
        
def main():

    num_of_die = 1
    dice_menu = None

    dice_menu = {}
    dice_menu['1'] = "Roll Die/Dice"
    dice_menu['2'] = "Add dice"
    dice_menu['3'] = "Exit"

    while True:
        print()
        option = dice_menu.keys()

        for i in option:
            print(i, dice_menu[i])

        selection = input("Select an option by typing a number: ")
        
        if selection == '1':
            print("Rolling...")
            dice_total = 0
            for _ in range(num_of_die):
                dice_rolled = r.randint(1, 6)
                dice_total += dice_rolled
                print_dice(dice_rolled)
            print("Dice roll result:", dice_total)

        elif selection == '2':
            if num_of_die < 5:
                num_of_die += 1
                print("Added a die.")
            else:
                print("Maximum number of dice reached (5)")

        elif selection == '3':
                    break
        
        else:
            print("option does not exist")
        
if __name__ == "__main__":
    main()

