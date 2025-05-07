#!/usr/bin/env python
# coding: utf-8

# In[10]:


shopping_bag={}

print('[구입]')
while True:
    item=input('상품명?')
    if item=='':
        break
    #shopping_bag.append(item)
    count=int(input('수량은?'))
    print(f'장바구니에 {item} {count}개가 담겼습니다.\n')
    shopping_bag[item]=count

print(f'\n>>>장바구니 보기: {shopping_bag}')

print('\n[검색]')
check=input('장바구니에서 확인하고자 하는 상품은?')
print(f'{check}은(는) {shopping_bag.get(check)}개 담겨 있습니다.')

