#Open Text file and read test answers into list Y
x = open("test_answers.txt", "r")
readfile_to_list = x.read()
y = readfile_to_list.split(",")
test_answers = y
x.close()

#Open Text file and read Student answers into list N
m = open("student_answers.txt", "r")
readfile_to_list = m.read()
n = readfile_to_list.split(",")
student_answers = n
m.close()

#Setting up my empty variables
index = 0
correct = 0
incorrect = 0
incorrectly_answered_questions = []

#Looping through both lists
for i in y:
    if y[index] == n[index]:
        print("{}. Correct, Great Job!".format(index+1))
        index = index + 1
        correct = correct + 1
    elif y[index] != n[index]:
        print("{}. {} was incorrect, the correct answer was {}.".format(index+1,n[index],y[index]))
        incorrect = incorrect + 1
        incorrectly_answered_questions.append(index+1)
        index = index + 1
    else:
        print("Error: Check filename or file location")

#Calculating the Students Score
passtest = (15 / 20) * 100
test_score = (correct / 20) * 100

print()
print("Correct Answers: {} \nIncorrect Answers: {}".format(correct, incorrect))

if test_score >= passtest:
    print("You have passed the exam! Your score was {}%".format(test_score))
elif test_score < passtest:
    print("You failed the test. Your score was {}%".format(test_score))

print("Here is a list of which questions were answered incorrectly: {}.".format(incorrectly_answered_questions))