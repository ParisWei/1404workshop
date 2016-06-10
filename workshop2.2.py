name = input("please enter your name:")
print ("(H)ello"'\n',
       "(G)oodbye"'\n',
       "(Q)uit")
menu = input("what do you want?")
menu = menu.upper()

while menu != 'Q':
    if menu == 'H':
        print("Hello",name)
    else:
        if menu == 'G':
            print("Goodbye",name)
        else:
            print("Invalid choice")
    menu = input("what do you want?")
    menu = menu.upper()
quit()
