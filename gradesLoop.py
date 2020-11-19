total_score = 0
for grades in range(5):
    score = int(input("Please enter your grade: "))
    total_score += score
average = total_score / 5
letter = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
if average >= 93 and average <= 100:
    print(f"For an average of {average}, your grade is a {letter[0]}")
elif average >= 90 and average <= 93:
    print(f"For an average of {average}, your grade is a {letter[1]}")
elif average >= 87 and average <= 90:
    print(f"For an average of {average}, your grade is a {letter[2]}")
elif average >= 83 and average <= 87:
    print(f"For an average of {average}, your grade is a {letter[3]}")
elif average >= 80 and average <= 83:
    print(f"For an average of {average}, your grade is a {letter[4]}")
elif average >= 77 and average <= 80:
    print(f"For an average of {average}, your grade is a {letter[5]}")
elif average >= 73 and average <= 77:
    print(f"For an average of {average}, your grade is a {letter[6]}")
elif average >= 70 and average <= 73:
    print(f"For an average of {average}, your grade is a {letter[7]}")
elif average >= 67 and average <= 70:
    print(f"For an average of {average}, your grade is a {letter[8]}")
elif average >= 63 and average <= 67:
    print(f"For an average of {average}, your grade is a {letter[9]}")
elif average >= 60 and average <= 63:
    print(f"For an average of {average}, your grade is a {letter[10]}")
else:
    print(f"For an average of {average}, your grade is a {letter[11]}")

