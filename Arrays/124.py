def isbalanced(s):
    c = 0
    for i in s:
        if i == "(":
            c += 1
        elif i == ")":
            c -= 1
        if c < 0:
            return "no"
        if c == 0:
            return "yes"
    return "no"


s = input()
print(isbalanced(s))  