import re

pattern = r"\b([0*1*]+)\b"
with open("text.txt", "r") as file:
    findall = re.findall(pattern, file.read())
print (findall)
lenght = len(findall)
for i in findall:
    count = int(i, 2)
    if (count % 3 == 0) and (count != 0):
        print (bin(count)[2:])

