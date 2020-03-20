#-----------------(1)變數宣告、變數型態、運算元---------------------------
print('HelloWorld')

a=123
b='456'
c=8.7

type(a)
print(type(a))
print(type(b))
print(type(c))
d=5
e=-2

print(a+d)
print(a/d) #數學除法
print(a//d)#無條件捨去除法
print(a**d)#a的b次方
print(abs(e)) #絕對值
print(max(a,c,d)) #最大值
print(min(a,e)) #最小值
print(a+int(b))
#------------------(2)使用者輸入-----------------------------

name=input()
print('name =',name)

#------------------(3)if-else 邏輯判斷式---------------------------

battery=50
if battery>80:
    print('電量充足')
elif battery<30:
    print('快沒電')
else:
    print('即將沒電')

#--------------------(4)for loop 迴圈---------------------------

for i in range(10): #印出0到n-1的數字
    print(i)
    #range 的結構是：range(起點, 終點, 間距)，
    #其中的間距預設為1 、比如 range(0, 6) = range(0, 6, 1) 。
    # 代表從 0 到 5，每次加 1 的意思。

for i in range(1,10):
    for j in  range(1,10):
        print(i*j,end='')
    print(end='\n')

for i in range(1,10,2):
    print(i)

#------------------(5)猜數字--------------------------------------

ans=45

for guesschance in range(0,3):
    try:
        guess=int(input())
        if(ans==guess):
            print('bingo')
            break
        else:
            print('wrong')
    except ValueError:
        print("It's not an integer!!")
print('game over')
#------------------(6)list--------------------------------------
#list如同櫃子可以放任何東西，
#會用一個數字代表放在第幾格櫃子，
#這個數字叫做index(索引)。
a=['eric',174.0,61,True]

len(a)      #len(a)代表list a的長度
for i in range(0,len(a)):  #印出a[0]至a[3]中的值
    print(a[i])

#不同的寫法但有相同結果
for i in a:
    print(i)

#現在有一個 list a = [1, 3, 5, 7, 9]，
#請對每一個元素都平方後印出來，
#且須將 a 也變成 [1, 9, 25, 49, 81]。
a=[1,3,5,7,9]
for i in range(0,len(a)):
    print(a[i]*a[i])
    a[i]=a[i]*a[i]
print(a)

#list.append(x): 把變數x塞到list的最後面
#list.insert(i, x): 把變數x塞到i這個位置上
#list.pop(): 把list的最後一格丟掉
#list.pop(i): 把list的第i格丟掉
#list.remove(x): 會把第一個出現的變數x拿掉
#list.clear(): 把list內的資料全部清光光
#max(list): 找出list中最大值
#min(list): 找出list中最小值
#sum(list): 找出list數字總和

baller=['kobe','leborn','curry','durant']
baller.append('irving')  #irving為選秀會上第五順位
baller.insert(0,'jordan') #增加喬丹在第一順位
baller.pop()#球場上只能有五個人，最後一個人只能下場
baller.pop(2) #leborn受傷下場
baller.remove('curry') #第一個curry被驅逐出場
#baller.clear() #比賽結束球員下場
#list[start: end]，start和end都可以省略不寫
#start的預設為0
#end的預設為len(list)
print(baller[0:5])  #['kobe', 'leborn', 'curry', 'durant', 'irving']

#------------------(7)Dict一個靠標籤能查到的東西--------------------------------------
#dict由大括號{}包住，元入以key:value的key-value pair組成(key後面階冒號和變數value)，並以由逗點,隔開
d={123:'Snoopy','cat':['Pusheen',"kitty"]}
print(len(d)) #只看key的數量
#dict在輸出時並不保證key的順序。
d={'one':1,'two':2,'three':3}
print(d)
print(len(d))  #len(dict)找出dict的大小
#當取到不存在的key時，相對於list中的index error，dict會顯示key error
#語法
dict={1:'w'} #建立空得dict
del dict[1]  #刪除特定的key-value
dict[2]='www' #新增或更新 如果key不存在，會增加這組K-V；如果key已存在，會更新這組K-V。
#for...in 例子
d={'one':1,'two':2,'three':3}
target =2
for key in d:
    if d[key] == target:
        print('find it key =',key)
        break
    else:
        print('try again')

#檢查dict的內容

d={'one':1,'two':2,'three':3,'four':4}
print('one' in d)   #true
print(1 in d)   #false
print(0 in d.keys())    #false
print(1 in d.values())  #true
print('one' in d.keys())    #true
print('9' in d.keys())  #false
#d[key]:這個做法相對不安全，key如果不存在的話就會出現KeyError
print(d['one']) #true
#d.get(key, default_value): 是比較安全的作法，如果key不存在的話就會回傳
print(d.get('one','找不到'))   #1
print(d.get(1,'找不到'))   #找不到

print(','.join(baller))
