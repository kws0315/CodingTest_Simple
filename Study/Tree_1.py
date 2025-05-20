class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

#전위 순회
def preorder(node): # 왼쪽부터 찾고 자식 노드가 None이면 부모노드의 right를 탐색
    if node == None:
        return
    print(node.data, end="->")
    preorder(node.left)
    preorder(node.right)

#중위 순회
def inorder(node): # 맨 아래있는 자식노드부터 탐색, 자식 노드가 None이면 부모노드의 right탐색
    if node == None:
        return
    inorder(node.left)
    print(node.data, end="->")
    inorder(node.right)

#후위 순회
def postorder(node): # 왼쪽부터 자식노드를 출력하고 None이면 부모노드를 출력하고 루트노드의 right로 이동해서 출력
    if node == None: # 최종적으로 루트 노드를 마지막에 출력
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end="->")

#이진 트리 노드 개수
def calc_count(node):
    if node == None:
        return 0
    else:
        return 1 + calc_count(node.left) + calc_count(node.right)

#이진 트리 깊이
def calc_height(node):
    if node == None:
        return 0
    hLeft = calc_height(node.left)
    hRight = calc_height(node.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1

if __name__ == "__main__":
    node1 = TreeNode()
    node2 = TreeNode()
    node3 = TreeNode()
    node4 = TreeNode()
    node5 = TreeNode()
    node6 = TreeNode()
    node7 = TreeNode()
    node8 = TreeNode()

    node1.data = '화사'
    node2.data = '솔라'
    node3.data = '문별'
    node4.data = '휘인'
    node5.data = '쯔위'
    node6.data = '다현'
    node7.data = '선미'
    node8.data = '사나'

    # 노드 왼쪽
    node1.left = node2
    node2.left = node4
    node2.right = node5
    node4.right = node6

    # 노드 오른쪽
    node1.right = node3
    node3.left = node7
    node7.right = node8

    print("=======트리 구조=======")
    print(node1.data)
    print(node1.left.data, node1.right.data)
    print(node1.left.left.data, node1.left.right.data, node1.right.left.data)
    print(node1.left.left.right.data, node1.right.left.right.data, "\n")

    print("=======트리 탐색=======")
    print('전위 순회: ', end=' ')
    preorder(node1)
    print('끝')

    print('중위 순회: ', end=' ')
    inorder(node1)
    print('끝')

    print('후위 순회: ', end=' ')
    postorder(node1)
    print('끝\n')

    print("=======노드의 갯수&레벨=======")
    cnt = calc_count(node1)
    print("노드의 개수: ", cnt)

    height = calc_height(node1)
    print("트리의 높이: ", height)