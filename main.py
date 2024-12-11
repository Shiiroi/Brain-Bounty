# Magwili, Vince Roi S.
# Section Y-3L
# main file of Brain Bounty

# libraries
from scripts import game
from scripts import highscore as hs

# initialization of dict for hs
highscores = {}

# main menu 
def mainMenu():
    print("\n" + "=" * 30)
    print(" Welcome to Brain Bounty! ")
    print("=" * 30)
    print("[1] Play Game")
    print("[2] View Highscores")
    print("[0] Exit")
    print("=" * 30)
    num = input("\nEnter your choice (0-2): ")
    if num.isdigit():
        return int(num)
    else:
        print("\nPlease enter a valid number!")

def main():
    # initialize variables 
    streak = 0
    currentHP = 50
    currentScore = 0
    easy_left = 5
    medium_left = 5
    hard_left = 5
    enemy_hp = 0
    chosen_question = None
    
    hs.Load(highscores)
    
    # main loop
    while True:
        choice = mainMenu()

        if choice == 1:
            streak = 0
            currentHP = 50
            currentScore = 0
            easy_left = 5
            medium_left = 5
            hard_left = 5
            enemy_hp = 0
            chosen_question = None
            questions = game.LoadQuestions('./questionpool/questionpool.dat')
            while currentHP > 0 and (easy_left > 0 or medium_left > 0  or hard_left > 0):
                randomTask = game.RandomTask(questions)
                chosenMonster = game.ChooseMonster(randomTask)
                enemy_hp = game.SetEnemyHP(chosenMonster)
                
                
                while enemy_hp > 0 and currentHP > 0 and (easy_left > 0 or medium_left > 0  or hard_left >0):
                    chosen_question = game.ChooseQuestion(easy_left, medium_left, hard_left)
                    easy_left, medium_left, hard_left = game.HandleQuestionsLeft(chosen_question, easy_left, medium_left, hard_left)
                    correct = game.HandleQuestion(questions, randomTask, chosen_question)
                    streak,currentScore = game.StreakCounter(streak,correct,currentScore)
                    currentHP = game.HandleHP(correct, currentHP,chosenMonster)
                    currentScore,enemy_hp = game.HandleDamage(correct, currentScore, enemy_hp, chosen_question)
                    game.DisplayRoundResult(currentHP,currentScore,easy_left,medium_left,hard_left,streak)
            
            game.GameOver(currentScore,currentHP)
            name = hs.EnterName()
            hs.Save(name,currentScore)
            
        elif choice == 2:
            hs.Load(highscores)
            hs.DisplayHS(highscores)
            pass
        elif choice == 0:
            break

main()
