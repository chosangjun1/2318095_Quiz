import random

def ran_lotto():
    results = []

    while len(results) < 6:
        ran_num = random.randint(1, 45)
        if ran_num in results:
            print("results 안에 ran_num이 있으므로, result를 제거하고 출력했습니다.")
        else:
            results.append(ran_num)

    return results

print(ran_lotto())
