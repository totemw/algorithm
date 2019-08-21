"""
remove extra edge
Given a binary tree, where an arbitary node has 2 parents i.e two nodes in the tree have the same child. Identify the defective node and remove an extra edge to fix the tree.

Example:

Input:
	   1
	  / \
	 2   3
	/ \ /
   4   5

Output:

     1			       1
    / \			      / \
   2   3    or	     2   3
  / \ 			    /   /
 4   5		       4   5

Explanation: We can remove either 3-5 or 2-5.
Follow-up:
What if the tree is a BST?
What if the tree is an N-ary tree?
"""
"""
Perform DFS/BFS and maintain a nod-to-parent map. Where key is node and value is its parents.
If we see a "candidate" node with two parents then deleting any of those two edges should work.

For BST,
Find Lowest Common Ancestor for both parent nodes, call it "ancestor" node
compare ancestor node value with candidate node and check if it belongs to left/right side and delete incorrect edge.
"""
def BFS(V, Adj, s):
    parent = {s: None}
    frontier = [s]
    while frontier:
        next = [] # nex level
        for u in frontier:
            if u.left:
                # if u.left in parent -> return
                parent[u.left] = u
                next.append(u.left)
            if u.right:
                # if u.right in parent -> return
                parent[u.right] = u
                next.append(u.right)
        frontier = next