def south_korea_resident_registration_number(a):
    if "-" in a:
        a.remove("-")
    valid_check_code = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    total = 0
    for k in range(0, 12):
        total += int(a[k])*valid_check_code[k]
    if (11-(total % 11)) % 10 == int(a[-1]):
        return "주민등록번호가 유효합니다."
    else:
        return "주민등록번호가 유효하지 않습니다."


resident_registration_number = list(input("주민등록번호를 입력하세요: "))
print(south_korea_resident_registration_number(resident_registration_number))