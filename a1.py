# Assignment 1
# Name: Taha Yar Khan
# Student ID: 501150770
#I recently started working out properly at the gym and I always noticed how I would write how much I was lifting in my notes app in my phone every workout session
#I would even often forget to add or change the weight in my phone which I would manually do by typing it in.
#This program helps to track your progress at the gym by storing the weight you lift for a particular exercise that you do each workout session automatically.
#It also helps you progressively overload your choice of exercise, which helps to make sure that you're actually progressing and gaining muscle.

#(LEARNING OBJECTIVE 5)
def progress():
    #This function is called progress and it is used for progressively overloading the chosen exercise by the user.
    new_weight=0+increase
    return new_weight
    #It increases the current weight that they are lifting for a given amount of sets and reps for an exercise by a certain amount of weight called "increase"
    #increase is going to be a variable in which it will ask the user to input the amount of weight they want to increase by for progressive overload.

# main block
if __name__ == "__main__":
    
    exercises=["bench press", "deadlift", "squat", "shoulder press", "bicep curls", "tricep extensions", "hammer curls", "barbell rows"]
    #This exercises list is a list of all the exercises that the user can choose from.
    
    #(LEARNING OBJECTIVE 4)
    for i in range(len(exercises)):
        print(i+1,")", exercises[i])
    #This for loop goes through the values inside the list called exercises and prints out all of them one by one.
    #It also prints them out with an ordered number next to it.
    #the i+1 part ensures the first value at the 0 index in the list is not 0) and also increases as we go further along the list.

    exercise=str(input("Enter the exercise you're doing: "))
    #The exercise variable is the input from the user of any of the exercise they want to chose from the options that will show up for them from the exercises list.
    exercise=exercise.lower()
    #The .lower() helps to automatically convert the users input of exercise to all lowercase incase they enter Bicep Curls instead of bicep curls for ex.
    
    #(LEARNING OBJECTIVE 1 & LEARNING OBJECTIVE 3)
    if exercise not in exercises:
        #This if statment checks if the string value for exercise is not inisde the list exercises.
        #It compares the string value of exercise with the string values inside the string values inside the exercises list.
        print("Error, please only enter the exercises mentioned above.")
        #If it is not it prints out an error message telling the user that the value that they have entered is not valid and not inside the list
    
    else:
        #However if the string value from the user input (exercise) is inside the list exercises it will run the code below:
        sets=int(input("Enter the number of sets: "))
        reps=int(input("Enter the number of reps: "))
        weight=int(input("Enter the weight for that exercise (in lbs): "))
        #These are more user inputs to aquire the number of sets, reps and weight that they are doing for the exercise that they have chosen.
        weekly_progress=[]
        #weekly_progress is an empty list in which we will add the weights that the user lifts for their exercise.
        #This will allow the user to track his progress and keep record of how much they're lifting.
        
        print("")
        print("You are currently doing: ")
        print(exercise)
        print("sets:"+str(sets))
        print("reps:"+str(reps))
        print("weight:"+str(weight) +"lbs")
        print("")
        #These lines of code just print out all the user inputs and shows it to them.
        
        increase=int(input("How much weight do you want to progress by (in lbs)?: "))
        #The increase variable is the users input of how much weight they want to progressively overload the exercise by.
        
        new_weight=weight
        #The variable new_weight needs to have a starting value which will be the weight that the user is currently lifting which will be inputed by themselves.
        
        #(LEARNING OBJECTIVE 2)
        run = True
        #We are assigning a variable called run with the boolean value True so that we can use it to run our while loop.
        #This while loop will keep running until run=False so that the user is able to keep adding weight values to the empty weekly_progress list.
        #That way the user can track his progress and see what they were lifting each workout session.

        #(LEARNING OBJECTIVE 4)
        while run:
            #This while loop runs if run is equal to True. 
            statement=input("did you complete all sets and reps for given weight? Or to quit program type 'quit': ")
            #statement variable asks the user whether they have done all the sets and reps for their exercise for the current weight that they're doing.
            
            #(LEARNING OBJECTIVE 1, LEARNING OBJECTIVE 2 & LEARNING OBJECTIVE 3)
            if statement == "quit":
                run = False
                break 
            #The loop stops if the user inputs quit. If the user inputs quit then the value for run is equal to False and the loop breaks. 
            #This would exit the user out of the loop.
            
            #(LEARNING OBJECTIVE 1 & LEARNING OBJECTIVE 3)
            if statement=="yes":
                #If the user has finished the sets and reps for their exercise for the current weight that they're doing then they'll input "yes"
                new_weight+=progress()
                #If the input from the user is "yes" then we will use the progress() function that we made to progressively overload the exercise.
                #This will update the the value for the new_weight variable as we are incrementing the value for it.
                weekly_progress.append(new_weight)
                #This updated value of new_weight will be added to the weekly_progress list 
                print("Great! Keep it up! Now do " + str(new_weight) + " lbs.")
                #motivating message being printed out.
                print(weekly_progress)
                #The user can track his progress and not forget how much weight he's lifting as the updated list will be printed out.
            
            #(LEARNING OBJECTIVE 1 & LEARNING OBJECTIVE 3)
            if statement=="no": 
                #If the user inputs "no" which would mean they have not completed the sets and reps for that weight for that exercise then it will not change the weight.
                #This is to prevent the user from getting injured.
                weekly_progress.append(new_weight)
                #The .append() adds the weight to the weekly_progress list to keep record of it 
                #It will also show the user how long they've been lifting the same weight for.
                print("It's alright!Keep doing " + str(new_weight) + " lbs.")
                #Instead it tells the user to keep doing the same weight for the same number of sets and reps.
                print(weekly_progress)
                #Again, the user can track his progress and not forget how much weight he's lifting as the updated list will be printed out.
                
                #Also if the user accidentally enters something other than "yes", "no" or "quit" then the program will keep running and not do any action.
                
        print(weekly_progress)
        print("Continue from", str(weekly_progress[-1]), "lbs next time.")
       #If the user inputs "quit" for statement and wants to quit the program then they will exit the while loop. 
       #This last line of code will then print out the list of all weights the user has lifted every workout session.
       #Incase the user wants to use the program again then they will know where they left off and can continue from the last weight they lifted.
    
