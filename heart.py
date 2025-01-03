import math
from turtle import *

def kalp_a(k):
    return 16 * math.sin(k)**3  

def kalp_b(k):
    return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)            
bgcolor('black')    
color('#ff3487')   

penup()              
for i in range(1000):  
    x = kalp_a(math.radians(i)) * 20
    y = kalp_b(math.radians(i)) * 20
    goto(x, y)      
    pendown()       

done()
