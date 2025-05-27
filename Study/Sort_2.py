## 함수 선언 ##
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if(ary[minIdx] > ary[k]):
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

    return ary

## 전역 변수 ##
dataAry = [188, 162, 168, 120, 50, 130, 77, 54, 230, 229]

if __name__ == "__main__":
    print('정렬 전--> ', dataAry)
    dataAry = selectionSort(dataAry)
    print('정렬 후--> ', dataAry)