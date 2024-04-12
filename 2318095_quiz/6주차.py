num = int(input("몇 단까지 출력할까요?:"))

for num2 in range(1, num+1) :
    print("------[",num2,"단]------")
    for a in range(1,num+1) :
      print(num2,"x",a,"=",num2*a)