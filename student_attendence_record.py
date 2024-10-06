def attendance(students, present):
    return {student: 'Present' if student in present else 'Absent' for student in students}
students = ['Ram', 'Sita', 'Lakshman']
present = ['Ram', 'Lakshman']
print(attendance(students, present))
