#question
#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second highest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

#solution
N = int(input("Enter the number of students in the class : "))
records = []
grades = []
dic = {}
for i in range(N):
    #Taking input
    name = input("Enter the name of the student : ")
    grade = int(input("Enter the number obtained by the student : "))
    #Making the dictionary
    dic[name]=grade
    #Making a nested list
    grades.append(grade)
    small_list = [name,grade]
    records.append(small_list)
    
    

print(f"The name & grades of the students are {records}")
print(dic)

#finding the 2nd largest element
temp = sorted(set(grades))
second_largest = temp[(len(temp))-2]
print(second_largest)

#printing the names 
sorted_names = []
for name,grade in dic.items():
    if grade == second_largest:
        sorted_names.append(name)

sorted_names.sort()
print(f"The names of the Students Having The 2nd Highest Score are : {sorted_names}")
