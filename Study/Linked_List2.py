class Node():
    def __init__(self):
        self.data = None
        self.link = None

def delete_Node(deleteData):
    global memory, head, currnet, pre

    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def insert_Node(findData, insertData):
    global memory, head, currnet, pre

    # 첫 번째 노드 삽입
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    # 중간 노드 삽입
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    # 마지막 노드 삽입
    node = Node()
    node.data = insertData
    current.link = node

def print_Nodes(start):
    current = start
    if current == Node:
        return
    print(current.data, end=', ')
    while current.link != None:
        current = current.link
        print(current.data, end=', ')
    print()

def find_Node(findData):
    global memory, head, currnet, pre

    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    return Node()
# 전역 변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ["라파", "망귀인", "완매", "갤러거", "더 헤르타", "트리비", "어벤츄린", "헤르타"]

# 메인 코드
if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0]
    head = node
    current = head
    memory.append(node)
## 과제는 첫번째 삽입, 중간 삽입 부분만 수정해서 제출하면 된다 (책에 코드 있음)
    for data in dataArray[1:]:
        pre = node
        node = Node()
        current = node
        node.data = data
        pre.link = node
        memory.append(node)
    print_Nodes(head)
