# == 시간 초과 답
# binary search도 필요 없고, list랑 dictionary 두가지로 하면 되는 거였다..!

def binary_search(sorted_arr, str, start, end):
    if start > end:
        raise 'not found'

    mid = (start+end)//2
    if str == sorted_arr[mid][1]:
        return sorted_arr[mid][0]

    if str < sorted_arr[mid][1]:
        return binary_search(sorted_arr, str, start, mid-1)
    else:
        return binary_search(sorted_arr, str, mid+1, end)

def solution(arr, test_case):
    sorted_arr = sorted(arr, key=lambda x: x[1])
    
    for tc in test_case:
        if tc.isnumeric():
            print(arr[int(tc)-1][1])
        else:
            print(binary_search(sorted_arr, tc, 0, len(arr)-1))



if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    # book = [(1, 'pikkachu'), (2, 'dealibird'), (3, 'razor')]
    book = [(i, input()) for i in range(1, n+1)]
    test_case = [input() for _ in range(m)]

    solution(book, test_case)


# == 통과한 답
def solution(arr, dic, test_case):    
    for tc in test_case:
        if tc.isnumeric():
            print(arr[int(tc)])
        else:
            print(dic[tc])



if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    book_arr = ['empty']
    book_dic = {}
    for i in range(1, n+1):
        str = input()
        book_arr.append(str)
        book_dic[str] = i

    test_case = [input() for _ in range(m)]

    solution(book_arr, book_dic, test_case)
    