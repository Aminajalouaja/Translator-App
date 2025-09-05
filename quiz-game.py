print("welcome to my new game")
a=input("do you want to play a game ?   ")
if a!="yes" :
    quit()
print("okay ! let's start the game !!!")  

score=0
questions=0


questions=+1
answer =input("what does CPU stand for ?   ")
if answer == "central processing unit" :
    print("correct")
    score+=1
    
else:
    print("incorrect")
    print("the correct answer is central processing unit ")


questions=+1
answer2=input("what does GPU stand for ?   ")
if answer2 == "graphics processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")
    print("the correct answer is graphics processing unit ")

questions += 1
answer3 = input("What does RAM stand for?  ")
if answer3.lower() == "random access memory":
    print("Correct ")
    score += 1
else:
    print("Incorrect ")
    print("The correct answer is: Random Access Memory")
        
questions += 1
answer4 = input("What does PSU stand for?  ")
if answer4.lower() == "power supply unit":
    print("Correct ")
    score += 1
else:
    print("Incorrect ")
    print("The correct answer is: Power Supply Unit")


questions += 1
answer5 = input("What does SSD stand for?  ")
if answer5.lower() == "solid state drive":
    print("Correct ")
    score += 1
else:
    print("Incorrect ")
    print("The correct answer is: Solid State Drive")



print(f"\nYou answered {score} out of {questions} questions correctly!")

