import numpy as np
import pandas as pd
import neurokit2 as nk
import json

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        children.append(child)


    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def print_tree(self):
        spaces ='   '* self.get_level() * 3
        prefix=spaces+'|__' if self.parent else''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def build_tree():
        root = TreeNode("Test")

        Versuchperson = TreeNode("Versuchsperson")
        Versuchperson.add_child(TreeNode('Testergebnis'))

        root.add_child(Versuchperson)

        return root

    if __name__=='__main__':
        root= build_tree()
        print(root.get_level())
        root.print_tree()
        pass
