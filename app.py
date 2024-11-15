import streamlit as st
import os

# File paths
QUESTIONS_FILE = "questions.txt"
RESPONSES_FILE = "responses.txt"

# Load questions from a file
def load_questions(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            questions = [line.strip() for line in file.readlines() if line.strip()]
        return questions
    return []

# Save responses to a file
def save_response(filename, name, email, answers):
    with open(filename, "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        for i, answer in enumerate(answers, start=1):
            file.write(f"Q{i}: {answer}\n")
        file.write("\n")

# Main app
def main():
    st.title("Survey App")
    st.write("Please fill out the survey below:")
    
    # Load questions
    questions = load_questions(QUESTIONS_FILE)
    
    if not questions:
        st.error("No questions found. Please ensure 'questions.txt' is present and has questions.")
        return
    
    # User input for name and email
    name = st.text_input("Name")
    email = st.text_input("Email")
    
    # User input for survey questions
    responses = []
    for question in questions:
        responses.append(st.text_input(question))
    
    # Submit button
    if st.button("Submit"):
        if not name or not email or any(not ans for ans in responses):
            st.error("All fields are required!")
        else:
            save_response(RESPONSES_FILE, name, email, responses)
            st.success("Thank you for completing the survey!")
            st.write("Your responses have been recorded.")

if __name__ == "__main__":
    main()
