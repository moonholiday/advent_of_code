
file = open('input.txt', 'r')
data = file.read()

floor = 0;
position = 0;

for i in data:
    position += 1
    if(i == "("):
       floor += 1
       if(floor == -1):
           break
    elif(i == ")"):
       floor -= 1
       if(floor == -1):
           break

print(position)
