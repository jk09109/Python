#!/usr/bin/env python
# coding: utf-8

# In[11]:


sale_rate=0

def get_fixed_price(price):
    global sale_rate
    BeforeSale=price/(1-sale_rate/100)
    
    return int(BeforeSale)


#주 프로그램부
sale_rate=int(input('할인율은?'))

Aprice=int(input('A 상품의 할인된 가격은?'))
Bprice=int(input('B 상품의 할인된 가격은?'))

print('A 상품의 정가는', get_fixed_price(Aprice), '원')
print('B 상품의 정가는', get_fixed_price(Bprice), '원')

