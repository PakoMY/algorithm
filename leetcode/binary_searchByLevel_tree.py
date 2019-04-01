# class Node(self):
#     def __init__(self, val = None):
#         self.val = val
#         self.left = None
#         self.right = None
class Solution():
    def levelOrder(self, root):
        res = []
        # 边缘条件
        if root is None:
            return res

        # 搞一个队列存储节点
        q = []
        q.append(root)
        # 队列如果空了结束循环
        while(q != None):
            tmp = []
            length = len(q)
            for i in range(length):
                ele = q.pop(0)
                tmp.append(ele.val)
                if ele.left != None:
                    q.append(ele.left)
                if ele.right != None:
                    q.append(ele.right)
            res.append(tmp)
        return res
