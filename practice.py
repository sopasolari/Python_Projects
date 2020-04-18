def cap(check):
    ins = ('how', 'what', 'why')
    capitalized = check.capitalize()
    if check.startswith(ins):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
check = ""
str = ""
while True:
    check = input("Say something:")
    if check != "/end":
        str += cap(check)
        str += " "
        print (str)
        continue
    else:
        print (str)
        break