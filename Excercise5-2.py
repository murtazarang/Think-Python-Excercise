flag = 0;
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for n in range(3, 10):
                value = a**n + b**n;
                if value == c**n:
                    flag = 1
                    break
                break
            break
        break
    break

if flag == 1:
    print ("Holy Smokes, Fermat was wrong!")
else:
    print ("No, that doesn't work")