import re
import sys

#Functions to calculate/get student initials, student grade, gpa grade
def check_username(username):
    # checking if there are only letters
    if not re.match("^[a-zA-Z\s]+$", username):
        return False
    
    # checking if there are at least 2 words
    palavras = username.split()
    if len(palavras) < 2:
        return False
    
    return True

def student_initials(fullname):
  initials = ""
  for name in name_list:
    initials += name[0].upper()
  return initials

def student_grade(scoreavg):
  if scoreavg >= 85:
    return 'A'
  elif scoreavg >= 70:
    return 'B'
  elif scoreavg >= 55:
    return 'C'
  elif scoreavg >= 40:
    return 'D'
  else: return 'F'

def gpa_grade(overallgrade):
  grades = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.00,
        'F': 0.00
    }
  
  if overallgrade in grades:
    return grades[overallgrade]

def calc_score_avg (score1, score2, score3):
   return round(((score1 + score2 + score3)/3), 2)

#Score Average calc
#score_avg = round(((float_score_1 + float_score_2 + float_score_3)/3), 2)

#Inputs
user_name = input("Please insert your full name:")
score_1 = input("Please insert your first score (out of 100):")
score_2 = input("Please insert your second score (out of 100):")
score_3 = input("Please insert your third score (out of 100):")
attendance_percentage = input("Please insert your attendance percentage (out of 100):")

#Checking user input and converting to float

if check_username(user_name):
    pass
else:
    print("Invalid username!")
    sys.exit(1)

try:
    float_score_1, float_score_2, float_score_3 = map(float, [score_1, score_2, score_3])
except ValueError:
    print("Input is not a valid score")
    exit()

# Checking if they're all floats
if not all(isinstance(num, float) for num in [float_score_1, float_score_2, float_score_3]):
    print("Input is not a valid score")
    exit()

# Checking if they are less than 100 and greater than 0
if not all(num < 100 for num in [float_score_1, float_score_2, float_score_3]):
    print("Input is not a valid score")
    exit()

#variables/measures
name_list = user_name.split()
second_name = name_list[1]
second_name = second_name.capitalize()
score_avg = calc_score_avg (float_score_1, float_score_2, float_score_3)


#Output
print("\n")
overall_grade = student_grade(score_avg)
initials = student_initials(fullname=user_name)
gpa = gpa_grade(overall_grade)
print("Your average exam score was " + str(score_avg))
print("Student initials: " + initials)
print("Student second name: " + second_name)
print('Student overall grade: ' + overall_grade) 
print("Student GPA: " + str(gpa))


#Thanks a million :)