# 引入TKINTER套件，並且重新命名為tk
import tkinter as tk 

#變數 有區域變數 跟 全域變數
OP = "N"  # N + - X /
numStr = "0"
firstNum = 0
secondNum =0
totalNum = 0
# 
def numShow(num):#把7指定給num這個變數
    global numStr
    if(len(numStr)==1 and numStr=="0"):
        numStr = num
    else:
        numStr = numStr + num
    numLabel['text'] = numStr
   
def AC():
    global numStr
    global firstNum
    global secondNum
    global totalNum
    global op
    op="N"
    numStr = "0"
    firstNum = "0"
    secondNum = "0"
    totalNum = "0"
    numLabel['text'] = numStr

def opFunction(opStr):
    global firstNum
    global numStr
    global OP
    OP= opStr
    firstNum = int(numStr)#把String轉成int狀態再指定給firstNum
    numStr = "0"
    numLabel['text'] = numStr

def equalFunction ():
    global secondNum 
    global numStr
    secondNum = int(numStr)

    if(OP=="+"):
        total = firstNum + secondNum
    elif(OP == "-"):
        total = firstNum - secondNum
    elif(OP == "x"):
        total = firstNum * secondNum    
    elif(OP == "/"):
        total = firstNum / secondNum
    else:
        print("沒有按下加減乘除")
            


    numLabel['text'] = str(total)#把int轉成string狀態再指定給numLabel['text'] 


# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
window.title("計算機")
window.geometry("600x600")# 應用程式大小
window.maxsize(400,600)    #最大值
window.configure(background='black')

#frame的初始設定
top_frame = tk.Frame(window)
numXX_frame = tk.Frame(window)
number7_frame = tk.Frame(window)
number4_frame= tk.Frame(window)
number1_frame = tk.Frame(window)
numberAC_frame = tk.Frame(window)

#frame的顯示，最先寫的語法最優先
top_frame.pack()

number7_frame.pack()
number4_frame.pack()
number1_frame.pack()
numberAC_frame.pack()


# LABEL
numLabel =tk.Label(top_frame, text="0",font=("Arial",36),bg='black', fg='orange')
# button的初始設定
btn7 = tk.Button(number7_frame, text='7',font=("Arial",22),width = 4,height=1, fg='red',command=lambda: numShow("7"))
btn8 = tk.Button(number7_frame, text='8',font=("Arial",22),width = 4,height=1, fg='red',command=lambda: numShow("8"))
btn9 = tk.Button(number7_frame, text='9',font=("Arial",22),width = 4,height=1, fg='red',command=lambda: numShow("9"))
btnPlus = tk.Button(number7_frame, text='+',font=("Arial",22),width = 4,height=1, fg='red',command = lambda : opFunction("+") )
btn4 = tk.Button(number4_frame, text='4',font=("Arial",22),width = 4,height=1,  fg='red',command=lambda: numShow("4") )
btn5 = tk.Button(number4_frame, text='5', font=("Arial",22),width = 4,height=1,fg='red',command=lambda: numShow("5") )
btn6 = tk.Button(number4_frame, text='6', font=("Arial",22),width = 4,height=1, fg='red',command=lambda: numShow("6") )
btnMinus = tk.Button(number4_frame, text='-',font=("Arial",22),width = 4,height=1,  fg='red',command = lambda : opFunction("-") )
btn1 = tk.Button(number1_frame, text='1',font=("Arial",22),width = 4,height=1,  fg='red',command=lambda: numShow("1") )
btn2 = tk.Button(number1_frame, text='2',font=("Arial",22),width = 4,height=1,  fg='red',command=lambda: numShow("2") )
btn3 = tk.Button(number1_frame, text='3',font=("Arial",22),width = 4,height=1, fg='red',command=lambda: numShow("3") )
btnMutilple = tk.Button(number1_frame, text='x',font=("Arial",22),width = 4,height=1,  fg='red',command = lambda : opFunction("x") )
btnAC = tk.Button(numberAC_frame, text='AC', font=("Arial",22),width = 4,height=1, fg='red',command=lambda: AC() ) 
btn0 = tk.Button(numberAC_frame, text='0', font=("Arial",22),width = 4,height=1, fg='red',command=lambda: numShow("0") ) 
btnDivide = tk.Button(numberAC_frame, text='÷',font=("Arial",22),width = 4,height=1, fg='red',command = lambda : opFunction("/") ) 
btnEqual = tk.Button(numberAC_frame, text='=',font=("Arial",22),width = 4,height=1,  fg='red', command = lambda : equalFunction() ) 

#LABEL
numLabel.pack()
#button在frame中的顯示
btn7.pack(side=tk.LEFT)
btn8.pack(side=tk.LEFT)
btn9.pack(side=tk.LEFT)
btnPlus.pack(side=tk.LEFT)
btn4.pack(side=tk.LEFT)
btn5.pack(side=tk.LEFT)
btn6.pack(side=tk.LEFT)
btnMinus.pack(side=tk.LEFT)
btn1.pack(side=tk.LEFT)
btn2.pack(side=tk.LEFT)
btn3.pack(side=tk.LEFT)
btnMutilple.pack(side=tk.LEFT)
btnAC.pack(side=tk.LEFT)
btn0.pack(side=tk.LEFT)
btnEqual.pack(side=tk.LEFT)
btnDivide.pack(side=tk.LEFT)


# 運行主程式
window.mainloop()