averg = []
averg.append(float(input("Enter the 1 value for avarage:")))
averg.append(float(input("Enter the 2 value for avarage:")))
averg.append(float(input("Enter the 3 value for avarage:")))
averg.append(float(input("Enter the 4 value for avarage:")))
print (averg)
print("The average grades of yours student is:", sum(averg) / len(averg))
print("The max it is:",max(averg))