#Theo B 2018
import random #including the library that will allow us to create random numbers 
#Step 1 : Reading the client's desired numbers
var = input('How many numbers do you want to insert ( 1-12 ) \n') #reads the amount of numbers the user will have to insert afterwards 
while (int(var)<1 or int(var)>12) :#checking if the number inserted is within the 1-12 range
	var = input('Wrong Value. Please insert a number from 1 to 12 \n')#number out of bounds case . Asks for another valid value
print(var);#prints the selected value of the client
numbers= [] #creating a numbers list 
#Step 2 Reading the numbers . 
for x in range(int(var)): #loop that occurs as many times as the value of var
	choice = input('Please insert a number from 1 to 80 \n') #reads a number from the user
	while int(choice)<1 or int(choice)>80  :#value checking loop
		choice = input('Invalid Entry . Please enter a number from 1 to 80 \n') #wrong value case
	numbers.append(int(choice)) #adds the user's number at the end of the list 
print("You chose: ")	
print(numbers) #prints out the choices of the user
#Step 3
multiplier=input('Please choose your multiplier ( 1,2,5,10 )  \n') #selecting the multiplier
while int(multiplier)!=1 and int(multiplier)!=2 and int(multiplier)!=5 and int(multiplier)!=10 : #value checking
	multiplier=input('Invalid Entry . Please enter a valid multiplier ( 1,2,5,10 )  \n')
#Step 4 
#highlighted numbers aka winning numbers 
highlight=[]
for i in range (20): #loop that creates the winning numbers 
	temp=random.randint(1,81) #creates a random number from 1 to 80 
	while temp in highlight: # checking if the number is unique
		temp=random.randint(1,81)	
	highlight.append(temp) #in this case the number is unique , so it is being added to the winning number list 
print("The 20 winning numbers are   : ")
print(highlight)	#printing out the winning numbers 
#Matching numbers , looking for how many numbers from the user's picks match the winning numbers 
success=0 # amount of matches
for x in highlight:
	if x in numbers: #comparing the 2 lists 
		success+= 1 # if they have a common value then the variable called success is increased by 1 
print("Amount of Matches: ")
print(success) #prints out the result 
#tuples of conferments
t = ((0, 2.5),(0, 1, 5),(0, 0, 2.5, 2.5), (0,0,1,4,100),(0,0,0,2,20,450),(0,0,0,1,7,50,1600),(0,0,0,1,3,20,100,5000),( 0,0,0,0,2,10,50,1000,1500),(0,0,0,0,1,5,25,200,4000,40000),(2,0,0,0,0,2,20,80,500,10000,100000),(2,0,0,0,0,1,10,50,250,1500,15000,500000), (4, 0, 0, 0, 0, 0, 5, 25, 150, 1000, 2500, 25000, 1000000))		
success_multiplier=t[int(var)][int(success)] #calculating the success multiplier 
prize=success_multiplier*multiplier # calculating how much the user won 
print("You won: ")
print(prize) #Printing out how much money the user won 
            
	
	
	

	

	
	
	
