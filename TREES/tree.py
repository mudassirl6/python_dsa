# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root):
        #your code goes here
        result = []

        if root == None:
            return []

        q = deque([root])

        while q:
            n = len(q)
            level = []
            for i in range(n):
                node = q.popleft()
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)


        return result


# iterative preorder implementation
def iter_pre(root):
    stack = [root]
    if stack == None:
        return None

    while stack:
        element = stack.pop()
        print(element.data)
        if element.right:
            stack.append(element.right)
        if element.left:
            stack.append(element.left)

#iterative inorder
def iter_inorder(root):
    stack = []
    result = []

    while 1:
        if root:
            stack.append(root)
            root = root.left

        else:
            if not stack:
                break
            root = stack.pop()
            result.append(root)
            root = root.right


    return result


def iter_postorder(root):
    stack1 = [root]
    stack2 = []
    result = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)


    while stack2:
        result.append(stack2.pop())






    
