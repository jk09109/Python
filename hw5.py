#!/usr/bin/env python
# coding: utf-8

# In[22]:


#사용자 정의 함수부
def read_single_digit(one):
    if one==0: print('영', end=' ')
    elif one==1: print('일', end=' ')
    elif one==2: print('이', end=' ')
    elif one==3: print('삼', end=' ')
    elif one==4: print('사', end=' ')
    elif one==5: print('오', end=' ')
    elif one==6: print('육', end=' ')
    elif one==7: print('칠', end=' ')
    elif one==8: print('팔', end=' ')
    elif one==9: print('구', end=' ')
    
def read_number(num):
    if 0<=num<10:
        read_single_digit(num)
    elif 10<=num<100:
        t=num//10
        o=num%10
        read_single_digit(t)
        read_single_digit(o)
    elif 100<=num<1000:
        h=num//100
        t=(num%100)//10
        o=num%10
        read_single_digit(h)
        read_single_digit(t)
        read_single_digit(o)

#주 프로그램부
num=int(input('세자리 정수 입력'))
read_number(num)


# In[ ]:




