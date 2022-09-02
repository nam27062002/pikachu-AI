from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time
browser  = webdriver.Chrome(executable_path="./chromedriver")
browser.maximize_window()
browser.get("https://www.pikachuonline.com/")
time.sleep(2)
ifame = browser.find_element(By.ID,"fullscreen")
browser.switch_to.frame(ifame)
listPikachu = browser.find_elements(By.XPATH,'//img[@border="1"]')
listscrPikachu = []
listscrNewPikachu = []
for i in listPikachu:
    listscrPikachu.append(str(i.get_attribute("src")))
listscrNewPikachu = set(listscrPikachu)
listscrNewPikachu = list(listscrNewPikachu)
arrayPikachu = []
for i in range(9):
    arrayPikachu.append([])
    for j in range(16):
        arrayPikachu[i].append(-1)
for i,value in enumerate(listscrPikachu):
    arrayPikachu[i%9][int(i/9)] = listscrNewPikachu.index(value)
def dir(pos):
    data = [0,0,0,0]
    count = [1,1,1,1]

    if pos[0] == 0:
        data[0] = 100
    else:
        while arrayPikachu[pos[0] - count[0]][pos[1]] == -1:
            count[0] += 1
            if (pos[0] - count[0] < 0):
                data[0] = 100
                break

    if pos[1] == 15:
        data[1] = 100
    else:
        while arrayPikachu[pos[0]][pos[1] + count[1]] == -1:
            count[1] += 1
            if (pos[1] + count[1]) > 15:
                data[1] = 100
                break

    if pos[0] == 8:
        data[2] = 100
    else:
        while arrayPikachu[pos[0] + count[2]][pos[1]] == -1:
            count[2] += 1
            if pos[0] + count[2] > 8:
                data[2] = 100
                break

    if pos[1] == 0:
        data[3] = 100
    else:
        while arrayPikachu[pos[0]][pos[1] - count[3]] == -1:
            count[3] += 1
            if pos[1] - count[3] < 0:
                data[3] = 100
                break
    for i in range(4):
        if data[i] <= count[i] - 1:
            data[i] = count[i] - 1
    return data
def threeLine(pos1,pos2):
    a = dir(pos1)
    b = dir(pos2)
    for i in range(len(a)):
        if a[i] == b[i] and a[i] == 100:
            return True
    return False
def PosAllPikachu(pos):
    list = []
    for i in range(9):
        for j in range(16):
            if arrayPikachu[i][j] == arrayPikachu[pos[0]][pos[1]]:
                if i == pos[0] and j == pos[1]:
                    pass
                else:
                    list.append([i,j])
    return list

def checkX(x1,x2,y):
    for i in range(x1,x2+1,1):
        if arrayPikachu[y][i] != -1:
            return False
    return True
def checkY(y1,y2,x):
    for i in range(y1,y2+1,1):
        if arrayPikachu[i][x] != -1:
            return False
    return True
def checkTowLine(pos1,pos2):
    x1 = pos1[1]
    y1 = pos1[0]
    x2 = pos2[1]
    y2 = pos2[0]
    if y2 > y1:
        if x2 > x1:
            if checkY(y1+1,y2,x1) == True and checkX(x1,x2-1,y2) == True:
                return True
            if checkX(x1+1,x2,y1) == True and checkY(y1,y2-1,x2) == True:
                return True
        if x2 < x1:
            if checkY(y1+1,y2,x1) == True and checkX(x2+1,x1,y2) == True:
                return True
            if checkX(x2,x1-1,y1) == True and checkY(y1,y2-1,x2) == True:
                return True
    return False
def ThreeLineX(pos1,pos2):
    x1 = pos1[1]
    y1 = pos1[0]
    x2 = pos2[1]
    y2 = pos2[0]
    if (x1 < x2):
        if (y1 < y2):
            for i in range(x1+1,x2,1):
                if checkX(x1+1,i,y1) == True and checkX(i,x2-1,y2) == True and checkY(y1,y2,i) == True:
                    return True
    if (x1 > x2):
        if y1 < y2:
            for i in range(x2+1,x1,1):
                if checkX(x2+1,i,y2) == True and checkX(i,x1-1,y1) == True and checkY(y1,y2,i) == True:
                    return True
    return False
def ThreeLineY(pos1,pos2):
    x1 = pos1[1]
    y1 = pos1[0]
    x2 = pos2[1]
    y2 = pos2[0]
    if  y1 < y2:
        if x1 < x2:
            for i in range(y1+1,y2,1):
                if checkY(y1+1,i,x1) == True and checkY(i,y2-1,x2) == True and checkX(x1,x2,i) == True:
                    return True
        else:
            for i in range(y1+1,y2,1):
                if checkY(y1+1,i,x1) == True and checkY(i,y2-1,x2) == True and checkX(x2,x1,i) == True:
                    return True
    return False
def metVclX(pos1,pos2):
    x1 = pos1[1]
    y1 = pos1[0]
    x2 = pos2[1]
    y2 = pos2[0]
    if y1 < y2:
        m = min(x1,x2)
        n = max(x1,x2)
        for i in range(16):
            if checkY(y1,y2,i) == True:
                if i < m:
                    if checkX(i,x1-1,y1) == True and checkX(i,x2-1,y2) == True:
                        return True
                elif i > n:
                    if checkX(x1+1,i,y1) == True and checkX(x2+1,i,y2) == True:
                        return True
    return False
def metVclY(pos1,pos2):
    x1 = pos1[1]
    y1 = pos1[0]
    x2 = pos2[1]
    y2 = pos2[0]
    if x1 < x2:
        m = min(y1,y2)
        n = max(y1,y2)
        for i in range(8):
            if checkX(x1,x2,i) == True:
                if i < m:
                    if checkY(i,y1-1,x1) == True and checkY(i,y2 - 1,x2) == True:
                        return True
                elif i > n:
                    if checkY(y1+1,i,x1) == True and checkY(y2+1,i,x2) == True:
                        return True
    return False
check = True
click = 0
def AI(pos):
    global check,arrayPikachu,click
    check = False
    if arrayPikachu[pos[0]][pos[1]] != -1:
        list = PosAllPikachu(pos)
        for i in list:
            check = threeLine(pos,i)
            if check == False:
                if pos[0] == i[0]: 
                    if pos[1] < i[1]:
                        check = checkX(pos[1] + 1,i[1]-1,pos[0])
                    else:
                        check = checkX(i[1] + 1,pos[1]-1,pos[0])
            if check == False:
                if pos[1] == i[1]: 
                    if pos[0] < i[0]:
                        check = checkY(pos[0] + 1,i[0] - 1,pos[1])
                    else:
                        check = checkY(i[0]+1,pos[0] -1,pos[1])
            if check == False:
                check = checkTowLine(pos,i)
            if check == False:
                check = ThreeLineX(pos,i)
            if check == False:
                check = ThreeLineY(pos,i)
            if check == False:
                check = metVclX(pos,i)
            if check == False:
                check = metVclY(pos,i)
            if check == True:
                try:
                    listPikachu[pos[0] + 9*pos[1]].click()
                    listPikachu[i[0] + 9*i[1]].click()
                    click += 2
                    arrayPikachu[pos[0]][pos[1]] = -1
                    arrayPikachu[i[0]][i[1]] = -1
                except:
                    pass
count = 1
t = 0
running = False
while click < 144:
    while count !=0:
        if running == False:
            t = time.time()
            running = True
        count = 0
        for i in range(9):
            for j in range(16):
                AI([i,j])
                if check == True:
                    count +=1
    if (click != 144):
        time.sleep(0.1)
        a = browser.switch_to.alert
        a.accept()
        time.sleep(0.1)
        listPikachu.clear()
        listscrPikachu.clear()
        listscrNewPikachu.clear()
        listPikachu = browser.find_elements(By.XPATH,'//img[@border="1"]')
        for i in listPikachu:
            listscrPikachu.append(str(i.get_attribute("src")))
        listscrNewPikachu = set(listscrPikachu)
        listscrNewPikachu = list(listscrNewPikachu)
        for i,value in enumerate(listscrPikachu):
            if arrayPikachu[i%9][int(i/9)] != -1:
                arrayPikachu[i%9][int(i/9)] = listscrNewPikachu.index(value)
        count = 1
print("Time: ",round(time.time() - t,2),"s")