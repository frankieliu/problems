def trav(tnode):

    if tnode.left == None and tnode.right == None:
        return tnode.val
    val1 = trav(tnode.left)
    val2 = trav(tnode.right)
    operation = ops[tnode.val]
    return operation(val1, val2)
"""
tnode
 tnode.left
  tnode.left.left
   tnode.left.left.left
    val..
   tnode.left.left.right
    val..
   op(val,val)
  tnode.left.rigth
"""
