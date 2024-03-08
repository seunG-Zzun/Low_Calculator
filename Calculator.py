import tkinter as tk

window = tk.Tk()
window.title('Calculator')
new_num = 0 #(글로벌) 입력변수
result_num = 0 #(글로벌) 최종수
operate = 0 #(글로벌) 이전 연산자 저장

#(1.11)결과값/버튼 구분 프레임
output_entry = tk.Entry(window, font=('Arial', 16), bg='black', fg='white', justify='right', bd=10)
input_frame = tk.Frame(window, height = 400, bg = 'black')
output_entry.grid(row = 0, column = 0, sticky = 'ew')
input_frame.grid(row = 1, column = 0, sticky = 'nsew')


def button_click(value): #버튼이벤트
    if value == 'AC': #초기화 버튼
        clear_all()
    else:
        try:
            value = int(value)
            number_click(value)
        except:
            operator_click(value)

def clear_all(): #초기화 버튼 함수
    output_entry.delete(0, tk.END)
    global new_num, result_num, operate
    new_num = 0
    result_num = 0
    operate = ''

def number_click(value): #숫자 클릭 함수
    current = output_entry.get()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, str(current) + str(value))

def operator_click(value): #연산자 클릭 함수
    global new_num, result_num, operate
    current_num = float(output_entry.get())

    if value in {'+', '-', '*', '/'}: # 등호 연산자 제외 연산자 
        if operate and operate != '=':
            result_num = eval(f'{result_num} {operate} {current_num}') # eval -> 문자열 수식 판단(1.15)
        else:
            result_num = current_num
        new_num = current_num
        operate = value
        output_entry.delete(0, tk.END)
    elif value == '%': ##(1.17)
        result_num = 0.01 * current_num
        output_entry.delete(0, tk.END)
        output_entry.insert(0, result_num)
    elif value == '+/-':
        result_num = -1 * current_num
        output_entry.delete(0, tk.END)
        output_entry.insert(0, result_num)
    elif value == '=':
        if operate:
            result_num = eval(f'{result_num} {operate} {current_num}')
            if result_num % 1 == 0: #소수점이하 0일때는 정수출력을 위해 코드 추가 ex) 0.05 + 3은 소수점이하 0이 아니라 3.05 출력, 3+5 는 0이라 8 출력
                result_num = int(result_num)
            output_entry.delete(0, tk.END)
            output_entry.insert(0, result_num)
            operate = '='
    else:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, str(current_num) + str(value))

#버튼 배치       
buttons = [] ##(1.12)
buttons_code = [['AC', '+/-', '%', '/'], ['7', '8', '9', '*'], ['4', '5', '6', '-'], ['1', '2', '3', '+'], ['', '0', '', '=']]
for i in range(5):
    row_buttons = []
    for j in range(4):
        button_text = buttons_code[i][j]
        button = tk.Button(input_frame, text=button_text, width=8, height=3, command=lambda value=button_text: button_click(value))
        button.grid(row=i+1, column=j, padx=5, pady=5, sticky = 'nsew')
        if i == 4 and j == 0:
            button.config(state=tk.DISABLED)
        if i == 4 and j == 2:
            button.config(state=tk.DISABLED)    

        row_buttons.append(button)
    buttons.append(row_buttons)
#버튼색 지정 연산자:orange, 숫자:grey, AC:white 
for i in range(5):
    for j in range(4):
        if i == 0 and j > 0 or j == 3:
            buttons[i][j]['bg'] = 'orange'
        else: buttons[i][j]['bg'] = 'grey'
buttons[0][0]['bg'] = 'white'


window.mainloop()

##실패 참고..
# import tkinter as tk

# window = tk.Tk()
# window.title('Calculator')
# operator = {'AC':0, '+':1, '-':2, 'x':3, '/':4, '+/-':5, '%':6,'.':7, '=':8}  #(글로벌) 연산자
# new_num = 0 #(글로벌) 입력변수
# garbage_num = 0 #(글로벌) 입력수 임시 저장 변수
# operate = 0 #(글로벌) 이전 연산자 저장
# #결과값/버튼 구분 프레임

# str_value = tk.StringVar()
# str_value.set(str(new_num))
# output_entry = tk.Entry(window, textvariable = str_value, font=('Arial', 16), bg='black', fg='white', justify='right', bd=10)
# input_frame = tk.Frame(window, height = 400, bg = 'black')
# output_entry.grid(row = 0, column = 0, sticky = 'ew')
# input_frame.grid(row = 1, column = 0, sticky = 'nsew')

# def number_click(value):
#     global new_num
#     new_num = (new_num * 10) + value #숫자 연속입력위해,,,
#     str_value.set(new_num)

# def operator_click(value): ##단일 연산자는 가능한데 연산자가 여러개 될경우 계산이 안됨..
#     global new_num, garbage_num, operate, operator
#     op = operator[value]

#     if op == 0: # AC
#         new_num = 0
#         garbage_num = 0
#         operate = 0
#         str_value.set(str(new_num))
#     elif new_num == 0: #현재 화면 값 0일때
#         operate = 0
#     elif operate == 0:
#         operate = op
#         garbage_num = new_num
#         new_num = 0
#         str_value.set(str(new_num))

#     elif op == 8:
#         if operate == 1:
#             new_num = garbage_num + new_num
#         if operate == 2:
#             new_num = garbage_num - new_num
#         if operate == 3:
#             new_num = garbage_num * new_num
#         if operate == 4:
#             new_num = garbage_num / new_num
        
#         str_value.set(str(new_num))
#         new_num = 0
#         garbage_num = 0
#         operate = 0
#     else:
#         new_num = 0
#         garbage_num = 0
#         operate = 0
#         str_value.set(str(new_num))




# def button_click(value):
#     try:
#         value = int(value)
#         number_click(value)
#     except:
#         operator_click(value)

# buttons = []
# buttons_code = [['AC', '+/-', '%', '/'], ['7', '8', '9', 'x'], ['4', '5', '6', '-'], ['1', '2', '3', '+'], ['', '0', '', '=']]
# for i in range(5):
#     row_buttons = []
#     for j in range(4):
#         button_text = buttons_code[i][j]
#         button = tk.Button(input_frame, text=button_text, width=8, height=3, command=lambda value=button_text: button_click(value))
#         button.grid(row=i+1, column=j, padx=5, pady=5, sticky = 'nsew')
#         if i == 4 and j == 0:
#             button.config(state=tk.DISABLED)

#         row_buttons.append(button)
#     buttons.append(row_buttons)
# #버튼색 지정 연산자:orange, 숫자:grey, AC:white 
# for i in range(5):
#     for j in range(4):
#         if i == 0 and j > 0 or j == 3:
#             buttons[i][j]['bg'] = 'orange'
#         else: buttons[i][j]['bg'] = 'grey'
# buttons[0][0]['bg'] = 'white'


# window.mainloop()