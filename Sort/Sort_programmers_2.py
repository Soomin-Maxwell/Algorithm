
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

'''
Source : https://programmers.co.kr/learn/courses/30/lessons/42746

# solution 풀이  
- 10과 1의 비교 : 1000 미만 갯수자리인 3자리까지 곱하고 key값으로 설정 
    예시 ; "101010" ("10" *3  ) < 111  ("1" *3 )
- 마지막 int -> str 하는 이유 : 00의 경우 0으로 변경하기 위해 

'''