import unittest
import os
from app import load_questions, save_response

class TestSurveyApp(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        self.test_questions_file = "test_questions.txt"
        self.test_responses_file = "test_responses.txt"

        # Create a sample questions file for testing
        with open(self.test_questions_file, "w") as file:
            file.write("What is your favorite color?\n")
            file.write("What is your favorite food?\n")
            file.write("What is your hobby?\n")

    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_questions_file):
            os.remove(self.test_questions_file)
        if os.path.exists(self.test_responses_file):
            os.remove(self.test_responses_file)

    def test_load_questions(self):
        """Test if questions are correctly loaded from the file."""
        questions = load_questions(self.test_questions_file)
        self.assertEqual(len(questions), 3)
        self.assertEqual(questions[0], "What is your favorite color?")
        self.assertEqual(questions[1], "What is your favorite food?")
        self.assertEqual(questions[2], "What is your hobby?")

    def test_save_response(self):
        """Test if responses are correctly saved to the file."""
        name = "Test User"
        email = "test@example.com"
        answers = ["Blue", "Pizza", "Football"]

        save_response(self.test_responses_file, name, email, answers)

        with open(self.test_responses_file, "r") as file:
            content = file.read()

        # Verify content
        self.assertIn("Name: Test User", content)
        self.assertIn("Email: test@example.com", content)
        self.assertIn("Q1: Blue", content)
        self.assertIn("Q2: Pizza", content)
        self.assertIn("Q3: Football", content)

    def test_load_questions_with_missing_file(self):
        """Test behavior when the questions file is missing."""
        missing_file = "nonexistent_file.txt"
        questions = load_questions(missing_file)
        self.assertEqual(questions, [])

if __name__ == "__main__":
    unittest.main()
