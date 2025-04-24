from random import randint

#사용자 정의 함수부
def roll_dice():
    return randint(1,6)

def main():
    print(roll_dice())
    print(roll_dice())
    print(roll_dice())
    print(roll_dice())
    print(roll_dice())

#주 프로그램부
if __name__ == '__main__':
    main()
