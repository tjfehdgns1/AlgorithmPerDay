class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(node):
    if node is not None:
        print(node.data, end="")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end="")
        inorder_traversal(node.right)


def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end="")


def build_tree(nodes_info):
    node_dict = {}

    for info in nodes_info:
        data, left, right = info

        if data not in node_dict:
            node_dict[data] = Node(data)

        if left != ".":
            node_dict[left] = Node(left)
            node_dict[data].left = node_dict[left]

        if right != ".":
            node_dict[right] = Node(right)
            node_dict[data].right = node_dict[right]

    return node_dict["A"]


def main():
    N = int(input())
    nodes_info = [input().split() for _ in range(N)]

    root = build_tree(nodes_info)

    # 전위 순회
    preorder_traversal(root)
    print()

    # 중위 순회
    inorder_traversal(root)
    print()

    # 후위 순회
    postorder_traversal(root)


if __name__ == "__main__":
    main()
