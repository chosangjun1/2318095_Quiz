class fishbread:
    total_sales = 0

    def __init__(self, contents, price):
        self.contents = contents
        self.price = price

    def sell(self):
        print(f"{self.contents} 붕어빵을 {self.price}원에 팔았습니다.")
        fishbread.total_sales += self.price

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹었습니다.")

    @classmethod
    def print_total_sales(cls):
        print(f"총 판매금: {cls.total_sales}원")


custard_fishbread = fishbread("슈크림", 1000)
red_bean_fishbread = fishbread("팥", 1000)

custard_fishbread.sell()
custard_fishbread.sell()
fishbread.print_total_sales()

# 팥 붕어빵 판매 및 총 판매금 출력
red_bean_fishbread.sell()
fishbread.print_total_sales()

# 슈크림 붕어빵 먹기
custard_fishbread.eat()

# 팥 붕어빵 먹기
red_bean_fishbread.eat()
