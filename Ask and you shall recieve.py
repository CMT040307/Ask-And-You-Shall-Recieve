def master():
    ask = input("Ask and I will do my best to tell! \n")
    if ask.lower() == "wifi password":
        print("Y8GN4PK9")
    elif ask.lower() == "creator":
        print("The creator of this file is CT")
    elif ask.lower() == "favourite website":
        print("reddit.com")
    elif ask.lower() == "favourite drink":
        print("Monster")
    elif ask.lower() == "favourite word":
        print("Blyat")
    elif ask.lower() == "favourite food":
        print("Pizza")
    elif ask.lower() == "monster drink flavours":
        print("https://www.monsterenergy.com/products/monster-energy")
    elif ask.lower() == "favourite thing to do":
        print("Skateboarding and going on the dark web")
    elif ask.lower() == "3rror":
        print("Well done you found the secret command! You have the creators respect! :)")
    elif ask.lower() == "test 001":
        print("test is working!")
    elif ask.lower() == "repeat":
        repeat = input()
        print(repeat)
    elif ask.lower() == "favourite parent":
        print("I love them both equally!")
    elif ask.lower() == "chicken":
        print("Very Nice!")
    elif ask.lower() == "fast food":
        favfastfood = input("What is you favourite fast food place? e.g McDonalds or KFC\n")
        if favfastfood.lower() == "kfc":
            print("Nice, that's my favourite fast food place too!")
        else:
            print("Noice, mine is KFC")
    elif ask.lower() == "favourite genre of music":
        print("Hip Hop and Heavy Metal")
    elif ask.lower() == "calculator":
        def calc():
            first_num = float(input("Enter Your First Number:\n"))
            symbol = input("Add = +, Subtract = -,Times = *, Divide = /")
            second_num = float(input("Enter Your Second Number:\n"))
            if symbol == "+":
                total = first_num + second_num
                print(total)
            elif symbol == "-":
                total = first_num - second_num
                print(total)
            elif symbol == "*":
                total = first_num * second_num
                print(total)
            elif symbol == "/":
                total = first_num / second_num
                print(total)
            else:
                print("Sorry, I don't understand please try again")
                calc()
        calc()
    else:
        print("I don't understand, please read the command list. Thanks")

    restart = input("Do you want to restart? y/n\n")
    if restart.lower() == "n":
        exit()
    else:
        master()

master()