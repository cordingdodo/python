#입금, 출금, 잔액 조회가 가능한 은행 계좌 관리 프로그램을 작성하여라
#잔액(balance), 입출금액(money), 계좌번호(idNum), 계좌주(idName)
#입금기능(deposit), 출금기능(withdraw), 잔액조회(getBalance)
#클래스의 멤버를 선언하여 작동할 수 있도록 할 것

class account:
    money=int(0)
    balance=int(0)
    def deposit(self, money):
        account.balance+=money
        print("입금되었습니다")
        return
    def withdraw(self, money):
        account.balance-=money
        print("출금되었습니다")
        return

    def getBalance(self):
        print("현재 잔액: ", account.balance)

        num = 0
        print("-------------------------------")
        print("1. 입금, 2. 출금, 3.잔액 조회")
        print("-------------------------------")

        num = int(input("선택>")
        if (num == 1):
            account.deposit
            break

        elif (num == 2):
             account.withdraw
             break

        else (num == 3):
             account.getBalance
             break
