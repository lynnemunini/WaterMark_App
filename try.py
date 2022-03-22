def solution(A):
    i = 1
    while (i < max(A)):
        if i in A:
            i += 1
            pass
        else:
            print(i)
            break

solution([1,4,8,5])



