print("Welcome to the Launch Console")
name = input("What is your name?\nEnter Here: ")
print(f"Hi, {name}!")
running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Fun fact")
    print("4) Exit")
    choice = int(input("Pick 1-4: "))
    if choice == 1:
        print(f"I'm {name}, a senior in high school.")
        print("I'm passionate about using coding and programming to help my community.")
        print("I previously worked on a project that was adopted by the nonprofit I was working with.")
    elif choice == 2:
        print("I want to learn Python more in-depth and it's professional use. I want to use what I learn to hopefully land and internship.")
    elif choice == 3:
        print("A fun fact about me is that I play the violin.")
    elif choice == 4:
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, 3, or 4")