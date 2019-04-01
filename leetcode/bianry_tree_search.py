# class Node(self):
#     def __init__(self, val = None):
#         self.val = val
#         self.left = None
#         self.right = None

# preorder inorder postorder
class Solution():
    def search_inorder_recursion(self, root):
        if root == None:
            return
        self.search_inorder(root.left)
        print(root.val)
        self.search_inorder(root.right)

    def search_inorder_loop(self, root):
        if root == None:
            return
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.val)
