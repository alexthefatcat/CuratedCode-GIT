# -*- coding: utf-8 -*-
"""Created on Tue Dec 10 10:01:02 2019@author: Alexm"""

################################################################

range1 = lambda x:range(1,x+1)

################################################################

def once_every_loop(div_by, number=None,start=0,shift=0):
    """ True once over the loop
        useful printing every 1000
    """
    if number is None:
        return lambda x: once_every_loop(div_by, x,start=start,shift=shift)
    a,rem = divmod(number,div_by) 
    if a>=start:
       return rem % div_by == shift
    return False

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
once_every_1000 = once_every_loop(1000,start=1)

for n in range(3000):
    if once_every_1000(n):
        print(n)
        
once_every_1000 = once_every_loop(1000)

for n in range1(3000):
    if once_every_1000(n):
        print(n)

#################################################################  

def sort_list_by_other_list(lis1,lis2):
    return [x for _,x in sorted(zip(lis2,lis1),key=lambda x:x[0])]
 
def sort_by_index(lis1,lis2):
    return [lis1[ind] for ind in lis2]
             
#################################################################          

def string_limit(string,length,fillchar=" ",how="right"):
    if how in ["r","right"]:
       return str(string).ljust(length,fillchar=fillchar)[:length]
    if how in ["l","left"]:
       return str(string).rjust(length,fillchar=fillchar)[length:]

if __name__ == "__main__":
    string_limit("abcde",8) 
    string_limit("abcdefghijklmnopqrstuv",8)           
        
#################################################################           
        
        
        
        
        
        
        
        