import random

def scores_and_grades():
    print "Scores and Grades"
    for x in range (0, 10):
        grade = random.randint(60,100)
        if grade < 70:
            letter = 'D'
        elif grade < 80:
            letter = 'C'
        elif grade < 90:
            letter = 'B'
        else:
            letter = 'A'
        print "Score: {}; Your grade is {}".format(grade, letter)
    print "End of the program. Bye!"

# Test it out
scores_and_grades()