import time



questions = ["1. How many elements are in the Periodic table?", "2. Which of the following animals has the largest egg?",
             "3. What is the hottest planet in the Solar System?", "4. What does IP stand for?", "5. Teheran is the capital of which country that is listed below? "]

choices = [["A. 117\nB. 118\nC. 119\nD. 120\n"], ["A. Whale\nB. Parrot\nC. Ostrich\nD. Eagle\n"], ["A. Mercury\nB. Earth\nC. Neptune\nD. Venus\n"],
           ["A. Internet Protocol\nB. Intranet Protocol\nC. Initiation Protocol\nD. Inductive Protocol\n"], ["A. Iraq\nB. Iran\nC. Saudi Arabia\nD. Qatar\n"]]

answers = ["B", "C", "D", "A", "B"] 

while True:
   score = 0
   print("---------------------------------------------------------------")
   start = input("Welcome to the quiz! Press S to start! ")

   if start.upper() == "S":
       print("---------------------------------------------------------------")

       for i, z, k in zip(questions, choices, answers):
            for j in z:

                 print(i)
                 print(j, end="")
                 choice = input("Enter your answer(A, B, C or D): ")
                 if choice.upper() == k:
                     print("That's correct!")
                     score+=1
                 else:
                     print("Incorrect!")
                 print("---------------------------------------------------------------")


       print("---------------------------------------------------------------")
       print("The quiz has finished:")
       print("---------------------------------------------------------------")
       print(f"Your score: {(score / 5)*100:.2f}%")
       print("---------------------------------------------------------------")
       again = input("Type Y is you want to try again, or N to Quit: ")
       print("---------------------------------------------------------------")
       if again.upper() == "N":
            print("Thanks for playing!")
            break
       if again.upper() == "Y":
            print("Trying Again:")
            time.sleep(2)
   else:
       start = input("Wrong Input. Try again: ")










