import random as r

class die(object):

    n = 6
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
                    dice = r.randint(1, n)
                    print(" ")
                    print(dice)

        elif selection == '2':
                    n = n + 6

        elif selection == '3':
                    break
        
        else:
            print("option does not exist")
        
        

