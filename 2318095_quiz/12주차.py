class 붕어빵:
    def __init__(self, 재료, 가격):
        self.재료 = 재료
        self.price = 가격
        self.total = 0

    def sell(self):
        self.total = self.price + 0
        총_판매_가격 = self.total
        print(f"{self.재료} 붕어빵이 {self.price}원에 판매되었습니다.")

    def eat(self):
        print(f"{self.재료} 붕어빵을 먹었습니다.")

김예은_붕어빵 = 붕어빵("김예은", 1000)
전상완_붕어빵 = 붕어빵("전상완", 10212100)
이시현_붕어빵 = 붕어빵("이시현", 1)
교수님_붕어빵 = 붕어빵("교수님", 50000000000)

전상완_붕어빵.sell()
전상완_붕어빵.eat()
이시현_붕어빵.sell()
이시현_붕어빵.eat()
교수님_붕어빵.sell()
교수님_붕어빵.eat()
김예은_붕어빵.sell()
김예은_붕어빵.eat()
print(f"총 판매금: {붕어빵.총_판매_가격}원 입니다.")

