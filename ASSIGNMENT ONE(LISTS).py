print('ASSIGNMENT')
print()
print('1. LIST SHOWING SCORES OF SEVEN STUDENTS')
scores = [100, 99, 97, 94, 86, 75, 81]
print(scores)
print()
print('2. EDIT 3RD, 5TH AND 6TH SCORES WITH NAMES')
scores[2] = 'SOTI'
scores[4] = 'DEMILARE'
scores[5] = 'HARUNA'
print(scores)
print()
print('3. ADDITION OF 3 SCORES')
scores.append(90)
scores.append(72)
scores.append(65)
print(scores)
print()
print('4. REMOVAL OF 3RD AND LAST VALUES')
del scores[2]
del scores[8]
print(scores)

