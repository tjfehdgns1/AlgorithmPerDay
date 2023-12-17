import sys


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def construct_bst(preorder):
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    stack = [root]

    for value in preorder[1:]:
        node = TreeNode(value)

        if value < stack[-1].key:
            stack[-1].left = node
        else:
            while stack and stack[-1].key < value:
                last = stack.pop()

            last.right = node

        stack.append(node)

    return root

def postorder_traversal(root):
    result = []

    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            result.append(node.key)

    helper(root)
    return result

sys.setrecursionlimit(10000)
preorder_result = []

while True:
    try:
        value = int(input())
        preorder_result.append(value)
    except EOFError:
        break

root = construct_bst(preorder_result)

postorder_result = postorder_traversal(root)
for value in postorder_result:
    print(value)
