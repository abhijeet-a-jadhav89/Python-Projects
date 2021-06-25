def xo(s):
    s = s.upper()
    count1 = 0
    count2 = 0
    for i in s:
        if i == 'X':
            count1 += 1
        elif i == 'O':
            count2 += 1

    if count1 == count2:
        return True
    else:
        return False

s =input("Enter srting ")
print(xo(s))