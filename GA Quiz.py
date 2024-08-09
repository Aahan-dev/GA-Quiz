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

    