def Menu():
    choice = 0
    while(choice != 9):
        print("1.Adding a grade")
        print("2.Show the grades")
        print("3.Average of grades")
        print("9.Exiting the program")
        choice = int(input("Which one do you chose?"))
        if (choice == 1):
            Add()
        elif(choice == 2):
            Show()
        elif(choice == 3):
            Ave()
        else:
            print("Wrong choice please choose something from the list") 
            
def Add():
    grade = int(input("What grade do you want to be added?"))
    MathGrades.append(grade)
    print(MathGrades)

def Show():
    choiceS = 0
    while(choiceS != 9):
        print("1.Show Math grades")
        print("2.Show BEL grades")
        print("3.Show IT grades")
        choiceS = int(input("Which one do you chose?"))
        if (choiceS == 1):
           for x in range(0, len(MathGrades)):
             print(MathGrades[x], end=" ")
           print()
        elif (choiceS == 2):
           for x in range(0, len(BELGrades)):
             print(BELGrades[x], end=" ")
           print()
        elif (choiceS == 3):
           for x in range(0, len(ITGrades)):
             print(ITGrades[x], end=" ")
           print()
        else:
            print("Wrong choice please choose something from the list")



def Ave():
    average = 0
    choiceA = 0
    while(choiceA != 9):
     print("1.Average Math grade")
     print("2.Average BEL grade")
     print("3.Average IT grade")
     choiceA = int(input("Which one do you chose?"))
     if (choiceA == 1):
       for x in range(0, len(MathGrades)):
         average += MathGrades[x]
       average /= len(MathGrades)    
       print("Your average grade is:",average)
     elif (choiceA == 2):
       for x in range(0, len(BELGrades)):
         average += BELGrades[x]
       average /= len(BELGrades)    
       print("Your average grade is:",average)
     elif (choiceA == 3):
        for x in range(0, len(ITGrades)):
          average += ITGrades[x]
        average /= len(ITGrades)    
        print("Your average grade is:",average)
     else:
         print("Wrong choice please choose something from the list")


MathGrades = [5,2]
BELGrades = [4]
ITGrades = [2,5,6]
Menu()
    