# Magwili, Vince Roi S.
# Section Y-3L
# game lib that handles most of the game logic

import random

# initialization of variables

# names of enemies
easy_enemies = ["Blossom", "Twiglet", "Breeze", "Puff", "Skitter", "Snail", "Grumble", "Flit", "Pip", "Whisker"]

medium_enemies = ["Grim", "Wisp", "Razor", "Viper", "Brute", "Shade", "Talon", "Glare", "Scourge", "Claw"]

hard_enemies = ["Maul", "Dread", "Ravage", "Venge", "Storm", "Fang", "Venom", "Ghoul", "Wretch", "Blight"]

# name of attacks
easy_name = "Quick Draw"
medium_name = "Ambush"
hard_name = "Dead Eyer"

# attack dmg controller
easy_dmg = 10
medium_dmg = 20
hard_dmg = 30

# points gain controller
easy_enemy_bounty = 100
medium_enemy_bounty = 250
hard_enemy_bounty = 500

# enemy dmg controller
easy_enemy_dmg = 10
medium_enemy_dmg = 15
hard_enemy_dmg = 20

# enemy hp controller
easy_enemy_hp = 10
medium_enemy_hp = 30
hard_enemy_hp = 50

# streak bonus points
streakBonus = 20

# CHOOSES ATTACK
def ChooseQuestion(easy,medium,hard):
    print("\nChoose Your Attack:")
    print("=" * 30)
    print(f"[1] Quickdraw [{easy_name}] ({easy_dmg} DMG)")
    print(f"[2] Ambush     [{medium_name}] ({medium_dmg} DMG)")
    print(f"[3] Dead Eye   [{hard_name}] ({hard_dmg} DMG)")
    print("=" * 30) 
    
    question = input("\nSelect your attack (1-3): ")
    if question.isdigit():
        question = int(question)
        if question == 1:
            if easy == 0:
                print("No more quickdraw left!")
                return ChooseQuestion(easy,medium,hard)
            return "easy"
        elif question == 2:
            if medium == 0:
                print("No more Ambush left!")
                return ChooseQuestion(easy,medium,hard)
            return "medium"
        elif question == 3:
            if hard == 0:
                print("No more Dead Eye left!")
                return ChooseQuestion(easy,medium,hard)
            return "hard" 
        else: 
            print("Please input a valid number!")
            return ChooseQuestion(easy,medium,hard)
    else:
        print("Please input a valid number!")
        return ChooseQuestion(easy,medium,hard)

# chooses enemy
def ChooseMonster(category):
    print("\n Monster Hunt!")
    print("=" * 30)
    print(f" Category: {category}")
    print("-" * 30)

    random_easy_name, random_medium_name, random_hard_name = RandomName()
    print(f"[1] {random_easy_name} (Common)")
    print(f"[2] {random_medium_name} (Elite)")
    print(f"[3] {random_hard_name} (Mythical)")
    print("=" * 30)

    monster = input("\nWhich monster would you like to hunt? (1-3): ")

    
    if monster.isdigit():
        monster = int(monster)
        if monster == 1:
            return "easy"
        elif monster == 2:
            return "medium"
        elif monster == 3:
            return "hard"  
        else: 
            print("Please input a valid number!")
            return ChooseMonster(category)
    else:
        print("Please input a valid number!") 
        return ChooseMonster(category)

# random name picker
def RandomName():
    easy = random.choice(easy_enemies)
    medium = random.choice(medium_enemies)
    hard = random.choice(hard_enemies)
    
    return easy, medium, hard

# random category given
def RandomTask(quesDict):
    keys = list(quesDict.keys())
    return random.choice(keys)

# displays ques and evaluates answer
def HandleQuestion(questionlist, category, difficulty):
    # Select a random question
    random_question = random.choice(questionlist[category][difficulty])
    correct_answer = random_question['answer']
    correct_question_text = random_question['question']
    questionlist[category][difficulty].remove(random_question)


    # Display the question
    print("\n Battle Time! ")
    print("=" * 40)
    print(f"Question ({difficulty.capitalize()}):")
    print(f"{correct_question_text}")
    print("=" * 40)
    
    play_answer = input("\nYour Answer: ").replace(" ", "").lower()
    correct_answer = correct_answer.replace(" ", "").lower()

    if play_answer == correct_answer:
        print("\nCorrect!")
        print("Damage Dealt to the Monster!")
        return True
    else:
        print("\n Wrong!")
        print(f"Damage Received! (The correct answer was: {correct_answer})")
        return False


def StreakCounter(streak,correct,score):
    if correct:
        streak += 1
        if streak >= 3:
            print("Plus Streak Bonus! ")
            score += streakBonus
        return streak, score
    else:
        print(" Streak Broken!")
        return 0, score
    
# gameover screen
def GameOver(score, hp):
    print("\n=== GAME OVER ===")
    if hp <= 0:
        print("You got defeated by the monsters!")
    else:
        print("Out of skills! You decided to pull back for now.")
    
    print(f" Final Score: {score}")
    print("=================")


# handle attacks left
def HandleQuestionsLeft(difficulty, easy_left, medium_left, hard_left):

    if difficulty == "easy":
        if easy_left > 0:
            easy_left -= 1
            print(f"{easy_name}left: {easy_left}")
        else:
            print(f"No{easy_name} left!")
    elif difficulty == "medium":
        if medium_left > 0:
            medium_left -= 1
            print(f"{medium_name} left: {medium_left}")
        else:
            print(f"No {medium_name} left!")
    elif difficulty == "hard":
        if hard_left > 0:
            hard_left -= 1
            print(f"{hard_name} left: {hard_left}")
        else:
            print(f"No {hard_name} left!")
    
    return easy_left, medium_left, hard_left

def HandleDamage(correct, currentScore,enemyhp,difficulty):
    dmg = 0
    plus_score  = 0
    if difficulty == "easy":
        dmg = easy_dmg
        plus_score = easy_enemy_bounty
    elif difficulty == "medium":
        dmg = medium_dmg
        plus_score = medium_enemy_bounty
    elif difficulty == "hard":
        dmg = hard_dmg
        plus_score = hard_enemy_bounty
    if correct:
        enemyhp = enemyhp - dmg 
        print(f"Correct! You dealt {dmg} damage. Enemy HP is now {enemyhp}.")
    else:
        print(f"Incorrect! No damage dealt.Enemy HP is now {enemyhp}.")    
        
    if enemyhp <= 0:
        print("Enemy Defeated!")
        currentScore += plus_score
        print(f"You earned {plus_score} points! Current Score: {currentScore}")
        
    return currentScore,enemyhp 

def SetEnemyHP(difficulty):
    
    if difficulty == "easy":
        return easy_enemy_hp
    elif difficulty == "medium":
        return medium_enemy_hp
    elif difficulty == "hard":
        return hard_enemy_hp

def HandleHP(correct, currentHP,difficulty):
    dmg = 0

    if difficulty == "easy":
        dmg = easy_enemy_dmg

    elif difficulty == "medium":
        dmg = medium_enemy_dmg
    elif difficulty == "hard":
        dmg = hard_enemy_dmg
        
    if not correct:
        currentHP = currentHP - dmg
    return currentHP  
            
def DisplayRoundResult(hp,score,easy,medium,hard,streak):
    print("\n--- Round Summary ---")
    if hp <= 0:
        print(f"HP Left: 0")
    else:
        print(f"HP Left: {hp}")
    print(f"Current Score: {score}")
    
    # Display Remaining Skills
    print("\nSkills Left:")
    print(f"Quick Draw: {easy}")
    print(f"Ambush: {medium}")
    print(f"Dead Eye: {hard}")

    # Display Current Streak
    print(f"\nCurrent Streak: {streak} {'(Bonus Active!)' if streak >= 3 else ''}")
    
    print("\n--------------------")

def LoadQuestions(file_path):
    questions = {}

    with open(file_path, "r") as file:
        current_category = None
        current_difficulty = None

        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith("category:"):
                current_category = line.split(":", 1)[1].strip()
                if current_category not in questions:
                    questions[current_category] = {}

            elif line.startswith("difficulty:"):
                current_difficulty = line.split(":", 1)[1].strip()
                if current_difficulty not in questions[current_category]:
                    questions[current_category][current_difficulty] = []

            elif line.startswith("question:"):
                question = line.split(":", 1)[1].strip()

            elif line.startswith("answer:"):
                answer = line.split(":", 1)[1].strip()
                if current_category and current_difficulty:
                    questions[current_category][current_difficulty].append({
                        "question": question,
                        "answer": answer
                    })

    return questions

