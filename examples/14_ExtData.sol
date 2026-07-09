main()
; There are lots of more data types in extdata
; We will only focus on Binary Trees now.
  _get("std/extdata/BinaryTree.sol)
  ; First, initialize a normal list
  n<tree>
  ; Let's turn it into a binary tree
  ; 3 is the capacity
  BinaryTree.init(tree, 3)
  ; Let's insert a value
  BinaryTree.insert(tree, 1)
  ; Let's add a parent
  BinaryTree.insert(tree, 0)
  ; This will be value 1's parent
  ; Let's get its parent
  n -> BinaryTree.get_parent(1)
  _out -> n
end
