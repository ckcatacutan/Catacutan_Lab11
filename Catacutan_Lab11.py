student_grades = []
students = 0

while True:
        grade_input = (input("Enter grade for student: "))
        
        if grade_input.lower() == "done":
            break
            
        if 40 <= float(grade_input) <= 100:
            student_grades.append(float(grade_input))
            students +=1
            
        else:
            print("Error: Invalid grade. Grade must be between 40 and 100")    
                      
avg_grade = sum(student_grades) / len(student_grades)

passing_grade = 0 
for grade_input in student_grades:
    if grade_input >= 75: 
        passing_grade += 1
        
percentage = (passing_grade / len(student_grades)) * 100

print("Grades: ", student_grades)
print(f"Average Grade: ", avg_grade)
print(f"Passing Grade: ", passing_grade)
print(f"Passing Percentage: ", percentage, "%")