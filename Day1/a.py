file = open('input.txt', 'r')
data = file.read()

floor = 0;

for i in data:
    if(i == "("):
        floor += 1;
    elif(i == ")"):
       floor -= 1;

print(floor)
