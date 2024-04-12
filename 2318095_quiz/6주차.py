num = (input("몇 단까지 출력할까요?:"))
a = int(num)
for num2 in range(1, a+1) :
    print("------[",num2,"단]------")
    for b in range(1,num2+1) :
      print(num2,"x",b,"=",num2*a)