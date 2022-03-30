import random
lottonum = []
for i in range(45):
    lottonum.append(i+1)
times = int(input("로또번호를 몇번 뽑을건지 숫자로 입력해주세요 : "))
for i in range(times):
    print("=====================================================")
    print("%d번째 로또 번호 추첨 :" %(i+1) ,end=" ")
    lotto = random.sample(lottonum, 7)
    lotto.insert(-1, "+")
    print(lotto)
print("=====================================================")

