# Program to demonstrate login checking using decorator 
password = "Onkar@2007"
def login_required(func): 
    def wrapper(): 
        print("Checking login status...")
        print("ENTER PASSWORD")
        if input() == password:  
            print("User access completed")
            func() 
        else:
            print("Access denied")
    return wrapper 

@login_required 
def dashboard(): 
    print("Welcome to Dashboard") 
    
dashboard()