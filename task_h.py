#превышен лимит по памяти

import collections

n = int(input())
m = int(input())
k = int(input())
addrs = []
def receive(n, addrs):
    for line in range(n):
        ip  = input()
        addrs.append(ip)
    return addrs

receive(n, addrs)

bad = []
start = 0
end = m
def findip(start, end):
    c = collections.Counter()
    for ip in addrs[start:end]:
        c[ip] +=1
    
    for ip, count in c.items():
        if count >= k:
            bad.append(ip)
for i in range(n - m + 1):
    if end > n - 1:
        end = None
    findip(start, end)
    start += 1
    if end != None:
        end +=1


ips = sorted(bad, key=lambda x: x.split())

for ip in ips:
    print(ip)