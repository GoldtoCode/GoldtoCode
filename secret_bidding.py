import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
d = {}
while True:
    ask = input("What is Your name: ")
    val = input("What is Your Bid: ")
    d[ask] = val
    yn = input("Are there more bidders? ")
    if yn.lower()[0] == "y":
        clear()
        continue
        
    else:
        clear()
        break
x = 0
for key in d:
    if x <float(d[key]):
        z = key
    else:
        continue
print(f"Winner is {z} with highest bid of {d[z]}")
