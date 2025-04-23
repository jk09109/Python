#!/usr/bin/env python
# coding: utf-8

# In[40]:


#사용자 정의 함수부
def display_multiplication_table(start, end):
    i=1
    while i<=9:
        for j in range (start, end+1):
            print(f'{j} x {i} = {j * i:2d}', end='\t')
        i+=1
        print()
    print()

#주 프로그램부
display_multiplication_table(2, 5)
display_multiplication_table(6, 9)


# In[ ]:




