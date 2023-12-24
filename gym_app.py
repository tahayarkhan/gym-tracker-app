import sqlite3 


def insert_exercises_data(cursor, exercise_data):
    cursor.execute('''
        INSERT INTO exercises (name,sets,reps,weight,increase)
        VALUES(?,?,?,?,?)    
    ''', exercise_data)


def make_progress_table(cursor, exercise_name):

    exercise_name = exercise_name.replace(" ", "_").lower()

    cursor.execute(f'''
    
    CREATE TABLE IF NOT EXISTS {exercise_name} (
        id INTEGER PRIMARY KEY,
        month INTEGER,
        day INTEGER,
        year INTEGER,
        weight INTEGER
    );

    ''')

def insert_progress_data(cursor, exercise_name, progress_data):

    exercise_name = exercise_name.replace(" ", "_").lower()

    cursor.execute(f'''
        INSERT INTO {exercise_name} (month, day, year, weight)
        VALUES(?,?,?,?)    
    ''', progress_data)


def print_table(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")

    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    print("\t".join(columns))

    for row in rows:
        print("\t".join(map(str, row)))
        


def progress(old,increase):
    new = old + increase
    return new
    


# main block
if __name__ == "__main__":

   
    
    conn = sqlite3.connect("gym_app.db")
    cursor = conn.cursor()

    cursor.execute('''
    
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY,
        name TEXT,
        sets INTEGER,
        reps INTEGER,
        weight INTEGER,
        increase INTEGER
    );

    ''')

    exercises=["bench press", "deadlift", "squat", "shoulder press", "bicep curls", "tricep extensions", "hammer curls", "barbell rows"]
  
    for i in range(len(exercises)):
        print(i+1,")", exercises[i])
   
    exercise = str(input("Enter the exercise you're doing: ")).lower()


    if exercise not in exercises:
       
        print("Error, please only enter the exercises mentioned above.")


    else:
        
        sets=int(input("Enter the number of sets: "))
        reps=int(input("Enter the number of reps: "))
        weight=int(input("Enter the weight for that exercise (in lbs): "))
        weekly_progress=[]
        
        print("")
        print("You are currently doing: ")
        print(exercise)
        print("sets:"+str(sets))
        print("reps:"+str(reps))
        print("weight:"+str(weight) +"lbs")
        print("")
        
        increase = int(input("How much weight do you want to progress by (in lbs)?: "))
        
        exercise_data = (exercise, sets, reps, weight, increase)


        insert_exercises_data(cursor, exercise_data)
        make_progress_table(cursor, exercise)



        last_weight = weight
        
        run = True

        while run:
            
            months = ["january" , "february" , "march" , "april", "may" , "june" , "july" , "august", "september" , "october" , "november" , "december"]
            month = input("Enter the month today: ").lower()
            
            for i in range(len(months)-1):
                if months[i] == month:
                    month = i + 1
            
            day = input("Enter the day of the month today: ")
            year = input("Enter the year: ")

            statement = input("did you complete all sets and reps for given weight today? Or to quit program type 'quit': ")
            
            
            if statement == "quit":
                run = False
                break 
            
            if statement=="yes":
                
                new_weight = progress(last_weight, increase)
                weekly_progress.append(new_weight)
                print("Great! Keep it up! Now do " + str(new_weight) + " lbs.")
                print(weekly_progress)
                last_weight = new_weight
            
            
            if statement=="no": 
                weekly_progress.append(last_weight)
                print("It's alright!Keep doing " + str(last_weight) + " lbs.")
                print(weekly_progress)

            progress_data = (month,day,year,last_weight)
            insert_progress_data(cursor,exercise,progress_data)
                


        print(weekly_progress)
        print("Continue from", str(weekly_progress[-1]), "lbs next time.")

   
    conn.commit()
    conn.close()

            
