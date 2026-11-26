def multiplication(s_num, e_num):
    print("=" * 20)
    for i in range(s_num, e_num + 1):
        for j in range(1, 10):
            print(i, "X", j, "=", i * j)
        print("=" * 20)

start_num = int(input("시작할 단 수를 입력하세요 : "))
end_num = int(input("끝낼 단 수를 입력하세요 : "))
multiplication(start_num, end_num)