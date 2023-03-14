import os 

def calculator():
    def add(n1, n2 ):
     return n1+n2
    def sub(n1, n2):
      return n1-n2
    def mul(n1, n2 ):
     return n1*n2
    def div (n1, n2):
     return n1/n2
    operations={
"+":add, 
"-":sub, 
"*":mul, 
"/":div
}
    function = operations["+"]
    function(2,3)

    num1 = float (input("What\'s the first number: "))
    num2 = float (input("What\'s the second number: "))

    for i in operations:
     print(i)
    picked_operation=input("Choose one of the following options from above: ")
    first_answer=operations[picked_operation](num1,num2)
    last_calculated=first_answer
    print(f"{num1} {picked_operation} {num2} = {first_answer}")
    go_on = "yes"
    while (go_on=="yes"):

        picked_operation = input("Pick another operation: ")
        num3 = float(input("What's the next number: "))
        calculation_function = operations[picked_operation]
        second_answer = calculation_function((last_calculated), num3)
        print (f"{last_calculated} {picked_operation} {num3} = {second_answer}")
        go_on = input("Would you like to continue? Type 'yes' or 'no'").lower()
        last_calculated=float (second_answer)
    if input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to start a new calculator: ") == "y":
        num1 = second_answer
    else:
        go_on="no"
        calculator()
calculator()

