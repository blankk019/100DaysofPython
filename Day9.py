student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for key, value in student_scores.items():
    if value >= 91 and value <= 100:
        student_grades[key] = "Outstanding"
    if value <= 90 and value >= 81:
        student_grades[key] = "Exceeds Expectations"
    if value <= 80 and value >= 71:
        student_grades[key] = "Acceptable"
    if value < 70:
        student_grades[key] = "Fail"
