def calculate_safety_management_cost(total_cost, safety_percentage):
    # 안전관리비 계산
    safety_cost = total_cost * (safety_percentage / 100)
    return safety_cost


def main():
    try:
        # 사용자 입력받기
        total_cost = float(input("프로젝트의 총 비용을 입력하세요 (원): "))
        safety_percentage = float(input("안전관리비 비율을 입력하세요 (%): "))

        # 안전관리비 계산
        safety_cost = calculate_safety_management_cost(total_cost, safety_percentage)

        # 결과 출력
        print(f"안전관리비는 {safety_cost:.2f} 원 입니다.")
    except ValueError:
        # 입력 값이 유효한 숫자가 아닌 경우 오류 메시지 출력
        print("유효한 숫자를 입력하세요.")


# 프로그램 시작
main()