def add_element(lst, element):
    lst.append(element)
    
def double_elements(lst):
    for i in range(len(lst)):
        lst[i]=lst[i]*2
    

l=[1,2,3]
add_element(l,4)
print(l)
double_element(l)
print(l)


