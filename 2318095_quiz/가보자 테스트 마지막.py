#환율
exchange_rate = {"달러":1320, "엔":950, "위안":182}

# 철수가 가지고 있는 돈 순서대로 달러, 엔, 위안
money = [13, 200, 13]

#환전 후 금액
total_money = (exchange_rate["달러"]*money[0])+(exchange_rate["엔"]*money[1])+(exchange_rate["위안"]*money[2])

#결과
print("철수가 가지고 있는 돈의 원화 가치는",total_money, "입니다.")