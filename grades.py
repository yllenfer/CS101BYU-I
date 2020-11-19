grade = float(input("What was your final grade?: "))
letter = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
if grade >= 93 and grade <= 100:
    print(f"For a score of {grade}, your grade is a {letter[0]}")
elif grade >= 90 and grade <= 93:
    print(f"For a score of {grade}, your grade is a {letter[1]}")
elif grade >= 87 and grade <= 90:
    print(f"For a score of {grade}, your grade is a {letter[2]}")
elif grade >= 83 and grade <= 87:
    print(f"For a score of {grade}, your grade is a {letter[3]}")
elif grade >= 80 and grade <= 83:
    print(f"For a score of {grade}, your grade is a {letter[4]}")
elif grade >= 77 and grade <= 80:
    print(f"For a score of {grade}, your grade is a {letter[5]}")
elif grade >= 73 and grade <= 77:
    print(f"For a score of {grade}, your grade is a {letter[6]}")
elif grade >= 70 and grade <= 73:
    print(f"For a score of {grade}, your grade is a {letter[7]}")
elif grade >= 67 and grade <= 70:
    print(f"For a score of {grade}, your grade is a {letter[8]}")
elif grade >= 63 and grade <= 67:
    print(f"For a score of {grade}, your grade is a {letter[9]}")
elif grade >= 60 and grade <= 63:
    print(f"For a score of {grade}, your grade is a {letter[10]}")
else:
    print(f"For a score of {grade}, your grade is a {letter[11]}")
