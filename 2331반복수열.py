# 나의 코드
# A, P = input().split(" ")
# lst = []
# visited = []
# def dfs(A):
#     # 처음 A
#     lst.append(int(A))
#     visited.append(A)
#     # 이후 A
#     num = sum([int(a) ** int(P) for a in A])
#     if str(num) not in visited:
#         dfs(str(num))
#     return visited
# print(dfs(A))

# n,m = map(int, input().split())
# check = [0] * (9**5 * 5)
# iteration = 1

# def cal(a,b):
#     result = 0
#     for i in str(a):
#         result += pow(int(i), b)
#     return result

# def dfs(n,m, iteration, check):
#     if check != 0:
#         return check[n] - 1

#     check[n] = iteration
#     iteration += 1
#     result = cal(n,m)
#     return dfs(result, m, iteration, check)

# print(dfs(n,m,iteration,check))

# 문제
# A=57, P=2
# 수열 D는 [57, 74, 65, 61, // 37, 58, 89, 145, 42, 20, 4, 16, // 37 ...]
# 답은 4개..


# 각 자리수 마다 p승하는 연산자
def cal_sequence(a, p):
    answer = 0
    for i in str(a):
        answer += pow(int(i), p)
    return answer


# check = [0]*250000  # 최댓값 4*9^5
# check 변수로 방문했는지 확인
# 만약 중복된 수가 나온다면, check리스트에서 그 위치는 이미 count로 채워져있음.


def dfs(a, p, count, check):
    # 해당 수열 값이 중복된 지 확인
    # 중복된 수라면 이미 그 자리엔 개수가 있기 때문
    # count != 0 이면 중복 된 것이므로 재귀를 멈추게 된다.
    if check[a] != 0:
        return check[a] - 1  # 중복 순열의 바로 앞의 원소 개수를 나타냄.

    check[a] = count
    next = cal_sequence(a, p)
    count += 1

    # 중복이 생길 때 까지 탐색
    return dfs(next, p, count, check)


def solution():
    # 각 index는 수열의 수를 뜻함
    check = [0] * 250000  # 최댓값 4*9^5

    # 첫수, 제곱 횟수
    a, p = map(int, input().split())
    count = 1  # 나온 수열의 개수
    print(dfs(a, p, count, check))


## __name__ == "main"
if __name__ == "__main__":
    solution()
