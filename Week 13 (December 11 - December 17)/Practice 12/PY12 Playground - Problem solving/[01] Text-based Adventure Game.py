def intro():
    print('After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.')
    print('A. Grab a nearby rock and throw it at the orc')
    print('B. Lie down and wait to be mauled')
    print('C. Run')
    option = input().upper()
    if option == "A":
        return option_rock()
    elif option == "B":
        return 'Welp, that was quick. You died!'
    elif option == "C":
        return option_run()

def option_rock():
    print('The orc is stunned, but regains control. He begins running towards you again.')
    print('A. Run')
    print('B. Throw another rock')
    print('C. Run towards a nearby cave')
    option = input().upper()
    if option == 'A':
        return option_run()
    elif option == 'B':
        return 'The rock flew well over the orcs head. You missed. You died!'
    elif option == 'C':
        return option_cave()
        
def option_cave():
    print('Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?')
    option_y_n = input().upper()
    print('What do you do next?')
    print('A. Hide in silence')
    print('B. Fight')
    print('C. Run')
    option = input().upper()
    if option == 'A':
        return 'I think orcs can see very well in the dark, right? You died!'
    elif option == 'B':
        if option_y_n == 'Y':
            return 'As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!'
        elif option_y_n == 'N':
            return "You're defenseless. You died!"
    elif option == 'C':
        print('The orc turns around and sees you running.')
        return option_run()

def option_run():
    print('You run as quickly as possible.')
    print('A. Hide behind boulder')
    print('B. Trapped, so you fight')
    print('C. Run towards an abandoned town')
    option = input().upper()
    if option == 'A':
        return "You're easily spotted. You died!"
    elif option == 'B':
        return "You're no match for an orc. You died!"
    elif option == 'C':
        return option_town()

def option_town():
    print('You notice a purple flower near your foot. Do you pick it up? Y/N')
    option_y_n = input().upper()
    if option_y_n == 'Y':
        return 'You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!'
    elif option_y_n == 'N':
        return 'Maybe you should have picked up the flower. You died!'

print(intro())