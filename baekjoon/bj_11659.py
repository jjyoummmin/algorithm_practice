# 누적합 기초
def cum_sum_generator(arr):
    acc = 0
    yield 0
    for x in arr:
        acc += int(x)
        yield acc


def solve():
    _, m = [int(x) for x in input().split()]
    cum_sum = list(cum_sum_generator(input().split()))

    result = []
    for _ in range(m):
        i, j = [int(x) for x in input().split()]
        result.append(cum_sum[j] - cum_sum[i-1])
    
    return result

result = solve()
for x in result:
    print(x)