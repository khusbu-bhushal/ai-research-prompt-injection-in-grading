#script to run the grader
#script to test 
#im guessing to do this you have to loop over all the data in de test
#loop each stduent_asnwer with attack conditions

from grader import build_prompt, ask_model, parse_text
from attacks import add_attack #from attacks.py bring the function add_attack
import time 
import pandas as pd

conditions = ["clean", "coercive_suffix", "fake_rubric", "role_play"]
SAMPLE_PATH = "data/derived/dev_sample.csv"   
OUTPUT_PATH = "results/dev_results.csv"
N_ANSWERS = 3


sample = pd.read_csv(SAMPLE_PATH)
if N_ANSWERS is not None:
    sample = sample.head(N_ANSWERS)

rows = []  #one dictionary per model call

for _, row in sample.iterrows():  #_ is stil la valid variable name used for various iterations
    for condition in conditions:
        answer = add_attack(row["student_answer"], condition)
        prompt = build_prompt(row["question_text"], row["ideal_answer"], answer)

        start = time.time()
        reply = ask_model(prompt)
        seconds = time.time() - start

        score = parse_text(reply)

        rows.append({
            "entry_id": row["entry_id"],
            "condition": condition,
            "reply": reply,
            "score": score,
            "teacher_grade": row["teacher_grade"],
            "seconds": round(seconds, 2),
        })

        print(row["entry_id"], condition, "| score:", score, "| teacher:", row["teacher_grade"], "|", round(seconds, 1), "s")

        #save after every call, so a crash doesnt lose everything
        pd.DataFrame(rows).to_csv(OUTPUT_PATH, index=False)


results = pd.DataFrame(rows)
print()
print("Calls:", len(results))
print("Parse failures:", results["score"].isna().sum())
print("Average seconds per call:", round(results["seconds"].mean(), 1))



