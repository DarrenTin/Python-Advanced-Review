import csv
import random

def load_questions(file_path, file_type="csv"):
    """
    Loads quiz questions from a CSV or TXT file.
    
    :param file_path: The path to the quiz file.
    :param file_type: 'csv' for CSV format, 'txt' for text format.
    :return: Dictionary with categories as keys and list of questions as values.
    """
    questions_dict = {}

    try:
        if file_type == "csv":
            with open(file_path, newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    category = row["category"].strip().lower()
                    question = row["question"].strip()
                    correct = row["correct"].strip()
                    wrong_answers = [row["wrong1"].strip(), row["wrong2"].strip(), row["wrong3"].strip()]
                    
                    if category not in questions_dict:
                        questions_dict[category] = []
                    questions_dict[category].append({"question": question, "correct": correct, "wrong_answers": wrong_answers})

        elif file_type == "txt":
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    parts = [p.strip() for p in line.split("|")]
                    if len(parts) == 5:
                        category, question, correct, wrong1, wrong2, wrong3 = parts
                        category = category.lower()
                        if category not in questions_dict:
                            questions_dict[category] = []
                        questions_dict[category].append({"question": question, "correct": correct, "wrong_answers": [wrong1, wrong2, wrong3]})
        else:
            return None
        
        return questions_dict

    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return None

def run_quiz(questions_dict, category="general", num_questions=3):
    """
    Runs the quiz by selecting random questions from a category.
    
    :param questions_dict: Dictionary containing quiz data.
    :param category: Category of questions.
    :param num_questions: Number of questions to ask.
    """
    if category not in questions_dict:
        print("❌ Invalid category! Choose from:", ", ".join(questions_dict.keys()))
        return
    
    questions = random.sample(questions_dict[category], min(num_questions, len(questions_dict[category])))
    score = 0

    print(f"\n📚 {category.capitalize()} Quiz 📚\n")

    for i, q in enumerate(questions, 1):
        options = [q["correct"]] + q["wrong_answers"]
        random.shuffle(options)  # Randomly assign A, B, C, D

        correct_letter = "ABCD"[options.index(q["correct"])]  # Get correct answer letter
        option_map = {letter: option for letter, option in zip("ABCD", options)}

        print(f"{i}. {q['question']}")
        for letter, option in option_map.items():
            print(f"{letter}) {option}")

        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if answer == correct_letter:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {correct_letter}) {q['correct']}.\n")

    print(f"🎯 Quiz Completed! Your Score: {score}/{num_questions}\n")

# Main program
if __name__ == "__main__":
    print("🎓 Random Quiz Generator 🎓")

    file_type = input("Enter file type ('csv' or 'txt', default: csv): ").strip().lower() or "csv"
    file_path = input("Enter the path to your quiz file (default: quiz_questions.csv): ").strip() or "quiz_questions.csv"

    questions_dict = load_questions(file_path, file_type)
    
    if questions_dict:
        print("\nAvailable categories:", ", ".join(questions_dict.keys()))
        user_category = input("Choose a category (default: general): ").strip().lower()
        category = user_category if user_category in questions_dict else "general"

        user_count = input("Enter number of questions (default: 3): ").strip()
        num_questions = int(user_count) if user_count.isdigit() else 3

        run_quiz(questions_dict, category, num_questions)
