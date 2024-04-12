num = int(input("몇 단까지 출력할까요?:"))

for num2 in range(1, num+1):
    print("------[",num2,"단]------")
    for db in range(1,num+1) :
      print(num2,"x",db,"=",num2*db)
