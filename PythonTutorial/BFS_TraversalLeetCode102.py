# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# For BFS Breadth first search use Queue to implement the array
import collections


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

    result = []

    q = collections.deque()
    q.append(root)

    while q:
        qlen = len(q)
        level = []
        for i in range(qlen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        result.append(level)

        return result
