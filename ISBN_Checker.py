ISBN = int(input("Enter ISBN (10 digits): "))
l = len(str(ISBN))

if l == 10:
    sum = 0
    i = 10
    while ISBN > 0:
        r = ISBN % 10
        sum += r * i
        i -= 1
        ISBN = ISBN // 10
    
    if sum % 11 == 0:
        print("Legal ISBN")
    else:
        print("Illegal ISBN - not divisible by 11")
else:
    print("Illegal ISBN")
