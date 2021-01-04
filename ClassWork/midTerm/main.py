# James Hooper
# 12/3/2020
# Mid term test

#imports
import sys
from datetime import datetime

#functions
def open_file(file_name,mode):
    """ Open and returns a open file with the given permissions"""
    try:
        file = open("assets/testFiles/"+file_name,mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program. \n",e)
        try:
            file = open("assets/Errors/errors_log.txt","a+")
            time = datetime.now()
            error_time = time.strftime("%m/%d/%Y %H:%M:%S")
            file.write(str(e)+" "+str(error_time)+"\n")
            input("\n\nPress the Enter key to exit.")
            sys.exit()
            
        except:
            sys.exit()
    else:
        return file


def next_line(file):
    try:
        line = file.readline()
        line = line.replace("/","\n")
        return line
    except:
        print("Could not read line")
        input("\n\nPress the Enter key to exit.")
        sys.exit()


def next_question(file):
    """Return the next question block of data from the test"""
    category = next_line(file)
    question = next_line(file)
    answers = []
    for i in range(4):
        answers.append(next_line(file))
    correct = next_line(file)
    if correct:
        correct = correct[0]

    explanation = next_line(file)

    return category, question, answers, correct, explanation
        

def get_name():
    """Gets name of the user"""
    try:
        time = datetime.now()
        test_time = time.strftime("%m/%d %H:%M")
        while True:
            name = input("What is your first and last name? ")

            if len(name) >= 2 and " " in name:
                name = name.title()
                return name,test_time
            else:
                print("this is not a valid name")
    except:
        print("something went wrong while getting the name")

    
def welcome(title,name,test_time):
    """Welcome the user"""
    print("Welcome "+name+" to your Mid Term\n")
    print("your tester is"+str(title))


def create_report_card(name,score,total_questions,test_time):
    """Creates the Report Card"""
    try:
        card = open("assets/Scores/"+name+".txt","w")
        card.write("name ="+name+"\n")
        card.write("Time taken = "+test_time+"\n")
        card.write("Number Correct = "+str(score)+"\n")
        try:
            percentage = score/total_questions*100
            print(percentage)
        except:
            percentage = 0
        card.write("% Correct = "+str(percentage)+"\n")
        if percentage >= 90:
            card.write("Letter Grade = A")
        elif percentage >= 80 and percentage < 90:
            card.write("Letter Grade = B")
        elif percentage >= 70 and percentage < 80:
            card.write("Letter Grade = C")
        elif percentage >= 60 and percentage < 70:
            card.write("Letter Grade = D")
        else:
            card.write("Letter Grade = F")
        card.close()
    except:
        print("something went wrong while creating the report")
        
def main():
    ######################################################################################################################
    file = open_file("Erin_Broadbents_Python_midterm_test.txt","r")# will need to change file name to match the test that your taking
    ######################################################################################################################
    title = next_line(file)
    name, test_time = get_name()
    welcome(title,name,test_time)
    score = 0
    total_questions = 0
    category, question, answers, correct, explanation = next_question(file)
    while category:
        total_questions += 1
        print(category)
        print(question)
        for i in range(len(answers)):
            print(str.format("\t{}:  {}",i+1,answers[i]))
        #get answer
        answer = input("what is your answer? ")
        #check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += 1
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("score:", score, "\n\n")
        # get the next question block
        category, question, answers, correct, explanation = next_question(file)
    file.close()
    print("That was the last question!")
    print("You're final score is", score)
    create_report_card(name,score,total_questions,test_time)
##    for i in range(20):
##        x = next_line(file)
##        print(x)



main()
