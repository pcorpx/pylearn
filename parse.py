serials = ""
with open("text.txt", "r") as file:
    for line in file:
        serial = line.split(',')[2]
        serial = serial.split('\t')[0]
        serials += serial + ", "

with open("out.txt", "w") as file:
    file.write(serials[:-1])