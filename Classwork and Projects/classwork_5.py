# Classwork_5.p
# This file contains the "starter code" for Classwork 5
# You must complete all three parts of the assignment


"""
Part 1: User input.
The objective of this part is to use a "while" loop to control user input.
You will ask a user to input a test score, which is to be an integer. But starting now, you will check for errors.
You will use the built-in Python method "isdigit()" to determine if the user has actually input an integer.
As long as the user has not entered an integer, you must disregard the input and ask the user to try again


"""


def get_user_input():
   score = ???  # ask the user to input a test score, which must be an integer
   while not(score.isdigit()):   # score.isdigit() = True if score is an integer; False otherwise
       print (???) # print out an error message telling the user that the entry was NOT an integer
       score = ??? # ask the user to re-enter a score
   return ???  # you want to return the score


if __name__ == "__main__":
   # There are 35 students in the class. You have to call the function get_user_input() 35 times to get all the scores
   for i in range(0,35):
       s = get_user_input()
       print ("Score: ", i, " is ", s)


"""
Part 2: infinite loops
The following code contains an infinite loop. Your task is to rewrite
this code so it does NOT contain an infinite loop. The loop must run exactly 100 times.
Note: you MAY NOT change the while loop into a for loop.
"""
sum == 0
i == 0
while (i%2)**3 != 1:
   sum += i
   i += 4
print ("The answer is ", sum)






"""
Part 3: Sentinel loops


A sentinel while loop is a loop that runs until a certain value - called a sentinel - is
encountered.  In this case, the sentinel can be EITHER an uppercase "Q" OR a lowercase "q".
Your task is to write a sentinel while loop that asks the user to input a student's name.
The loop should run until the sentinel is encountered. That is, it should stop when the user
types either a "Q" or a "q".  Hint: this would be a really good place to use either the
built-in string method .upper()  or .lower()


"""


#first prompt the user for the first student's name.
# remember to tell the user that entering 'Q' or 'q' as the name will end the program.
student_name = input(???)
while (???):  # check to see if the user has entered the sentinal value. If not, print the name.
   print(student_name)
   #now, prompt for the next student_name. Remind the user how to end the program
print ("Thank you for using this program.")

