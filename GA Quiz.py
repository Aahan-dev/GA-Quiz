class QuizGame:
    def __init__(self):
        """Initialize the quiz game with questions and answers."""
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
                "answer": "C"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
                "answer": "B"
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) J.K. Rowling"],
                "answer": "C"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
                "answer": "D"
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
                "answer": "C"
            },
        ]
        self.score = 0  # Initialize the score

    def ask_question(self, question):
        """
        Ask a question and get the user's answer.


        Args:
            question (dict): A dictionary containing the question, options, and correct answer.


        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        print(question["question"])  # Display the question
        for option in question["options"]:
            print(option)  # Display the options


        answer = input("Your answer (A/B/C/D): ").strip().upper()  # Get user's answer
        if answer == question["answer"]:
            print("Correct!\n")
            return True
        else:
            print(f"Wrong! The correct answer was {question['answer']}.\n")
            return False


    def run(self):
        """Run the quiz game."""
        print("Welcome to the Quiz Game!\n")
        for question in self.questions:
            if self.ask_question(question):
                self.score += 1  # Increment score for a correct answer


        # Display the final score
        print(f"You scored {self.score} out of {len(self.questions)}.")


if __name__ == "__main__":
    # Create an instance of QuizGame and run it
    quiz_game = QuizGame()
    quiz_game.run()