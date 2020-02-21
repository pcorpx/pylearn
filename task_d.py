#Неверный ответ

table_1 = []
table_2 = []
result_table = []

def receive(n, table):
    for line in range(n):
        a, b  = input().split(" ")
        table.append([a,b])
    return table

def compile(method):
    
    for row_1 in table_1:
        miss = 0
 
        for row_2 in table_2:
            if row_1[0] == row_2[0]:
                result_table.append([row_1[0], row_1[1], row_2[1]])
            
            elif (method == "LEFT") or (method == "FULL"):
                miss += 1
                if miss == len(table_2):
                    result_table.append([row_1[0], row_1[1], "NULL"])

    for row_2 in table_2:
        miss = 0
        for row_1 in table_1:
            if row_2[0] != row_1[0]:
                if (method == "RIGHT") or (method == "FULL"):
                    miss += 1
                    if miss == len(table_1):
                        result_table.append([row_2[0],  "NULL", row_2[1]])
                    

    return result_table

def output(result_table):
    print(len(result_table))
    for row in result_table:
        print(" ".join(row))


receive(int(input()), table_1)
receive(int(input()), table_2)
method = input()
result_table = compile(method)
output(result_table)