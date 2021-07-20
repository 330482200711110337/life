import time
import os
def helper_dairy():
    a=input("读日记扣d,写日记扣x")
    if a=='d':
        reader()
    if a=='x':
        write_dairy()


#TODO write in txt
def dairy_bag():
    if not os.path.exists("C:/dairy/"):
        os.mkdir("C:/dairy/")

def write_dairy():
    date = time.strftime('%Y-%m-%d', time.localtime(time.time())).split('-')
    file_name=''
    for i in date:
        file_name+=i
    seconds = 1514736000 - time.time()
    days = seconds//(60*60*24)

    print("Today is: ",date ,",there`s",int(days),"days left in 2020")
    print("请输入你的日记，可以输入多行，我将以txt的形式保存为日期，",
          "目录为“C:/dairy/”，如果想停止，请输入:'end'，同一天的日记将保存在一个文件")
    fd = open("C:/dairy/"+file_name+".txt",'a')
    while True:
        line = input()
        if line == 'end':
            break
        fd.write(line+'\n')
    fd.close()

    print("今天的日记号是",end='')
    for i in date:
        print(i,end='')

#TODO read txt
def reader():
    x=input("请输入你要访问的日记号，如20210701之类。")
    with open("C:/dairy/"+x+".txt",'r') as f:
        for line in f:
            print(line)

