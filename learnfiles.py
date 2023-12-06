name= input('What is your name? ')

# names= open('names.txt', 'a')
# names.write(f'{name}')
# names.close()

#writing mode 
with open('names.txt', 'a') as names:
    names.write(f'{name}\n')

#reading mode
with open('names.txt', 'r') as names:
    #reading all the lines in the file
    #     lines= names.readlines()

    # for line in lines:
    #     print('Hello,',  line.rstrip())# rstrip is for stripping off the \n from the lines
    for line in names:
        print('Hello,',  line.rstrip())

print('\n')
#another way of reading the file while sorting them.
nombres= []

with open('names.txt') as file:
    for line in file:
        nombres.append(line.strip())

for nombre in sorted(nombres):
    print(f"Hola, {nombre} 👋")

print('\n')
#you can also sort the file directly
with open('names.txt') as file:
    for line in sorted(file):
        print(f"Hi, ", line.rstrip(), " 😀")