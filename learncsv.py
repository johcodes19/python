with open('students.csv') as file:
    for line in file:
        # line = line.rstrip().split(',')
        # print(f"{line[0]} is in{line[1]}.")
        name, house= line.rstrip().split(',')
        print(f"{name} is in{house}.")

print("\n")
#reading the csv while sorting it

students= []
with open('students.csv') as file:
    for line in file:
        name, house= line.rstrip().split(',')
        students.append(f'{name} is in{house}')

for student in sorted(students):
    print(student)

print('\n')

#another way of reading the file while sorting it.
hogwarts_students= []
with open('students.csv') as file:
    for line in file:
        name, house= line.rstrip().split(',')
        # student= {}
        # student['name']= name
        # student['house']= house
        student= {'name': name, 'house': house}
        hogwarts_students.append(student)

# def get_house(student):
#     return student['house'] #in this function we are getting the house of each student so we can sort it below

# for student in sorted(hogwarts_students, key=get_house):
#     print(f"{student['name']} is in {student['house']}")

#instead of using the get_house function, you can use an anonymous function like lambda
for student in sorted(hogwarts_students, key=lambda student: student['house']):
    print(f"{student['name']} is in {student['house']}")


print('\n')
#now using the module of csv reader. It is better to use, especially when you have characters in files which for example, have gramatical comas like, Harry, "Number four, Privet Drive"

import csv

hogwart_students= []

with open('students.csv') as file:
    reader = csv.reader(file)

    for name, house in reader:
        hogwart_students.append({"name": name, "house": house})

for student in sorted(hogwart_students, key=lambda student: student['name']):
    print(f"{student['name']} is in {student['house']}")

print('\n')

#writing in csv files. we will prompt the user to provide the name and home of the characters
name= input("What is the name of the character?\n")
home= input('What is the home of the character?\n')

with open('students.csv', 'a') as file:
    # writer = csv.writer(file)
    # writer.writerow({name, home})

    #using a dictionary writer 
    writer= csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})