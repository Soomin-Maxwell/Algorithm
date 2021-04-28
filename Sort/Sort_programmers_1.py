
def solution(array, commands):
    answer = []

    for command in commands : 
        i = command[0]
        j = command[1]
        k = command[2]

        myList_1 = array[i-1:j]
        myList_1.sort()
        answer.append(myList_1[k-1])

    return answer




'''
Source : https://programmers.co.kr/learn/courses/30/lessons/42748

'''