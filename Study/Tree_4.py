import random


class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


memory = []
rootBook, rootAuth = None, None
bookAry = [['어린왕자', '생떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'], ['신곡', '단테'], ['돈키호테', '세르반테스'],
           ['동물농장', '조지오웰'], ['데미안', '헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅']]
random.shuffle(bookAry)

## 책 이름 트리 ##
node = TreeNode()
node.data = bookAry[0][0]
rootBook = node
memory.append(node)

for book in bookAry[1:]:
    name = book[0]
    node = TreeNode()
    node.data = name

    current = rootBook
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
    memory.append(node)
print("책 이름 트리 구성 완료!")

## 작가 이름 트리 ##
node = TreeNode()
node.data = bookAry[0][1]
rootBook = node
memory.append(node)

for book in bookAry[1:]:
    name = book[1]
    node = TreeNode()
    node.data = name

    current = rootAuth
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
    memory.append(node)
print("작가 이름 트리 구성 완료!")

if __name__ == "__main__":
    ## 책 이름 및 작가 이름 검색 ##
    bookOrAuth = int(input('책검색(1), 작가검색(2)-->'))
    findName = input('검색할 책 또는 작가-->')

    if bookOrAuth == 1:
        root = rootBook
    else:
        root = rootAuth

    current = root
    while True:
        if findName == current.data:
            print(findName, '을(를) 찾음')
            findYN = True
        elif findName < current.data:
            if current.left == None:
                print(findName, '이(가) 목록에 없음')
                break
            current = current.left
        else:
            if current.right == None:
                print(findName, '이(가) 목록에 없음')
                break
            current = current.right
