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



# 통과한 답
