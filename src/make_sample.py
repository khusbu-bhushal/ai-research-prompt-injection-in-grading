#picks 50 student answers that it iwll test and saves them to a file. That file can be reused again later.
#we are only sampling 100 out of 3000 and running them before doing large dataset
#teacher_grade is human grade that the model never sees and compare it later to see how close it would be to the model's answer
#this is just a sample set and not a baseline set

import pandas as pd  #go to library to import dataset thats in csv
full_dataset = pd.read_csv("data/raw/dataset_en.csv")  #load the data from a CSV file
print(len(full_dataset))

#checking below to see which dataset is empty:
#print(full_dataset["student_answer"].isna().sum()) #checking to see if there are any missing values
#print(full_dataset[full_dataset["entry_id"] == 218][["entry_id", "student_answer", "teacher_grade"]])

#adding the filter 
#.notna() detects missing and non existing values in dataframe from python panda library

#checking where (.notna() and < 10) produce True or False for each row below.
filtered_dataset = full_dataset[(full_dataset["student_answer"].notna()) & (full_dataset["teacher_grade"] < 10)]
print(len(filtered_dataset))  #comebacktothisfromyourlog

#choose 100 samplesize from filtered_dataset
pilot_sample = filtered_dataset.sample(n=100, random_state=42)
print(pilot_sample)

#save the sample to derived 
pilot_sample.to_csv('data/derived/pilot_sample.csv', index=False)
