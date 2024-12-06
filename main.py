from scripts import game

# name = input("Enter Player Name: ")

# print(name)

def mainMenu():
    print("\nWelcome to Brain Bounty!")
    print("[1] Play Game")
    print("[2] Highscores")
    print("[0] Exit")
    return int(input("\nEnter a Number: "))

def main():
    while True:
        choice = mainMenu()

        if choice == 1:
            game.play("pokemon")
        elif choice == 2:
            ...
        elif choice == 0:
            ...

main()