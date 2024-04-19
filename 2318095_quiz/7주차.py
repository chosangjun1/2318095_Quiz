numbers = [[1,2,3], [4,5,6], [7,8,9]]
results = []

for row in numbers:
    for num in row:
        if num % 2 == 0:
            results.append(num)

print("짝수를출력해보겠습니다~:",results)
