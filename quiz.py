questions=("Who is father of our nation ?",
"Who invented Computer",
"Which is the smallest state of India ?",
"Fastest animal on earth is ?")
options=(("A.MahatmaGandhi","B.Jawaharla Nehru","C.BhagatSingh","D.ChandraBose"),
          ("A.Newton","B.Thomas Edison","C.Charles Babbage","D.Aristotle"),
          ("A.Kerala","B.Goa","C.Punjab","D.Odisha"),
          ("A.Dog","B.Tiger","C.Leopard","D.Cheetah"))
guesses=[]
answers=('A','C','B','D')
ques_num=0
score=0
for question in questions:
    print('--------------------------------------')
    print(question)
    print(options[ques_num])
    guess=input("Enter your answer").upper()
    guesses.append(guess)
    if guess==answers[ques_num]:
        print("Correct")
        score+=1
    else:
        print("Incorrect")
        print(f"{answers[ques_num]} is correct ans")
    ques_num +=1
print("--------------------------------------------------------------")
print("Results")
print("guesses",end="")
print(guesses)
print("Answers",end="")
print(answers)
score=score/len(questions)*100
print(f"Your score is:{score}%")
