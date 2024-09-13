a = [[1,2,3],[4,5,6],[7,8,9]]

result=[]

for b in a:
    for num in b:
        if num % 2 == 0:
            result.append(num)


print(result)
