name= input("What is the name of the character: ")    

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
        n= int(input("Enter a number"))
        if n >0:
            return n
    


def meow(n):
    for _ in range(n):
        print("System executed successfully!!")

#main()

students= ["Harry", "Ron", "Hermione", "Luna", "Ginny"]

for i in students:
    print(i)

hogwarts= {
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Luna": "Ravenclaw",
    "Draco":"Slytherin"

}

kee= input(" Enter the name of the student").capitalize()

print(f"{kee} is in {hogwarts[kee]}")

