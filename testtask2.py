import collections
c = collections.Counter()
n = int(input()) 
numbers = [i for i in input().split()] 
for number in numbers:
    c[number] +=1

ordered_list = c.most_common()
equals = [ordered_list[0],]
if len(ordered_list) > 1: 
    m = 1
    while m < len(ordered_list) and equals[0][1] == ordered_list[m][1]:
        equals.append(ordered_list[m])
        m += 1

print(max(equals,key=lambda item:int(item[0]))[0])