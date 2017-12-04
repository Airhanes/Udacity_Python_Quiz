#these are my questions and answers 
easy_questions= ["What is 20 + 2?__1__", "What is the capital of Georgia?__2__","If john has $4 and buys a candy bar for $3.50, how much money does he have left over?__3__","What is the name of the NBA basketball team in Georgia?__4__","What is the name of the NFL team in Georgia?__5__","How many toys do I have if I sell 3, but had 8 toys originally?__6__","How many Bad Boy movies are there?__7__","How many Fast Furious movies are there?__8__","What is 10 * 5?__9__","What city does the UGA team play in?__10__"]

medium_questions= ["What is 20 * 2 ?__1__", "What is 100 * 2? __2__", "Who was the first Black President? __3__"," Who was the first president of the USA?__4__", "Where is Lebron James from (Hometown)?__5__", "1*1?__6__", "30*1000?__7__", "5 - 10?__8__","How many home alone movies are there?__9__","Who is the head coach of the Atlanta Falcoms?  ___10____"]

hard_questions= ["How many wheels do normal cars have?___1___","What city is disney world located in Florida? ___2___","What type of dog was Balto in the movie? ___3___", "Did the Rock ever play college football (yes or no)? ____4___", "how many best man movies are there? ____5____","What type of dog was lassie? ____6____", "100 + 100 ? ___7___", "40+40 ? ____8____", "What is the name of the team that Greg Popovich coaches? ___9___",  "What is the name of the football team in Atlanta? ____10____"]
easy_answers= ["22", "atlanta", ".50", "atlanta hawks", "atlanta falcons" ,"five", "two", "eight" , "50", "athens"]

medium_answers= ["40", "200", "barack obama","george washington","akron ohio","1","30000","-5","4","dan quin"]

hard_answers= ["4", "orlando", "husky", "yes","2","collie","200","80","Spurs","Atlanta Falcons"]
#this is my data dictionary
question_guide = {  "easy":{    "answers":easy_answers,    "questions": easy_questions  },  "medium":{    "answers":medium_answers,    "questions": medium_questions  },  "hard":{    "answers":hard_answers,    "questions": hard_questions  }}

questions = question_guide[level.lower()]["questions"]answers = question_guide[level.lower()]["answers"]score, num_answers = quiz(questions, answers)
#this will print out my welcome statement and ask you for your nameprint('Hello welcome to my Quiz, what is your name?')
#definied the variable username so that the user could type in their nameusersname = input()print ("")print('It is nice to meet you, ' + usersname)
print("")
#This is my level selectorlevel = ""while level.lower() not in ["easy", "medium", "hard"]:  level = input ('Please select a difficulty (easy, medium, or hard): ')
# I defined quiz using a for loop so that the questions in my data dictionary will#populate one at a time until there no more questions. # also I added the question numberingdef quiz(questions, answers):  score = 0  num_answers = None  for question_number, question in enumerate(questions):    print("{}) {}".format(question_number + 1, question))    answer = input("Please fill in the blank with your answer below:\n")    if answer.lower() == answers[question_number].lower():      score += 1  return score, len(answers)
print("Your score is {}/{}".format(score, num_answers)) #print score numerator over denomenator
