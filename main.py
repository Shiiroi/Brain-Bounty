from scripts import game

# name = input("Enter Player Name: ")

# print(name)
questions = None

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
            questions = game.LoadQuestions('/workspaces/Brain-Bounty/questionpool/questionpool.dat')
            randomTask = game.RandomTask(questions)
            print(randomTask)
            game.Play(randomTask)
        elif choice == 2:
            ...
        elif choice == 0:
            break

main()