exitornah = True

while exitornah == True:

    welcum = input("welcome to calculator, y to keep calculating and n to exit    ")

    if welcum == "n":
        print("fuck you for not using my calculator")
        exitornah = False
        break
    if welcum == "y":
        print(" ")

    else:
        print("i told you to use y and n dumb bitch")
        exitornah = False
        break

    num1str = input("what is the first number?    ")
    try:
        num1int = int(num1str)
    except:
        print("error not a number, fuck you")
        exitornah = False
        break

    num2str = input("what is the second number?    ")
    try:
        num2int = int(num2str)
    except:
        print("error not a number, fuck you")
        exitornah = False
        break

    operator = input("choose an operator    ")
    operatorstr = str(operator)
    
    try:
        if operatorstr == '+':
            print(num1int, "+", num2int, "=", num1int+num2int)

        if operatorstr == '-':
            print(num1int, "-", num2int, "=", num1int-num2int)

        if operatorstr == '*':
            print(num1int, "*", num2int, "=", num1int*num2int)

        if operatorstr == '/':
            print(num1int, "/", num2int, "=", num1int/num2int)

        if operatorstr == '=':
            print(num1int, "=", num2int, "=", num1int==num2int)
    except:
        print("error, not an operator")
