
quiz = [
    {
        "question": "What is the stadium of Barcelona?",
        "options": ["A. Camp Nou", "B. Santiago bernabeu", "C. Old Trafford", "D. San Siro"],
        "answer": "A"
    },
    {
        "question": "How many UCL does AC MILAN have?",
        "options": ["A. 0", "B. 7", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Team with the most UCL is?",
        "options": ["A. Inter Milan", "B. F. Liverpool", "C. Real Madrid", "D. Barcelona"],
        "answer": "C"
    }
]


def run_quiz(quiz):
    score = 0
    for question in quiz:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {question['answer']}.")
    
    print(f"\nYou got {score} out of {len(quiz)} questions right.")


def main():
    print("Welcome to Football Quiz!")
    print("Answer the questions by choosing A, B, C, or D.")
    run_quiz(quiz)


if __name__ == "__main__":
    main()
