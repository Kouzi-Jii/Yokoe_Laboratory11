passed_count = 0
all_grades = []

for grade in range(5):
    grade = float(input("Enter Grade: "))
    if grade >= 40 and grade <= 100:
        if grade >= 75:
            passed_count += 1
    else:
        print("Your entered grade is invalid, Please try again!")
        break
    all_grades.append(grade)
    if len(all_grades) == 5:
        sum_grade = all_grades[0] + all_grades[1] + all_grades[2] + all_grades[3] + all_grades[4]
        average_grade = sum_grade / 5
        pass_percents = (passed_count / 5) * 100
        print(f"Entered Grades: {all_grades}")
        print(f"Average grade: {average_grade}")
        print(f"Passing Percentage: {pass_percents}%")
        print(f"Number of students who passed: {passed_count}")