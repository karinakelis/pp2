import re
with open('row.txt', 'r', encoding='utf-8') as file:
 data = file.read()

#exercise 1
mylist = []
corrects = data.split()
for i in corrects:
    match = re.search(r'a.*b+', i)
    if match:
      mylist.append(match.group())

print(mylist)


