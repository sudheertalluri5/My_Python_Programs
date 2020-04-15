# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:40:40 2019

@author: sudhe
"""

class First:
    no="first"
    def first(self):
        print("first")
        return
    def alter(self):
        print(self.no)
        return
    def try_(self,obj):
        print(obj.first())
        return
firstobj=First()
print(firstobj.alter())
print(firstobj.first())
secondobj=First()
print(firstobj.try_(secondobj))