#Quora challenge for application of Software engineer (Grad)
#Author : Jinxuan Zhao (Steven)
 
from collections import deque
from collections import defaultdict

"""
The prefix tree under each category node. 
It supports querying if the category node 
contains the answer that has the prefix 
we are querying with. 
"""
class Trie(object):

    def __init__(self):
        self.root = {}

    def insert(self, word):
        currentTrieNode = self.root
        for c in word:
            if c not in currentTrieNode:
                currentTrieNode[c] = {}
            currentTrieNode = currentTrieNode.get(c)
        #if a node has the key "#" that means it is an endpoint. 
        currentTrieNode["#"] = {}

    def startsWith(self, prefix):
        currentTrieNode = self.root
        for c in prefix:
            if c not in currentTrieNode:
                return False
            currentTrieNode = currentTrieNode.get(c)
        return True
        
        

 
"""
The treenode of the category tree, 
which contains the label, child tree node
and the prefixTree node on itself.
"""
class treeNode(object):
    def __init__(self, label):
        self.category = label
        self.child = []
        self.prefixTreeNode = Trie()
        
        
class CategoryTree(object):

    def __init__(self, text):
        text = text.split(" ")
        self.root =  self.treeParser(text)

    """
    Helper function to parse input. 
    """
    def findNextMatchParen(self, text):
        count = 0
        for i, s in enumerate(text):
            if   s == "(" : count += 1
            elif s == ")": count -= 1
            if count == 0 and i > 1: return i
        return 
 
    """
    Takes in a text and convert it into a category tree. 
    input is in such format:
    "Animals ( Reptiles Birds ( Eagles Pigeons Crows ) )"
    """
    def treeParser(self, text):
        root = treeNode(text.pop(0))
        text.pop(0)
        text.pop()
        while text:
            if len(text) == 1 or text[1] != "(":
                root.child.append(treeNode(text.pop(0)))
                continue
            nextParenthesePos = self.findNextMatchParen(text)
            root.child.append(self.treeParser(text[:nextParenthesePos + 1]))
            text = text[nextParenthesePos+1:]
        return root
    
    """
    Find the node that has the category name same as the label. 
    """
    def findNode(self, root, label):
        if root.category == label:
            return root
        for child in root.child:
            node =  self.findNode(child, label)
            if node: return node
        return None
    
    """
    Recursive function to traverse all nodes under the root 
    that starts with the query. 
    """
    def queryAnswerCount(self, root, answer, count):
        if root.prefixTreeNode.startsWith(answer):
            count += 1
        for child in root.child:
            count += self.queryAnswerCount(child, answer, 0)
        return count
    
    """
    Input all answers into the correspondent category's prefix tree. 
    """
    def inputAnswer(self, answer):
        answer = answer.split(":")
        category = answer.pop(0)
        categoryNode = self.findNode(self.root, category)
        answer = answer.pop(0).strip()
        if categoryNode:
            categoryNode.prefixTreeNode.insert(answer)
        return
    
    """
    Returns the answer count for each query.
    """
    def countAnswer(self, query):
        query = query.split(" ", 1)
        categoryNode = self.findNode(self.root, query.pop(0))
        return self.queryAnswerCount(categoryNode, query.pop(0), 0)

        
#Test based on the given test cases.
#run command :
#python Ontology.py
ct = CategoryTree("Animals ( Reptiles Birds ( Eagles Pigeons Crows ) )")
ct.inputAnswer("Reptiles: Why are many reptiles green?")
ct.inputAnswer("Birds: How do birds fly?")
ct.inputAnswer("Eagles: How endangered are eagles?")
ct.inputAnswer("Pigeons: Where in the world are pigeons most densely populated?")
ct.inputAnswer("Eagles: Where do most eagles live?")
    
print ct.countAnswer("Eagles How en")
print ct.countAnswer("Birds Where")
print ct.countAnswer("Reptiles Why do")
print ct.countAnswer("Animals Wh")
