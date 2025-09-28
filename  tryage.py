def check_age():
    try:
        age = int(input("Enter your age: "))
        if age>0:
           if age<=60:
              print("Your age is ",age)
              if age%2== 0:
                  print("Age is even ")
              else:
                  print("Age is odd")
           else:
               print("Invalid age is not less than 60")
        else:
            print("Invalid age age must be positive")
    except ValueError:
        print("Invalid input! Please enter a numeric value for age.")                
check_age()
                  



