class 붕어빵:
    def __init__(self, contents, price):
        self.contents = contents
        self.price = price
        self.total_sales = 0

    def sell(self):
        self.total_sales += self.price
        print(f"{self.contents} 붕어빵이 {self.price}원에 판매되었습니다.")


    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")



shukcream_bungeo = 붕어빵("슈크림", 2000)
redbean_bungeo = 붕어빵("팥", 1500)

shukcream_bungeo.sell()
shukcream_bungeo.eat()
redbean_bungeo.sell()
redbean_bungeo.eat()


print(f"총 판매 금액: {shukcream_bungeo.total_sales + redbean_bungeo.total_sales}원")

