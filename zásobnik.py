# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:38:31 2018

@author: škola
"""

class stack:    
    
    def __init__(self):
        self._stack = []
        
    def push (self,item):
        self._stack.append(item)
        
    def pop (self):
        if len(self._stack)>0:
            c= self._stack[len(self._stack)-1]
            del self._stack[len(self._stack)-1]
            return c
        else:
            return False
        
    def peek(self):
        if len(self._stack)>0:
            return self._stack[len(self._stack)-1]
        else:
            return False
    
    def is_empty(self):
        if len(self._stack)==0:
            return True
        else:
            return False
        
        
    def size(self):
        return (len(self._stack))
        

def breaker(text):
    operator = stack()
    output = []
    cislo = ""
    
    for i in text:     
        
        if i == "*" or i == "/" or i == "(" :
            if len(cislo) > 0 :
                output.append(int(cislo))
                cislo = ""
            operator.push(i)            
            
        elif ord(i) >= 48 and ord(i) <= 57 :
            cislo = cislo + str(i)
            
        elif i == ")" :
            if len(cislo) > 0:
                output.append(int(cislo))
                cislo = ""
            last = operator.pop()
            while last != "(" :
                output.append(last)
                last = operator.pop()
                
                
        elif i == "+" or i ==  "-" :
            if len(cislo) > 0 :
                output.append(int(cislo))
                cislo = ""             
            if operator.is_empty() is False:
                last = operator.peek()
                while last == "*" or last == "/" :
                    output.append(last)
                    operator.pop()
                    last = operator.pop()
                operator.push(i)
            else:
                operator.push(i)
    
    if len(cislo) > 0:
        output.append(int(cislo))
                
    while operator.is_empty() is False:
        output.append(operator.pop())
    
    return output

def counter(btext):
    operants = stack()
    for i in btext:
        
        if i == "*" or i == "/" or i == "+" or i == "-":
            b = operants.pop()
            a = operants.pop()
            if i == "*" :
                c = a * b
            elif i == "/" :
                c = a / b
            elif i == "+" :
                c = a + b
            elif i == "-" :
                c = a - b
            operants.push(c)
        else:
            operants.push(i)
    return(operants.pop())

txt = open ( 'problems.txt' , 'r' )
file=txt.read().split("\n")
txt.close()
results=[]
for problem in file:
    
    results.append(str(counter(breaker(problem))))
    
file="\n".join(results)
txt = open ( "results.txt" , "w" )
txt.write(file)
txt.close()
