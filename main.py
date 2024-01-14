#python program to illustrate 
#function with main

def getinteger():
    result = int(input("Enter the number : "))
    return result 
    
def main():
    print("started")
    
    #calling the getinteger function and 
    #storing its returned value in the output variable 
    output = getinteger()
    print(output)
    
#now we are required to tell python 
#for 'main' function existence 

if __name__=="__main__":
    main()
