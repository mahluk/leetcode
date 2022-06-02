class TrieNode:
  """ Represents node in trie """
  def __init__(self, char):
    self.char = char
    self.isLeaf = False

    """
      a dict of neighbour nodes
      keys are characters and values are nodes
    """
    self.children = {}

class Trie:
  """ Represents prefix tree """

  """
    The trie has at least the root node which doesn't store any char
  """
  def __init__(self):
    self.root = TrieNode("")

  def insert(self, word):
    """
      Insert a word into the trie
    """
    node = self.root

    for char in word:
      if char in node.children:
        node = node.children[char]
      else:
        new_node = TrieNode(char)
        node.children[char] = new_node
        node.isLeaf = False
        new_node.isLeaf = True
        node = new_node
  
  def dfs(self, node, prefix):
    """
      Depth-first traversal of the trie  
      Args:
        - node: the node to start with
        - prefix: the current prefix, for tracing a word while traversing the trie
    """

    if node.isLeaf:
      self.result.append(prefix + node.char)

    for child in node.children.values():
      self.dfs(child, prefix + node.char)

  def query(self, prefix):
    """
      Given an input (a prefix), retrieve all words stored in
      the trie with that prefix
    """

    node = self.root
    self.result = []

    for char in prefix:
      if char in node.children:
        node = node.children[char]
      else:
        return []

    self.dfs(node, prefix[:-1])
    return self.result
    