#!/usr/bin/env python
# coding: utf-8

# In[8]:


#사용자 정의 함수부
def buy(bag):
    print('[구입]')
    item=input('상품명?')
    if item=='':
        return False
    count=int(input('수량은?'))
    print(f'장바구니에 {item} {count}개가 담겼습니다.\n')
    bag[item]=count
    return True

def show(bag):
    print(f'\n>>>장바구니 보기: {bag}')
    
def find(bag):
    print('\n[검색]')
    check=input('장바구니에서 확인하고자 하는 상품은?')
    if check in bag:
        print(f'{check}은(는) {bag[check]}개 담겨 있습니다.')
    else: 
        print(f'장바구니에 {check}은(는) 없습니다.')
    
#주 프로그램부
shopping_bag={}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)


# In[ ]:




