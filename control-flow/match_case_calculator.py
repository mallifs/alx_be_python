num1 = int(input("Enter first number:"))
num2 = int(input("Enter secon number:"))
operation = input(("+, -, *, /:"))

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2 
        print(f"The result is {result}")  
    case "/":
        if num2 == 0:
            print(f"cannot divide by 0")
        else:
            result = num1 / num2
            print(f"the result is {result}")
    case _:
        print("Invalid operation")            
                  
