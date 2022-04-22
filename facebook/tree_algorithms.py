
from optparse import Values
from turtle import right


def tree_dfs_iterative(root):
    if root == None:
        return None
    mystack = [root]
    result = []
    while(mystack):
        curr = mystack.pop()
        result.append(curr)
        print(curr.val)
        if (curr.right): # need to push the right first 
            mystack.append(curr.right)
        if (curr.left):
            mystack.append(curr.left)
        



def tree_dfs_recursion(root):
    if root == None:
        return []
    leftvals = tree_dfs_recursion(root.left)
    rightvals =tree_dfs_recursion(root.right)    
    return [root.val,leftvals,rightvals]





def bfs_tree(root):
    myvalues = []
    if (root == None):
        return None
    myqueue = [root]
    while (len(myqueue)>0):
        curr = myqueue.pop(0)
        myvalues.append(curr)    # append or push
        if curr.left :
            myqueue.append(curr.left)
        if curr.right:
            myqueue.append(curr.right)
        

