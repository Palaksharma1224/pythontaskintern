def calculator(a,b):
    match input("enter the expression(+,-,*,/,%,//): "):
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
            print("floor division",c)
        case _:
            print("default statement.")
calculator(12,5)