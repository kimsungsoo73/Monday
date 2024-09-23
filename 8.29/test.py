# test.py

# 문제 1. 홍길동, 34, True 키보드 입력, 나이는 숫자
def name():
    data = input('이름을 입력하시오>>> ')
    print(f'이름 : {data}')
    return data

def age():
    while True:
        num = int(input('나이를 입력하세요>>> '))
        if num < 20 and num > 70:
            if num < 20:
                print(f'{num}살, 청소년')
                print('잘못 입력하셨습니다.')
            elif num > 70:
                print(f'{num}살, 노년')
                print('잘못 입력하셨습니다.')
        if num >= 20 and num < 30:
            print(f'{num}살, 청년')
        elif num >= 30 and num < 66:
            print(f'{num}살, 중년')
        elif num >= 66 and num < 71:
            print(f'{num}살, 노년')
            break
        return num

def gender():
    gen = input('성별을 입력하세요>>> ')
    if gen == 'M':
        print('남자, True')
    elif gen != 'M':
        print('여자, False')
    return gen
print(name(), age(), gender())


