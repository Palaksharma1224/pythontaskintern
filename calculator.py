a=int(input("enter the  first number"))
b=int(input("enter the second number"))
match input("enter the operation (+, -, *, /, %, //): "):
    case "+":
        c=a+b
        print("sum",c)
    case "-":
        c=a-b
        print("sub",c)
    case "*":
        c=a*b
        print("mul",c)
    case "/":
        c=a/b
        print("div",c)
    case "%":
        c=a%b
        print("mod",c)
    case "//":
        c=a//b
        print("floor div",c)


    case _:
        print("the input given at switch case is wrong try another one.")