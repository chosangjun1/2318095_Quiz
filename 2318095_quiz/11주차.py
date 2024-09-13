
def so(a):
    a = a.replace("-", "")  # "-" 제거
    if len(a) != 13:  # 주민등록번호는 총 13자리여야 함
        return "주민등록번호의 길이가 잘못되었습니다."

    valid_check_code = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    total = 0
    for k in range(12):  # 0부터 11까지 반복
        total += int(a[k]) * valid_check_code[k]

    if (11 - (total % 11)) % 10 == int(a[-1]):
        return "주민등록번호가 유효합니다."
    else:
        return "주민등록번호가 유효하지 않습니다."


resident_registration_number = input("주민등록번호를 입력하세요: ")  # 문자열로 입력 받음
print(so(resident_registration_number))