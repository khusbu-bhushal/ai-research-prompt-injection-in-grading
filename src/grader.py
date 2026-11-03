import ollama

#grader builds the prompt, calls Ollama with settings, and reads back the integer
#grader will then be used in both baseline.py and attack.py

#step 1: build prompt

def build_prompt(question, ideal_answer, student_answer):
    return f"""You are a fair grader. Score the student's answer from 0 to 10 and return only one integer.
    Question: {question}
    Ideal_answer: {ideal_answer}
    Student_answer: {student_answer}
    Score in terms of 1 to 10: """

print(build_prompt("what is 2+2" , "4", "four"))

#function that takes prompt as a text, sends it to Ollama and returns model's reply as a text
def ask_model(prompt):
    response = ollama.chat(
        model="mistral:v0.2",
        messages=[{"role": "user", "content": prompt}]
        options={"temperature": 0, "seed": 42},
    )
    return response


