marks={
    "Physics":90, "Chemistry":92,"Math":96
}
marks["Biology"]=94
marks["Physics"] = 91
print(marks)
total_marks= 0
for i in marks:
    total_marks+=marks[i]
subjects= len(marks)
avg= total_marks / subjects
print("Averge marks = ", avg)