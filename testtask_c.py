#Превыщен лимит по памяти
n = int(input()) 
seq_keys = [int(i) for i in input().split()] 
limit = max(seq_keys)
seq = [0, 1, 2]

for number in range(limit-2):
    seq.append(seq[len(seq)-1] + seq[len(seq)-3])
result = ""
for k in seq_keys:
    result += " " + str(seq[k])

print(result[1:])