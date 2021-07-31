def chooseandSwap(st):
    string = list(st)
    n = len(string)
    olist = [-1] * 26

    for i in range(n):

        if (olist[ord(string[i]) - 97] == -1):
            olist[ord(string[i]) - 97] = i

    for i in range(n):
        flag = False

        for j in range(ord(string[i]) - 97):

            if (olist[j] > olist[ord(string[i]) - 97]):
                flag = True
                break

        if (flag):
            break
        else:
            return "".join(string)

    if (i < n):

        character1 = (string[i])
        character2 = chr(j + 97)

        for i in range(n):

            if (string[i] == character1):
                string[i] = character2

            elif (string[i] == character2):
                string[i] = character1

    return "".join(string)


print(chooseandSwap("ccad"))