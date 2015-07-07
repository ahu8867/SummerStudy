
subject1 = raw_input()
score1 = input()
subject2 = raw_input()
score2 = input()
subject3 = raw_input()
score3 = input()
sum = score1 + score2 + score3
average = float(sum)/3

print str(subject1) + ": " + str(score1) + ' score'
print str(subject2) + ": " + str(score2) + ' score'
print str(subject3) + ": " + str(score3) + ' score'
print "total score: " + str(sum) + ' score'
print "average score: " + str(round(average, 3)) + ' score'