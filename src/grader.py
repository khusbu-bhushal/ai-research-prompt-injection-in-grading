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

