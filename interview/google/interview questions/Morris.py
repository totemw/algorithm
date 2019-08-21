"""
Find sum of the leaf nodes of the binary tree,
provided there are billions of nodes in the tree.
Expected O(1) space solution (you can't use recursion as it will throw stack overflow exception).

You an also do some modifications in your tree.
Use a stack to traverse the tree.


public int sum(TreeNode root) {
		int sum = 0;
		Stack<TreeNode> stack = new Stack<>();
		TreeNode curr = root;
		while(curr != null) {
			stack.push(curr);
			curr = curr.left;
		}
		while(!stack.isEmpty()) {
			TreeNode node = stack.pop();
			if(node.left == null && node.right == null) {
				sum += node.val;
			}else {
				TreeNode right = node.right;
				while(right != null) {
					stack.push(right);
					right = right.left;
				}
			}
		}
		return sum;
    }

2. Morris traversal

1. Initialize current as root
2. While current is not NULL
   If the current does not have left child
      a) Print current’s data
      b) Go to the right, i.e., current = current->right
   Else
      a) Make current as the right child of the rightmost
         node in current's left subtree
      b) Go to this left child, i.e., current = current->left
"""


# Iterative function for inorder tree traversal
def MorrisTraversalInorder(root):
    # Set current to root of binary tree
    current = root

    while (current is not None):

        if current.left is None:
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while (pre.right is not None and pre.right != current):
                pre = pre.right
            sum += pre.val

                # Make current as right child of its inorder predecessor
            if (pre.right is None):
                pre.right = current
                current = current.left

            #     # Revert the changes made in if part to restore the
            # # original tree i.e., fix the right child of predecessor
            # else:
            #     pre.right = None
            #     current = current.right
