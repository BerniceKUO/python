#
# bingo game
#

import random

SIZE = 25
# 產生數列 1~25
nums = [ i+1 for i in range(SIZE) ]
table = [ '*' for i in range(SIZE)]

# 產生答案表
answer = random.sample(nums, SIZE)

def showAnswer():
    # 顯示答案結果
    for i in range(1, SIZE+1):
        thisNum = answer[i-1]

        # 如果數字小於10 多加一個空白
        if thisNum < 10:
            string = " "+str(thisNum)
        else:
            string = str(thisNum)
        
        print( string+" ", end="")
        if i%5 == 0:
            print("\n")


#showAnswer()

def showTable():
    # 顯示表格
    for i in range(1, SIZE+1):
        print(table[i-1]+" ", end="")
        if i%5==0:
            print("\n")


# 賓果遊戲從這裡開始 start
# 猜測的次數
count = 0 

while count < 25:
    
    #showAnswer()
    # 輸入數字
    now_number = int(input("請輸入數字: "))
    #if now_number >=1 and now_number <=25:    
    #else:
    #    print("範圍有誤!")
    #    continue
    
    # 查表
    mark = 0

    for i in range(1, SIZE+1):
        if now_number == answer[i-1]:
            mark = i-1
            break
    # 將mark的位置改成數字
    table[mark] = str(now_number)

    showTable()

    if table[0] != '*' and table[1] != '*' and table[2] != '*' and table[3] != '*' and table[4] != '*':
        print("BINGO!!!")
    elif table[5] != '*' and table[6] != '*' and table[7] != '*' and table[8] != '*' and table[9] != '*':
        print("BINGO!!!")
    elif table[10] != '*' and table[11] != '*' and table[12] != '*' and table[13] != '*' and table[14] != '*':
        print("BINGO!!!")
    elif table[15] != '*' and table[16] != '*' and table[17] != '*' and table[18] != '*' and table[19] != '*':
        print("BINGO!!!")
    elif table[20] != '*' and table[21] != '*' and table[22] != '*' and table[23] != '*' and table[24] != '*':
        print("BINGO!!!")
    elif table[0] != '*' and table[5] != '*' and table[10] != '*' and table[15] != '*' and table[20] != '*':
        print("BINGO!!!")
    elif table[1] != '*' and table[6] != '*' and table[11] != '*' and table[16] != '*' and table[21] != '*':
        print("BINGO!!!")
    elif table[2] != '*' and table[7] != '*' and table[12] != '*' and table[17] != '*' and table[22] != '*':
        print("BINGO!!!")
    elif table[3] != '*' and table[8] != '*' and table[13] != '*' and table[18] != '*' and table[23] != '*':
        print("BINGO!!!")
    elif table[4] != '*' and table[9] != '*' and table[14] != '*' and table[19] != '*' and table[24] != '*':
        print("BINGO!!!")
        
    elif table[0] != '*' and table[6] != '*' and table[12] != '*' and table[18] != '*' and table[24] != '*':
        print("BINGO!!!")
    elif table[4] != '*' and table[8] != '*' and table[12] != '*' and table[16] != '*' and table[20] != '*':
        print("BINGO!!!")
    
    count += 1
