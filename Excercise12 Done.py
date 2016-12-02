class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 

 
 

    
 
def inOrder(tree):
    lst = [] # initialze stack
    done = 0
     
    while not done:
         
        if tree is not None:
            lst.append(tree)       
            tree = tree.left 
        else:
            if(len(lst) >0 ):
                tree = lst.pop()
                print (tree.value)

                tree = tree.right 
 
            else:
                done = 1
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  inOrder(t)
