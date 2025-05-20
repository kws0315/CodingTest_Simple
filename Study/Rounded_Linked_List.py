class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    print("======= 현재 노드 정보 =======")
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def insertNode(findData, insertData):
    global memory, head, current, pre

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        last = head
        while last.link != head:
            last = last.link

        last.link = node
        head = node
        return
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = head
            pre.link = node
            return
    node = Node()
    node.data = insertData
    current.link = node
    node.link = head


def deletNode(deleteData):
    global memory, head, current, pre
    if head.data == deleteData:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del (current)
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del (current)
            return


def findNode(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != head:
        current = current.link
        if current.data == findData:
            return current
    return Node()


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArr = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__":
    if dataArr:
        node = Node()
        node.data = dataArr[0]
        head = node
        node.link = head
        memory.append(node)

        for data in dataArr[1:]:
            pre = node
            node = Node()
            node.data = data
            pre.link = node
            node.link = head # 마지막 노드가 head를 가리키도록
            memory.append(node)

    while True:
        printNodes(head)
        print("========== 메뉴 =========="
              "\n1.삽입, 2.삭제, 3.검색, 4.종료")
        menuNum = int(input("메뉴를 선택해주세요 : "))
        if menuNum == 1:
            position = input("삽입할 노드의 위치를 입력해주세요 : ")
            data = input("삽입할 데이터를 입력해주세요: ")
            insertNode(position, data)
            printNodes(head)
        elif menuNum == 2:
            data = input("삭제할 데이터를 입력해주세요: ")
            deletNode(data)
            printNodes(head)
        elif menuNum == 3:
            data = input("검색할 데이터를 입력해주세요: ")
            print("%s 이 검색되었습니다." % findNode(data))
            printNodes(head)
        elif menuNum == 4:
            break
