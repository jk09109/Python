#!/usr/bin/env python
# coding: utf-8

# In[8]:


#사용자 정의 함수부
def get_integer(prompt):
    res = int(input(prompt))
    return res;

def exchange(amount):
    n500=amount//500
    amount %= 500
    n100=amount//100
    amount %= 100
    n50=amount // 50
    amount %= 50
    n10=amount // 10

    print('500원 동전의 개수:',n500)
    print('100원 동전의 개수:',n100)
    print('50원 동전의 개수:',n50)
    print('10원 동전의 개수:',n10)
    

#주 프로그램부
n=get_integer('동전으로 교환하고자 하는 금액은? ')  
exchange(n) 


# In[ ]:




