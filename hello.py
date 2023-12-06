import sys, statistics, cowsay, requests,json

response = requests.get('https://itunes.apple.com/search?entity=song&limit=20&term='+ sys.argv[1])
#print (json.dumps(response.json(), indent=2)) #to use json.dumps you have to import json
object_returned= response.json() #with json.dumps you get a string and with this approach, without using json.dumps, you geta dictionary

for result in object_returned["results"]:
    print('The name of the song is:' + result['trackName'])

if len(sys.argv)==4:
    cowsay.turkey('Hello, ' + sys.argv[1])
    cowsay.trex('Hello, ' + sys.argv[2])
    cowsay.cow('Hello, ' + sys.argv[3])

if len(sys.argv) <2:
    sys.exit('Too few arguments')

for arg in sys.argv[1:]: #here I an slicing from the first argument
    
    print ('Hello, my name is ', arg)

print( "The mean of 6,4 and 2 is: ", statistics.mean([6,4,2]))
while True:
    user_input= input("Please enter an integer\n")
    try:
        x=int(user_input)
    except ValueError:
        print(f'{user_input} is not a valid integer')
    else:
        break

print(f"You have entered {user_input}")

name= input("Enter the name of a Harry Potter character to find which house they were in: ")    

match name:
    case "Harry" | "Ron" | "Ginny" | "Hermione":
        print("Gryffindor")
    case "Luna" | "Cho" | "Cedric":
        print("Ravenclaw")
    case "Draco" | "Crab" | "Goil":
        print("Slitherin")
    case _:
        print("The character you have entered is not in any of the houses")

def main():
    number= get_number()
    meow(number)

def get_number():
    while True:
        n= int(input("Enter a number\n"))
        if n >0:
            return n
    


def meow(n):
    for _ in range(n):
        print("System executed successfully!!")

main()

students= ["Harry", "Ron", "Hermione", "Luna", "Ginny"]

for i in students:
    print(i)

hogwarts= {
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Luna": "Ravenclaw",
    "Draco":"Slytherin"

}

kee= input(" Enter the name of the student\n").capitalize()

print(f"{kee} is in {hogwarts[kee]}")

wizadryschool= [
    {'name': "Harry", 'house':'Gryffindor', 'patronus':'Stag'},
    {'name': 'Hermione', 'house':'Gryffindor', 'patronus': 'Otter'} ,
    {'name': 'Ron', 'house':'Gryffindor', 'patronus': 'Jack Russel Terrier'},
    {'name': 'Snape', 'house':'Slytherin', 'patronus':'Doe'}
]

for person in wizadryschool:
    print (person['name'], person['house'], person['patronus'], sep='- ')

for i in range(3):
    for j in range(3):
        print ('#' , end='')
    print()

