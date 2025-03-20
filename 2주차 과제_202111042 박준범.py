#!/usr/bin/env python
# coding: utf-8

# In[4]:


#함수 정의부
def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(r):
    calc=3.14*r*r
    return calc


#주 프로그램부
rad=get_radius('넓이를 구하고자 하는 원의 반지름은? ')
result=get_circle_area(rad)
print('반지름 ', rad,'인 원의 넓이 = 3.14 x ', rad, ' x ', rad, ' = ', result, sep='')


# In[ ]:




