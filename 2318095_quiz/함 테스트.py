wt_calculate = input("원하는 계산은 무엇인가요?:")

if wt_calculate == "재해손실일수":
    def calculate_loss_days(disability_grade):
        if 1 <= disability_grade <= 3:
            return 7500
        elif disability_grade == 4:
            return 5500
        elif disability_grade == 5:
            return 4000
        elif disability_grade == 6:
            return 3000
        elif disability_grade == 7:
            return 2200
        elif disability_grade == 8:
            return 1500
        elif disability_grade == 9:
            return 1000
        elif disability_grade == 10:
            return 600
        elif disability_grade == 11:
            return 400
        elif disability_grade == 12:
            return 200
        elif disability_grade == 13:
            return 100
        elif disability_grade == 14:
            return 50
        else:
            return None


    disability_grade = int(input("장애 등급을 입력하세요 (1~14): "))

    loss_days = calculate_loss_days(disability_grade)
    if loss_days is not None:
        print(f"장애 등급 {disability_grade}에 따른 재해 손실 일수는 {loss_days}일 입니다.")
    else:
        print("잘못된 등급이 입력되었습니다.")