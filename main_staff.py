#Function
from typing import List


def raise_to_3(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

#Arrays inside array
test_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
#print(test_array[1][2]) first "[]" to choose inside array second "[]" to choose column

#functions of list
Cities = ["Madrid", "Milan", "London", "Chicago"]
Cities.append("Lviv")
Cities.remove("Lviv")
Cities.insert(0, "Odessa")
Cities.sort()
Cities.reverse()
#print(Cities.index("Odessa")) to check if smth is in the list

#Tuple
Data = ("Nikita", "Dima")
#print(Data) Tupels = store information that doesnt need to be changed

'''
Basic calculator
num1 = float(input("Enter first number"))
op = input("Enter operator")
num2 = float(input("Enter second number"))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Error")
'''
#Dictionary
Monthes = {
    "Mar": "March",
    "Dec": "December",
    "Jan": "January",
}
#print(Monthes.get("Mar"))

#While
'''
i = 1
while i <10:
    print(i)
    i += 1
print("Done")
'''

#For
#for letter in "Nikita":
    #print(letter)

#Translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AOUIEaioue":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
#print(translate(input("Enter a phrase:")))

#Try/Except
'''
try:
    value = 10 / 0
    number = int(input("Enter a number:"))
    print(number)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Devided by zero")
'''

#Reading files
#open("name of the file", "r - read/ w - write and create new file/ a - append/ r+ - reand and write")
'''
employee_file = open("Employees.txt", "a")
print(employee_file.readable())
employee_file.write("\nToby - Driver")

#print(employee_file.read())
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
'''

#Class
from Students import Student
Student1 = Student("Jack", "Business", 3.1, True)

#Multiple choice quiz
from Question import Question
question_prompts = [
    "What color are apples?\n(a) Red\n(b) Yellow\n(c) Orange\n\n",
    "What color are bananas?\n(a) Purple\n(b) Pink\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Magenta\n(b) Blue\n(c) Red\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c")

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)