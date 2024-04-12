a = int(input("몇 단까지 출력할까요?"))

for z in range(1, a+1) :
    print("------[",z,"단]------")
    for y in range(1,20) :
      print(z,"x",y,"=",z*y)