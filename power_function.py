# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:24:52 2021

@author: Linga Banda aka A.B
"""
#Code that demonstrates Power Function in Python
def power_of(n, p): #The function takes in n as number, p as power
    
    ans=n #initialises answer with the number
    
    for i in range (1, p): # the range runs to the power 
        
        ans*=n
        
    print(str(n) +" to the power " +str(p)+" is " +str(ans))
        
def main():
    
    num=input("Enter the number: \n") #Takes in number from the user
    num=int(num)
    
    pow_=input("Enter the power: ") #Takes in the power from the user
    pow_=int(pow_)
    
    power_of(num, pow_) #takes in inputs from user 
    
if __name__ == "__main__":

    main() 
    
#The end