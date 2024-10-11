var = [1,2,3,4]
print(var, type(var))
var.append(6)
print(var, type(var))

class player:

    def __init__(self, name, age, Pnumber):
        self.name = name
        self.age = age
        self.Pnumber = Pnumber
    def info(self):
        print(f"가입하신 계정은 {self.name}이며, 나이는 {self.age}, 그리고 연락처는 {self.Pnumber}입니다.")

userme = player("조상준", 21, "010-6395-2922")

userme.info()