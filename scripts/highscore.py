# Magwili, Vince Roi S.
# Section Y-3L
# hanldes loading and saving of hs

def EnterName():
    return input("Enter Name: ")
    
def Save(name,score):
    with open("./highscores/highscores.dat", "a") as fileWriter:
        fileWriter.write(f"{name}:{score}\n")
        
        
def Load(highscores):
    with open("./highscores/highscores.dat", "r") as fileReader:
        for line in fileReader:
            info = line.strip().split(":")  
            name = info[0]
            score = info[1]
            highscores[name] = score

        
def DisplayHS(highscores):
    
    print()
    print("=" * 30)
    print("======== HIGH SCORES =========")
    print("=" * 30)
    print(f"\n{'Name':<15}{'Score'}")
    print("-" * 30)
    # makes list from data
    highscore_list = []
    for name, score in highscores.items():
        highscore_list.append([name, int(score)])

    # sorting algo from lect to arrange hs
    for i in range(len(highscore_list)):
        for j in range(i + 1, len(highscore_list)):
            if highscore_list[i][1] < highscore_list[j][1]:
                highscore_list[i], highscore_list[j] = highscore_list[j], highscore_list[i]
        
    
    # Display the top 5 high scores
    for i, (name, score) in enumerate(highscore_list[:5]):
        print(f"{name:<15}{score}")
    
    # Print the bottom border
    print("-" * 30)