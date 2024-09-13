import random

def ran_lotto():
    result = {}

    while len(a) < 6:
        ran_num = random.randint(1,45)
        if ran_num in result:
            print("d")
        else:
            result.append(ran_num)

    return result

print(ran_lotto())