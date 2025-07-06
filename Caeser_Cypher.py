alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz01234567890123456789"
def shift():
    global x
    global shif
    x = input("Type yr message: ")
    shif = int(input("Type shift number: "))
    if shif > 26:
        print("Please input from 0 to 26")
        shift()
def encode():
    shift()
    answer = ""
    for i in x:
        if i == " ":
            answer = answer + " "
            continue
        z = alphabets.find(i)
        z = z + shif
        z = alphabets[z]
        answer = answer+z
    print(answer)
def decode():
    shift()
    answer = ""
    for i in x:
        if i == " ":
            answer = answer + " "
            continue
        z = alphabets.find(i)
        z = z - shif
        z = alphabets[z]
        answer = answer+z
    print(answer)

while True:
    enordeco = input("Type encode or decode: ")
    if enordeco[0].lower() == "e":
        encode()
        
    elif enordeco[0].lower() == "d":
        decode()
    else:
        print("Please type 'enocode' or 'decode'.")
    ask = input("Do you want to continue? yes or no: ")
    if ask[0].lower() == "y":
        continue
    elif ask[0].lower() == "n":
        break
print("Thanks for using our programme")

