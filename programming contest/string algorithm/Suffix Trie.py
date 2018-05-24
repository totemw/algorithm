"""
Suffix Trie

- a rooted tree that stores all the suffixes
- each node corresponds to some substring of T
- each edge is associated with an alphabet
- For each node that corresponds to ax, there is a special
  pointer called 'suffix link' that leads to the node
  corresponding to x

"""