import pandas as pd

full_dataset = pd.read_csv("data/raw/dataset_en.csv")
pilot_sample = pd.read_csv("data/derived/pilot_sample.csv")

# same filter as the pilot
filtered_dataset = full_dataset[
    (full_dataset["student_answer"].notna()) & (full_dataset["teacher_grade"] < 10)
]

# drop every answer that is already in the pilot
#tilda helps you flip bit: ~x equals -x - 1, so ~0 is -1 and ~-1 is 0.
not_in_pilot = filtered_dataset[
    ~filtered_dataset["entry_id"].isin(pilot_sample["entry_id"]) #REVISIT True (in the pilot) becomes False, and False (not in the pilot) becomes True.
]

dev_sample = not_in_pilot.sample(n=20, random_state=7)
dev_sample.to_csv("data/derived/dev_sample.csv", index=False)

print(len(not_in_pilot))    # expect 2842
print(len(dev_sample))      # expect 20
print(dev_sample["entry_id"].isin(pilot_sample["entry_id"]).sum())   # expect 0