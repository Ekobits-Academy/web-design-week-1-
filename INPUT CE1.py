print('Good Morning. This is a Program to take the names, test scores and exam scores of five students and find the mean of their exam scores')
stu1=input("Hello first Student!Please enter your name:")
stu11= int(input("Thanks! Please enter your test score:"))
stu111= int(input("Great! Finally enter your exam score please:"))
stu12= stu11 + stu111
print("Hello {}. Your total score is {}".format(stu1, stu12))
print()
print("Next student Please!")
print()
stu2=input("Hello second Student!Please enter your name:")
stu22= int(input("Thanks! Please enter your test score:"))
stu222= int(input("Great! Finally enter your exam score please:"))
stu23= stu22 + stu222
print("Hello {}. Your total score is {}".format(stu2, stu23))
print()
print("Next student Please!")
print()
stu3=input("Hello third Student!Please enter your name:")
stu33= int(input("Thanks! Please enter your test score:"))
stu333= int(input("Great! Finally enter your exam score please:"))
stu34= stu33 + stu333
print("Hello {}. Your total score is {}".format(stu3, stu34))
print()
print("Next student Please!")
print()
stu4=input("Hello fourth Student!Please enter your name:")
stu44= int(input("Thanks! Please enter your test score:"))
stu444= int(input("Great! Finally enter your exam score please:"))
stu45= stu44 + stu444
print("Hello {}. Your total score is {}".format(stu4, stu45))
print()
print("Next student Please!")
print()
stu5=input("Hello fifth and final Student!Please enter your name:")
stu55= int(input("Thanks! Please enter your test score:"))
stu555= int(input("Great! Finally enter your exam score please:"))
stu56= stu55 + stu555
print("Hello {}. Your total score is {}".format(stu5, stu56))
totalscores=stu12 + stu23 + stu34 + stu45 + stu56
mean= totalscores/5
print("Thank you all for your help! I will now compute the mean of your total scores")
print("THE MEAN OF THE FIVE STUDENT'S TOTAL SCORES IS %.2f"%(mean))


