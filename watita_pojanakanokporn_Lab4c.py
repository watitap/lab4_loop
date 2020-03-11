# This is to calculate the grade of students
# Vars
myGrade = 0.0
count = 0
totalGrade = 0

# Input
myGrade = float(input('Enter your grade (0-100), or -1 to stop: '))

while myGrade > 0:
    if myGrade >= 90:
        print("Congratulations! You've got an A\n")
    elif myGrade >= 80:
        print("Not bad! You've got a B\n")
    elif myGrade >= 70:
        print("Study harder! You've got a C\n")
    elif myGrade >= 60:
        print("You barely passed. You've got a D\n")
    else:
        print("Obviously you didn't study. You've got an F\n")
    count += 1
    totalGrade = totalGrade + myGrade
    myGrade = float(input('Enter another grade, or -1 to stop: '))

if count > 0:
    averageGrade = float(totalGrade / count)
    print('\nYour average grade is', format(averageGrade, '.2f'),'%.')
    print('This is based on', count, 'total number of assignments entered')