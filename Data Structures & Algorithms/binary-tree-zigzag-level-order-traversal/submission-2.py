# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque()
        q.append(root)

        while (q):
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                if(curr):
                    level.append(curr.val)
                    
                    if(curr.left):
                        q.append(curr.left)
                    if(curr.right):
                        q.append(curr.right)
                
            if(len(result) % 2 != 0):
                level.reverse()

            if(len(level) > 0):
                result.append(level)

        return result
