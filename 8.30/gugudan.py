#함수 4개 사용
# 시작 진입 호출 main
# 출력시 1초단위로 출력
import time

def create():
    title = '구구단 시작하겠습니다.'
    print(title)

def guguinput(): 
    try:        
        dan = int(input('숫자입력 >>> '))
    except Exception as ex:
         print('에러이유',ex)
    return dan

def guguouput(dan):
    for i in range(1,10):
        print(f'{dan} * {i} = {dan*i}')
        time.sleep(1)
    
     
def main():
    # create()
    data = guguinput()
    guguouput(data)
print(main())