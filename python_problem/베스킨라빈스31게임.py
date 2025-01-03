from random import randint

""" 예외처리 """
class NotValidNumber(Exception):
    def __init__(self):
        super().__init__("1과 3사이의 정수가 아닙니다.")
""" num입력 """
def Input_num(x):
    while(True):
        try:
            x = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if(x not in [1,2,3]):
                raise NotValidNumber
        except ValueError:
            print("정수를 입력하세요")
            continue
        except NotValidNumber as E:
            print(E)
            continue
        else :
            return x
""" num을 받고 그걸 통해 출력 """
def player_declare(num,baskin,status):
    for i in range(num):
        baskin +=1
        if(status == True):
            print("player:",baskin)
        else:
            print("Computer:",baskin)
        if(baskin == 31):
            return baskin
    return baskin
""" 우승자 출력 """
def printWinner(status):    
    if(status == False):
        print("Computer win!")
    else:
        print("Player win!")
""" 게임 전체 코드 """
def brGame():

    num = 0
    baskin = 0
    status = True

    while(baskin <31):
        if(status == True): #플레이어 1의 차례
            num = Input_num(num)
            baskin = player_declare(num,baskin,status)
            status = not status
        else: #플레이어 2의 차례
            num = randint(1,3)
            baskin = player_declare(num,baskin,status)
            status = not status
    printWinner(status)
    
brGame()
