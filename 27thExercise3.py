# Create a program capable of displaying questions to user like KBC
# Use lise data type to store the questions and their correct answer.
# Display the final amount the person is taking home after playing the game. 

questions =[
    #Q_1
    ["A process is a _______.","single thread of execution","program in the execution",
     "program in the execution","task",2],
    #Q_2
    ["The word processing feature that catches most random typographical errors and misspellings is known as _____.",
     "Grammar checker","Spell checker","Word checker","Word checker",2],
    #Q_3
    [" What is smallest unit of the information?",
     "A bit","A byte","A block","A nibble",1],
    #Q_4
    ["What is the decimal equivalent of the binary number 10111?",
     "21","39","42","23",4],
    #Q_5
    ["What is the term for a temporary storage area that compensates for differences in data rate and data flow between devices?",
     "Buffer","Bus","Channel","Modem",1],
    #Q_6
    ["How many color dots make up one color pixel on a screen?",
     "265","16","8","3",4],
    #Q_7
    ["Which of the following values is the correct value of this hexadecimal code 1F.01B?",
     "35.0065918","32.0065918","31.0065918","30.0065918",3],
    #Q_8
    ["How is the data stored on the diskette?",
     "Ink","Laser bubbles","Magnetism","Circuits",3],
    #Q_9
    ["Which of the following is the smallest visual element on a video monitor?",
     "Character","Pixel","Byte","Bit",2],
    #Q_10
    ["Which of the following natural element is the primary element in computer chips?",
     "Silicon","Carbon","Iron","Uranium",1],
    #Q_11
    [" Which of the following programs enables you to calculate numbers related to rows and columns?",
     "Window program","Spreadsheet program","Graphics program","Word program",2],
    #Q_12
    ["Which of the following is a structured programming technique that graphically represents the detailed steps required to solve a program?",
     "Object-oriented programming","Pseudocode","Flowchart","Top-down design",3],
    #Q_13
    ["Which of the following values is the correct value of this hexadecimal code ABCDEF?",
     "11259375","11259379","11259312","11257593",3],
    #Q_14
    ["Which of the following is an output device?",
     "Keyboard","Mouse","Light pen","VDU",4],
    #Q_15
    ["Which of the following is an input device?",
     "Plotter","Printer","VDU","Mouse",4]
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"Ques{i+1}:",questions[i][0])
    print(f"a.{questions[i][1]}            b.{questions[i][2]}")
    print(f"c.{questions[i][3]}            b.{questions[i][4]}")
    reply=int(input("\nEnter your answer(1-4): "))
    if(reply==question[-1]):
        print(f"Correct answer,You have won Rs.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
            print("Now you are a KororPoti.")
    else:
        print("Wrong answer!")
        break
    
print(f"Your take home money is {money}")