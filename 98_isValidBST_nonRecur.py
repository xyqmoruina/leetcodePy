# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #@return leftChild[], rightChild[]
    def checkRoot(self,root):
        l,r=[],[]
        i=0

        if root.left:
            l.append(root.left)
            while i<len(l):
                if l[i].left:
                    l.append(l[i].left)
                if l[i].right:
                    l.append(l[i].right)
                i=i+1
        i=0
        if root.right:
            r.append(root.right)
            while i<len(r):
                if r[i].left:
                    r.append(r[i].left)
                if r[i].right:
                    r.append(r[i].right)
                i=i+1
        return [l,r]
    #check if all left < root.val and all right > root.val
    def check(self, root):
        sub=self.checkRoot(root)
        l,r=sub[0],sub[1]
        for ll in l:
            if ll.val >= root.val:
                return False
        for rr in r:
            if rr.val <= root.val:
                return False
        return True
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or root.left is None and root.right is None:
            return True
        sub=self.checkRoot(root)
        
        l,r=sub[0],sub[1]
        #check rule1,2 and apply to subtree.
        for ll in l:
           # print ll.val
            if ll.val >= root.val or not self.check(ll) :
                return False
        for rr in r:
           # print rr.val
            if rr.val <= root.val or not self.check(rr):
                return False
        return True
            
            
            
            
            
            
            
            
            
            
            
            
