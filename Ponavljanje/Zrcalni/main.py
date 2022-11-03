number = int(input())
counter = 0
hitBreak = False

while number > 0:
    digit = number % 10
    if digit == 0 and counter == 0 and len(number) != 1:
        print("NE")
        hitBreak = True
        break
    elif digit != 0 and digit != 8:
        print("NE")
        hitBreak = True
        break
    
    number //= 10
    counter += 1

if hitBreak == False:
    print("DA")
