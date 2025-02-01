import random

def start():
    
    print("Press 1 to start \nPress 0 to exit ")
    inp=input("0 OR 1 : ")
    print()
    if inp=="0":
        print("Exiting") 
        return
    elif inp=="1":
        play()  
    else:
        print("Invalid input") 
        print()
        start()
        
        
def play():
   
   x={17:4 ,24:16 ,39:12, 56:48, 61:23 , 72:63 , 84:55 ,95:12 ,99:88} 
   print('Snakes are present at : ',end = "")
   for z in x:
       print(z,end=" ")
   print()    

   place=0
   while place<100:
       
       i=input('Press 7 to roll the dice : ')
       print()
       
       if i=="7":
           
           dice = random.randint(1, 6) 
           place+=dice
               
           if place>100:
               
                place-=dice
                print(f'DICE GOT {dice} ')
                print("Can't move forward ")
                print(f'YOUR PLACE {place} ')
                print()
                
           else: 
                     
               print(f'DICE GOT {dice} ')
               print(f'YOUR PLACE {place} ')
               print()
           
           #Alternate: for c in x: if place in x: place=x[place]
          
               if place in x.keys():
                   place=x[place]
                   print(f"Bitten!! Moved to {place}")
                   print()
       
       
       elif i=="0":
           print("Exit") 
           break
      
       else:
           print("Invalid input")
           print()
           continue
    
       if place==100:
           print('CONGRATULATIONS!! YOU REACHED 100 🏆')
           


print('        WELCOME TO SNAKE LADDER GAME!')
print("If you want to exit the game anywhen, press 0\n") 
start()