def gradingStudents(grades):
    # Write your code here
    parsed_grades = []
    for grade in grades:
        if grade <38:
            parsed_grades.append(grade)
        else:
            for _ in range(1,3):
                grade += 1
                if grade%5 == 0:
                    break
            if grade%5 != 0:
                grade -=3
            parsed_grades.append(grade)
    return parsed_grades

a = gradingStudents([10,67,54,35,42])
print(a)