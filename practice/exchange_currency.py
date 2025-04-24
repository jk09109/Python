exchange_rate=0

def set_rate(rate):
    global exchange_rate
    exchange_rate = rate

def get_rate():
    return exchange_rate

def to_dollar(won):
    return won / exchange_rate

def to_won(dollar):
    return dollar * exchange_rate

def main():
    print('### 환율 변환 모듈 테스트 ###')

    set_rate(1010)

    print('오늘의 환율', get_rate())
    print('2020 원 =', to_dollar(2020), '달러')
    print('2 달러 =', to_won(2), '원')

if __name__=='__main__':
    main()
