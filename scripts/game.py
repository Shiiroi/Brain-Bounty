import random

def Play(task):
    print(f"Assigned task {task}")


def RandomTask(quesDict):
    return random.choice(list(quesDict.keys()))


def LoadQuestions(file_path):
    questions = {}

    with open(file_path, "r") as file:
        current_category = None
        current_difficulty = None

        for line in file:
            line = line.strip()

            if not line:  # Skip empty lines
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
                # Add the question-answer pair to the current category and difficulty
                if current_category and current_difficulty:
                    questions[current_category][current_difficulty].append({
                        "question": question,
                        "answer": answer
                    })

    return questions
