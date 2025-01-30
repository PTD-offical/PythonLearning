Result = ""

# App Functions

# Addition Function
def AdditionFunc():
    global Result, Numb1, Numb2
    Result = Numb1 + Numb2
    print(F'Your Result is: {Result}')
    
# Subtraction Function
def SubtractionFunc():
  global Result, Numb1, Numb2
  Result = Numb1 - Numb2
  print(F'Your Result is: {Result}')

# Multiplication Function
def MultiplicationFunc():
  global Result, Numb1, Numb2
  Result = Numb1 * Numb2
  print(F'Your Result is: {Result}')
  
# Division Function
def DivisionFunc():
  global Result, Numb1, Numb2
  Result = Numb1 / Numb2
  print(F'Your Result is: {Result}')
  
# ##########################################################################
  
# Main Application
if __name__ == "__main__":
    print("Welcome, User.")
    while True:
        print("\n")
        print("Select your operation.")
        print("########################")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        print("########################")
        
        # Choice Input
        choice = input("Enter Your Choice: ")
        
        # Exit Condition
        if choice == "5":
            print("Good Bye User.")
            break
        
        # Check for valid operations before asking for numbers
        if choice == "1":
            try:
                # Number Input
                Numb1 = int(input("Enter Your First Number: "))
                Numb2 = int(input("Enter Your Second Number: "))
                AdditionFunc()
            except ValueError:
                print("Please enter valid numbers!")
        elif choice == "2":
            try:
                # Number Input
                Numb1 = int(input("Enter Your First Number: "))
                Numb2 = int(input("Enter Your Second Number: "))
                SubtractionFunc()
            except ValueError:
                print("Please enter valid numbers!")
        elif choice == "3":
            try:
                # Number Input
                Numb1 = int(input("Enter Your First Number: "))
                Numb2 = int(input("Enter Your Second Number: "))
                MultiplicationFunc()
            except ValueError:
                print("Please enter valid numbers!")
        elif choice == "4":
            try:
                # Number Input
                Numb1 = int(input("Enter Your First Number: "))
                Numb2 = int(input("Enter Your Second Number: "))
                DivisionFunc()
            except ValueError:
                print("Please enter valid numbers!")
        else:
            print("Invalid Choice.")
