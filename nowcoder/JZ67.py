# -*- coding:utf-8 -*-

# def back_track(n):
#     if n <= 4:
#         return n
#     result = 0
#     for i in range(1, n):
#         result = max(result, i*back_track(n-i))
#     return result


def cutRope(number):
    # write code here
    if number <= 4:
        return number
    result = []
    for i in range(number+1):
        result.append(i)

    for i in range(5, number+1):
        for j in range(1, i):
            result[i] = max(result[i], j * result[i-j])
    return result[number]



print cutRope(8)