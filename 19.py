# 문제 19. 숫자의 길이 구하기
number = 123456

# 1. 123
cnt = 0
result = 0
# 몫이 0이 되면 종료!
while number != 0:
    # result = result // 10
    number //= 10
    cnt += 1
print(cnt)

# 2. 문자열로 형변환
number = 123456
print(len(str(number)))

# 3. log
import math
number = 123456
print(int(math.log(number,10))+ 1)