#1
def add(a,b,c,d):
    result=a+b+c+d
    return result
def multiply(a,b,c,d):
    result=a*b*c*d
    return result

#2
def holzzak(a):
    result=a%2
    if result==0:
        print("짝수")
    else:
        print("홀수")
    return result

#3
def average(numbers):
    total=0
    for i in numbers:
        total+=i
        print(total)
    return total/len(numbers)

#4
class me:
    def __init__(self,id,gender,job):
        self.id=id
        self.gender=gender
        self.job=job
    def attack(self):
        print("공격!")

#5
class realestate:
    def __init__(self,location,size,building_type,price,year_built):
        self.location=location
        self.size=size
        self.building_type=building_type
        self.price=price
        self.year_built=year_built

    def display_info(self):
        print(f"위치:{self.location}")
        print(f"평수: {self.size}")
        print(f"건물 종류: {self.building_type}")
        print(f"가격: {self.price}")
        print(f"건축 연도: {self.year_built}")


estate = realestate("화성", 1000000, "우주선", 2000000000000000000, 3024)
estate.display_info()