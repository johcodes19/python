'''

title=('conversion of kilograms to pounds\n')
print(title.upper())

a=input('Enter kgs you want to convert\n')
b =float(a)*2.2046

print( str(a)+ ' kgs =  '  +str(b) +' pounds\n\n')

#circumfrence of a circle
title=('\ncalculating circumfrence of a circle')
print(title.upper())

r= input('Enter radius of your circle\n')
pi=float(3.14)

c=2*pi*float(r)
print(c)
print('\n\n')

#math magic
print('MATH MAGIC')
print(' ')
a=input('enter a number\n')
print('Your number multiplied by three is ')

b=int(a)*3
print(b)

print('\n your number times three plus six is ')

c=int(b)+int(6)
print(c)

print('The above output divided by three is')

d=int(c)/int(3)
print(d)

print('The above answer minus your number')
print('final number will always be')

print(d-int(a))
print(' ')
print('\n\n')


#quiz game
print('QUIZ GAME')

prompt=input('Do you want to play the game?\n')


if prompt.lower() == 'yes':
	name=input('Enter your name  ')
	print('\nWelcome to the game  ' +   name)
	
else:
	quit()
	
score=0
		
print('\nQuestion' +str(1))
print('What does CPU stand for?\n')
answer=input('')

if answer.lower()== 'central processing unit':
	print('correct')
	score+=1
	
else:
	print('incorrect')

print('\nQuestion' +str(2))
print('What does GPU stand for?\n')
answer=input('')

if answer.lower()== 'graphics processing unit':
	print('correct')
	score+=1
	
else:
	print('incorrect')

print('\nQuestion' +str(3))
print('What does RAM stand for?\n')
answer=input('')

if answer.lower()== 'random access memory':
	print('correct')
	score+=1
	
else:
	print('incorrect')

print('\nQuestion' +str(1))
print('What does ROM stand for?\n')
answer=input('')

if answer.lower()== 'read on memory':
	print('correct')
	score+=1
	
else:
	print('incorrect')

print(' ')
print(name + ' you got ' +str(score) +' out of ' +str(4) + ' questions correctly\n')

print('You have ' + str(score/4 *100) +'%\n')
print('\n\n')



#tip calculator
print('TIP CALCULATOR#')
price=input('Enter the price you were charged\n')
price=int(price)
print(' ')

percentage=input('Enter the percentage you want to tip\n')
percentage=int(percentage)
print(' ')

tip=round(price*percentage/100 ,2)
print('The amount you will give as tip is')
print(tip)
print(' ')
print('\n\n')


#car insurance

print('CAR INSURANCE\n')

gender=input('Enter your gender\n')

if gender.lower()=='male':
	age=input('Enter your age in numbers\n')
	age=int(age)
	if age <= 26:
		print('You will pay 26%')
	else:
		print('You will pay 9%')
		
elif gender=='female':
	car=input('Do you drive a sports car?\n')
	if car=='yes':
		print('You will pay 21%')
	else:
		print('You will pay 16%')
		
else:
		print('Prices not available at the moment\n')
print('\n\n')		
'''

#math game
import random

print('MATH GAME')

a=random.randint(1,10)
b=random.randint(1,10)
c=int(a)*int(b)


answer=input(  f'{a} x {b} =\n'   )
print(' ')
answer=int(answer)

if answer==int(c):
	print('correct')
else:
	print('incorrect')
	print(f'Ans:  {c} ')
	
print(' ')
print('\n\n')
	
#rock paper scissors
import random

print('ROCK PAPER SCISSORS')

print(' 1 = rock')
print('2 = paper')
print('3 = scissors')

comp=random.randint(1,3)
comp=int(comp) 


    
num=input('Enter your number\n')
num=int(num)

if num ==1:
	print('You chose: ROCK')

elif num==2:
	print('You chose: PAPER')

elif num==3:
	print('You chose: SCISSORS')

else:
	print('invalid input')
	quit()


if comp==1:
    	print('Computer chose : ROCK')
elif comp==2:
    	print('Computer chose : PAPER')
elif comp==3:
    	print('Computer chose : SCISSORS')
    	
    	
if comp==num:
	print('\nits a DRAW')
	
elif comp==1 and num==2:
	print('YOU WIN')
	
elif comp==2 and num==1:
	print('YOU LOOSE')
	
elif comp==2 and num==3:
	print('YOU WIN')
	
elif comp==3 and num==2:
	print('YOU LOOSE')
	
elif comp==3 and num==1:
	print('YOU WIN')
	
elif comp==1 and num==3:
	print('YOU LOOSE')
	
print(' ')
print('\n\n')


#word jumble

import random

print('WORD JUMBLE')
list=['programming','resistance','fiction','condition','reverse','computer','python'  ]
word= random.choice(list)

sampled=' '.join(random.sample(word,len(word)) )


print(sampled.upper())

guess=input('\nguess the word\n')

if guess.lower()==word:
	print('YOU WIN')
	
else:
	print('YOU LOST')
	print('The word is:   '+ word)
	
print(' ')
print('\n\n')


#hangman game
import random

print('HANGMAN GAME\n')

list=['programming','resistance','fiction','condition','reverse','crush','exhaust','trouble','stimulate','vivid','stoist','random','character','paper','onoin','computer','python', 'father','chaos'  ]

word=' '.join(random.choice(list))
word=word.upper()

lives=10
guesses=' '

while lives>0:
	
	print('You have '+str(lives) +' lives       remaining\n\n')
	guessed_all=True
	
	for char in word:
		if char in guesses:
			print(char, end=' ')
			
		else:
			print('-', end=' ')
			guessed_all=False
			
	print()
	
	if not guessed_all:
		
		guess=input('\nGuess the letters:  ')
		guess=guess.upper()
		guesses+=guess
		if guess not in word:
			lives -= 1
			if lives < 1 :
				print('\nYOU LOSE. GAME OVER')
				print(f'The word is {word}')
				quit()
		else:
			lives=lives
	
	else:
	     
	    print('\n\nYOU WON')
	    quit()

print('\n\n')


#CAESAR CIPHER

print('CAESER CIPHER')

def encrypt_char(char,key):
	sum=(ord(char)+key)
	if sum>90:
		sum-=25
	letter=chr(sum)
	print(letter)
	


def encrypt_msg(message):
	for char in message:
		letters=char.upper()
		encrypt_char(letters,4)
		
	
encrypt_msg('I love you')
print()
print()

def decrypt_char(char,key):
	
	sum=(ord(char)-key)
	if sum<65:
		sum+=4
	letter=chr(sum)
	print(letter)
	

def decrypt_msg(message):
	for char in message:
		letters=char.upper()
		decrypt_char(letters,4)

decrypt_msg('hyivfgdfy')

print('\n\n')


#GUESS THE CAPITAL 
import random
print('GUESS THE CAPITAL CITY')

dict={
'country':'capital',
'France': 'Paris',
'Finland' : 'Helsinki',
'Japan' : 'Tokyo',
'India' : 'Mumbai',
'Kenya' : 'Nairobi'
}

len=(len(dict))
num=0 

while len >0:
	len-=1
	array=list(dict.keys())
	num+=1
	print(num)
	random=array[num]
	
	print('You have 3 guesses remaining')
	guess=input(f'Guess the capital City of {random}  ')
	
	guess=guess.upper()
	ans=dict[random]
	ans=ans.upper()
	
	guessed=True
	guesses=3
	
	if guess==ans:
		print()
		print('You Got it')
		print()

	else:
		guessed=False
		
		while not guessed and guesses>0:
			print()
			guesses-=1
			print(f'You have {guesses} guesses remaining')
			guess=input('Thats not right. Try again    ')
			guess=guess.upper()
			
			if guesses<1:
				print('You are out of guesses')
				print(f'The answer is {ans}')
				
			if guess==ans:
				print()
				print('You Got it')
				exit()
print()
print()
		
		
'''		
		
#frequecy count
print('Frequency counter')
print()
text= input('Enter a line of text    ')

count={ }

for letter in text:
	count[letter]=count.get(letter,0)+1
	#print(letter ,count[letter])
	
for key ,value in count.items():
		print(key,value)
		print()
		print()
		

'''
#tower of hanoi
print('TOWER OF HANOI')
towers=[ [ 3,2,1],[],[] ]
print()



def move( ):

	one=towers[0]
	two=towers[1]
	three=towers[2]
	
	print(one,two,three)
	print()
	'''
	poped=one.pop()
	two.append(poped)
	poped=one.pop()
	two.append(poped)
	
	print(one,two,three)
	print()
	
	poped=one.pop()
	three.append(poped)
	
	print(one,two,three)
	print()
	
	clear=two.pop()
	three.append(clear)
	clear=two.pop()
	three.append(clear)
	print(one,two,three)'''
	
move()

def solve_tower(towers,n,start_tower,dest_tower,aux_tower):
	move()
	if n<=1:
		return n
	n=solve_tower(n-1)+solve_tower(n-2)
	print(n)
	
solve_tower(towers,3,towers[0],towers[1],towers[2])
	

	