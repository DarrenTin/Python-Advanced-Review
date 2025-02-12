import random

# Quiz questions dictionary
quiz_questions = {
    "general": [
        {"question": "What is the capital of France?", "options": ["A) London", "B) Paris", "C) Rome", "D) Berlin"], "answer": "B"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"], "answer": "B"},
        {"question": "How many continents are there?", "options": ["A) 5", "B) 6", "C) 7", "D) 8"], "answer": "C"}
    ],
    "science": [
        {"question": "What is H2O commonly known as?", "options": ["A) Oxygen", "B) Hydrogen", "C) Water", "D) Helium"], "answer": "C"},
        {"question": "Which gas do plants absorb from the atmosphere?", "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"], "answer": "B"},
        {"question": "What is the chemical symbol for gold?", "options": ["A) Au", "B) Ag", "C) Fe", "D) Hg"], "answer": "A"}
    ],
    "history": [
        {"question": "Who was the first President of the United States?", "options": ["A) Abraham Lincoln", "B) George Washington", "C) John Adams", "D) Thomas Jefferson"], "answer": "B"},
        {"question": "In which year did World War II end?", "options": ["A) 1940", "B) 1945", "C) 1950", "D) 1939"], "answer": "B"},
        {"question": "Who discovered America?", "options": ["A) Christopher Columbus", "B) Vasco da Gama", "C) Marco Polo", "D) Ferdinand Magellan"], "answer": "A"}
    ],
    "technology": [
        {"question": "Who founded Microsoft?", "options": ["A) Steve Jobs", "B) Bill Gates", "C) Elon Musk", "D) Mark Zuckerberg"], "answer": "B"},
        {"question": "What does CPU stand for?", "options": ["A) Central Processing Unit", "B) Computer Processing Unit", "C) Core Processor Utility", "D) Central Power Unit"], "answer": "A"},
        {"question": "Which programming language is known as the 'mother' of all languages?", "options": ["A) Java", "B) C", "C) Python", "D) Assembly"], "answer": "B"}
    ]
}

def generate_quiz(category="general", num_questions=3):
    """
    Generates a random quiz from a given category.
    
    :param category: The category of the quiz (default: "general").
    :param num_questions: Number of questions to ask.
    """
    if category not in quiz_questions:
        return "❌ Error: Invalid category! Choose from: " + ", ".join(quiz_questions.keys())

    # Select random questions
    questions = random.sample(quiz_questions[category], min(num_questions, len(quiz_questions[category])))
    
    score = 0
    print(f"\n📚 {category.capitalize()} Quiz 📚\n")

    for i, q in enumerate(questions, 1):
        print(f"{i}. {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}.\n")

    print(f"🎯 Quiz Completed! Your Score: {score}/{num_questions}\n")

# Main program
if __name__ == "__main__":
    print("🎓 Random Quiz Generator 🎓")

    # User selects category
    print("\nAvailable categories:", ", ".join(quiz_questions.keys()))
    user_category = input("Choose a category (default: general): ").strip().lower()
    category = user_category if user_category in quiz_questions else "general"

    # User selects number of questions
    user_count = input("Enter number of questions (default: 3): ").strip()
    num_questions = int(user_count) if user_count.isdigit() else 3

    # Start quiz
    generate_quiz(category, num_questions)
