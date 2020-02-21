
#Превышен лимит времени исполнения

sessions = []
counter = {}
def receive(n, sessions):
    for line in range(n):
        start, end  = input().split(" ")
        sessions.append([start,end])
    return sessions

receive(int(input()), sessions)
earliest = min(sessions, key = lambda x: x[0])[0]
latest = max(sessions, key = lambda x: x[1])[1]
for t in range(int(earliest), int(latest) + 1):
    counter[t] = 0  
    for session in sessions:
        if int(session[0]) <= t <= int(session[1]):
            counter[t] += 1
max_quantiny = max(counter.items(), key = lambda x: x[1] )
popular = min([x for x in counter.keys() if counter[x] == max_quantiny[1]])
print(popular)