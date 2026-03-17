#Student Record Analyzer (Python Mini Project)
#Solution - Task - 1
n = int(input("Enter the total no of students in the class : "))
records = []
for i in range(n):
    name = input("Enter the name of the student : ")
    mark = int(input("Enter the marks of the student : "))
    temp_list = [name,mark]
    records.append(temp_list)
print(records)


#TSolution - Task - 2
for i in range(len(records)):
    if records[i][1] >= 90:
        records[i].append('A')
    elif records[i][1] >= 75 and records[i][1]<=89 :
        records[i].append('B')
    elif records[i][1] >= 50 and records[i][1]<=74 :
        records[i].append('C')
    elif records[i][1] < 50 :
        records[i].append("Fail")
print(records)


#Solution - Task - 3
grades = []
total = 0
for i in range(len(records)):
    total=total+records[i][1]
    grades.append(records[i][1])

grades.sort()
length = len(grades)
average = total/length

print(f"The Highest Marks Obtained is : {grades[length-1]}")
print(f"The Lowest Marks Obtained is : {grades[0]}")
print(f"The Average Marks Obtained is : {average}")


#Solution - Task - 4
highest = grades[length-1]
lowest = []
print("The student(s) who are the TOP PERFORMERS are : ")
for i in range(len(records)):
    if records[i][1] == highest:
        print(records[i][0])
    elif records[i][1] < 50 :
        lowest.append(records[i][0])

print("The students who failed are : ",lowest)
