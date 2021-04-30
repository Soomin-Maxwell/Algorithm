def solution(citations):
    citations.sort()
    answer = []
    for i in range(len(citations)) :
        if citations[i] <= len(citations[i:]):
            answer.append(citations[i])
    return max(answer)

'''Source : https://programmers.co.kr/learn/courses/30/lessons/42747'''
