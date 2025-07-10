def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def multiply(a,b):
    return a * b
def div(a,b):
    return a / b

d = {
    '+':add,
    "-":sub,
    "*":multiply,
    "/":div
}
def calculator():
    x = float(input("First Number: "))

    should_continue = True

    while should_continue:
        for i in d: print(i)
        sym = input("Pick an operation: ")
        y = float(input("Second Number: "))
        answer = d[sym](x,y)
        print(f"{x} {sym} {y} = {answer}")
        if input(f"Type 'n' for new calc and type 'y' for conitnue calc with {answer}: ") == "y":
            x = answer
        else:
            should_continue = False
            calculator()

calculator()
