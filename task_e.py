import json

data =json.loads(input())
counter_list = 0
counter_dict = 0
def sanit(data):
    global counter_dict
    global counter_list
    if isinstance(data, list):
        for item in data:
            if item == []:
                data.remove(item)
                counter_list += 1
            elif item == {}:
                data.remove(item)
                counter_dict +=1
            else:
                sanit(item)
    elif isinstance(data, dict):
        keys = list(data.keys())
        for key in keys:
            if data[key] == []:
                del data[key]
                counter_list += 1
            elif data[key] == {}:
                del data[key]
                counter_dict += 1
            else:
                sanit(data[key])
sanity = True
while sanity:
    prev_counter_list =  counter_list
    prev_counter_dict =  counter_dict
    sanit(data)
    if (prev_counter_list == counter_list) and (prev_counter_dict == counter_dict):
        sanity = False
if (data == []):
    data = ""
    counter_list += 1
if (data == {}):
    data = ""
    counter_dict += 1

print(str(counter_dict) + " " + str(counter_list))


