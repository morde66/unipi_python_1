text = input("Enter text here: ")
x = len(text)
output = " "
for i in range(x):
    c = text[x - i - 1] #pairnei ton teleutaio xarakthra
    y1 = ord(c) #ton kanei se ascii arithmo
    y2 = 128 - y1 #upologizei to katoptriko se ascii
    output += chr(y2) #kanei ton  katoptriko se xarakthra kai ton vazei sto output strng
print(output)
