# Faulty Calculator
while True:
    var1 = int(input("Enter your first number \n"))
    oper = input("Enter the operator -\n(+)\n-(-)\n-(*)\n-(/)\n")
    var2 = int(input("Enter your second number \n"))
    if var1 == 45 and oper == "*" and var2 == 3:
          print("555")
    elif var1 == 56 and oper == "+" and var2 == 9:
          print("77")
    elif var1 == 56 and oper == "/" and var2 == 6:
          print("4")
    elif oper == "+":
          print(var1+var2)
    elif oper == "-":
          print(var1-var2)
    elif oper == "*":
          print(var2*var1)
    elif oper == "/":
          print(var2/var1)
    next_calculation = input("Let's do next calculation ? (yes)/(no): ")
    if next_calculation == "no":
            print("Bye , Dear User !")
            break
    else:
        pass
