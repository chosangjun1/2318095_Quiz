num = (input("몇 단까지 출력할까요?:"))
a = int(num)
for num in range(1, a+1):
    print("-----[",num,"단]------")
    for b in range(1,num+1):
      print(num,"x",b,"=",num*b)
print("----------[출력완료]----------")