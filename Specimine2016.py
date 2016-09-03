studentNames = []

studentMarks_1 = []
studentMarks_2 = []
studentMarks_3 = []

studentTotalScore = []

classTotalScore = 0
classAverageTotalScore = 0
highestScore = 0

print("Test one: 20 marks \nTest two: 25 marks \nTest three: 35 marks")
for x in range(len(studentNames), 30):
    tempStudentName = str(input("\nInput student number " + str(x+1) + "'s name: "))
    studentNames.append(tempStudentName)

    tempStudentMarks_1 = int(input("Input student's score for the first test: "))

    if tempStudentMarks_1 > 20 or tempStudentMarks_1 < 0:
        print("Invalid input; Please input a number between 0 and 20")
        tempStudentMarks_1 = int(input("Input student's score for the first test again: "))
        if tempStudentMarks_1 > 20 or tempStudentMarks_1 < 0:
            exit("Wrong input twice; exiting...")
        else:
            studentMarks_3.append(tempStudentMarks_3)
    else:
        studentMarks_1.append(tempStudentMarks_1)

    tempStudentMarks_2 = int(input("Input student's score for the second test: "))

    if tempStudentMarks_2 > 25 or tempStudentMarks_2 < 0:
        print("Invalid input; Please input a number between 0 and 25")
        tempStudentMarks_2 = int(input("Input student's score for the second test again: "))
        if tempStudentMarks_2 > 25 or tempStudentMarks_2 < 0:
            exit("Wrong input twice; exiting...")
        else:
            studentMarks_3.append(tempStudentMarks_3)
    else:
        studentMarks_2.append(tempStudentMarks_2)

    tempStudentMarks_3 = int(input("Input student's score for the third test: "))

    if tempStudentMarks_3 > 35 or tempStudentMarks_3 < 0:
        print("Invalid input; Please input a number between 0 and 35")
        tempStudentMarks_3 = int(input("Input student's score for the third test again: "))
        if tempStudentMarks_3 > 35 or tempStudentMarks_3 < 0:
            exit("Wrong input twice; exiting...")
        else:
            studentMarks_3.append(tempStudentMarks_3)
    else:
        studentMarks_3.append(tempStudentMarks_3)

    print(studentNames)
    print(studentMarks_1)
    print(studentMarks_2)
    print(studentMarks_3)
print("---------------------------------------------------------------------------------------------")

for x in range(0, len(studentNames)):
    test1 = studentMarks_1[x]
    test2 = studentMarks_2[x]
    test3 = studentMarks_3[x]
    totalScore = (test1 + test2 + test3)
    studentTotalScore.append(totalScore)
    print(studentNames[x] + "'s total score is", studentTotalScore[x])
print("---------------------------------------------------------------------------------------------")

for x in range(0, len(studentTotalScore)):
    classTotalScore += studentTotalScore[x]

classAverageTotalScore = classTotalScore / len(studentNames)

print("\nClass Average Total Score:", classAverageTotalScore)
print("---------------------------------------------------------------------------------------------")

for x in range(0, len(studentTotalScore)):
    if studentTotalScore[x] > highestScore:
        highestScore = studentTotalScore[x]

print("\nHighest score[s] are:")
for x in range(0, len(studentTotalScore)):
    if highestScore == studentTotalScore[x]:
        print(studentNames[x] + "'s at total test score:", studentTotalScore[x])