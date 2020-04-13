averg = []
userinp = int(input("How values you want to add:"))
for x in range(userinp):
    averg.append(float(input("Enter the %d value for avarage:" % (x+1))))
print (averg)

print("The average grades of yours student is:", sum(averg) / len(averg))
print("The max it is:",max(averg))