#PARAM CHANGER IMPORTS
import msilib
from msilib.schema import Error
import re
import os
import subprocess
import time
#INTERFACE IMPORTS
import datetime
from tkinter import *
import tkinter as tk
import PIL
from PIL import ImageTk,Image
from tkinter import filedialog,messagebox,ttk
import tkinter.font as tkFont

#GLOBAL VARIABLES
index=0
terminal_index=0
menu_auxiliar=["OP0","OP1","OP2","OP3","OP4","OP5","OP6","OP7","OP8","OP9","OP10","OP11","OP12","OP13","OP14","OP15","OP16","OP17","OP18","OP19","OP20","OP21","OP22","OP23",
            "OP24","OP25","OP26","OP27","OP28","OP29","OP30","OP31","OP32","OP33","OP34","OP35","OP36"]
message_to_send="Enter the parameter's value. Example: \"ENABLED\""
max_AR_lenght=len("This is a test to verify the action required")
terminal_history=["---------------------------------------------Welcome to HDMT Parameter Changer---------------------------------------------------s"
                  ]
menu_modules=[]
#INTERFACE FUNCTIONS----------------------------------------------------------------------------
#MENU BUTTON FUNCTIONS
def send_clicked():
    nummodules=AR_textbox.get()
    aux=get_modules()
    listModulesDef = getDefModules(aux,nummodules)
    write_to_terminal()
    AR_textbox.delete(0,END)
    print("LIST MODULE DEF-----------------------------------------",listModulesDef)

def arrow_clicked_0():
    print("Button Clicked 0") 
    values=get_menu_values()
    print("Label=",values[0][0]) 
    print("Value=",values[1][0]) 
    clear_textbox()
def arrow_clicked_1():
    print("Button Clicked 1")
    values=get_menu_values()
    print("Label=",values[0][1]) 
    print("Value=",values[1][1]) 
    clear_textbox()
def arrow_clicked_2():
    print("Button Clicked 2")
    values=get_menu_values()
    print("Label=",values[0][2]) 
    print("Value=",values[1][2]) 
    clear_textbox()
def arrow_clicked_3():
    print("Button Clicked 3")
    values=get_menu_values()
    print("Label=",values[0][3]) 
    print("Value=",values[1][3]) 
    clear_textbox()
def arrow_clicked_4():
    print("Button Clicked 4")
    values=get_menu_values()
    print("Label=",values[0][4]) 
    print("Value=",values[1][4]) 
    clear_textbox()
def arrow_clicked_5():
    print("Button Clicked 5")
    values=get_menu_values()
    print("Label=",values[0][5]) 
    print("Value=",values[1][5])
    clear_textbox()
def arrow_clicked_6():
    print("Button Clicked 6")
    values=get_menu_values()
    print("Label=",values[0][6]) 
    print("Value=",values[1][6]) 
    clear_textbox()
def arrow_clicked_7():
    print("Button Clicked 7")
    values=get_menu_values()
    print("Label=",values[0][7]) 
    print("Value=",values[1][7])
    clear_textbox()
def arrow_clicked_8():
    print("Button Clicked 8")
    values=get_menu_values()
    print("Label=",values[0][8]) 
    print("Value=",values[1][8]) 
    clear_textbox()
def arrow_clicked_9():
    print("Button Clicked 9")
    values=get_menu_values()
    print("Label=",values[0][9]) 
    print("Value=",values[1][9])
    clear_textbox() 
def arrow_clicked_10():
    print("Button Clicked 10")
    values=get_menu_values()
    print("Label=",values[0][10]) 
    print("Value=",values[1][10]) 
    clear_textbox()
def arrow_clicked_11():
    print("Button Clicked 11")
    values=get_menu_values()
    print("Label=",values[0][11]) 
    print("Value=",values[1][11])
    clear_textbox() 
def arrow_clicked_12():
    values=get_menu_values()
    print("Label=",values[0][12]) 
    print("Value=",values[1][12]) 
    clear_textbox()

def clock():
    now = datetime.datetime.now()
    hour=now.hour
    minutes=now.minute
    seconds=now.second
    year=now.year
    month=now.month
    day=now.day
    if(hour<10):
        hour="0"+str(hour)
    else:hour=str(hour)
    if(minutes<10):
        minutes="0"+str(minutes)
    else:minutes=str(minutes)
    if(seconds<10):
        seconds="0"+str(seconds)
    else:seconds=str(seconds)
    if(day<10):
        day="0"+str(day)
    else:day=str(day)
    if(month<10):
        month="0"+str(month)
    else:month=str(month)
    Hour.config(text=hour+":"+minutes+":"+seconds)
    #Date.config(text=month)
    Hour.after(1000,clock)

def write_to_menu():
    global index
    global menu_auxiliar
    can_show=True
    for i in range(len(menu_auxiliar)):
        if(index+i > 12):
            can_show=False
            break
        else: continue
    if(len(menu_auxiliar)<12):
        can_show=False
    if(can_show):
        arrow0_label.config(text=menu_auxiliar[index])
        arrow1_label.config(text=menu_auxiliar[index+1])
        arrow2_label.config(text=menu_auxiliar[index+2])
        arrow3_label.config(text=menu_auxiliar[index+3])
        arrow4_label.config(text=menu_auxiliar[index+4])
        arrow5_label.config(text=menu_auxiliar[index+5])
        arrow6_label.config(text=menu_auxiliar[index+6])
        arrow7_label.config(text=menu_auxiliar[index+7])
        arrow8_label.config(text=menu_auxiliar[index+8])
        arrow9_label.config(text=menu_auxiliar[index+9])
        arrow10_label.config(text=menu_auxiliar[index+10])
        arrow11_label.config(text=menu_auxiliar[index+11])
        arrow12_label.config(text=menu_auxiliar[index+12])
    else:
        list_aux=[]
        for i in range(index,len(menu_auxiliar)):
            list_aux.append(menu_auxiliar[i])
        while(len(list_aux)<13):
            list_aux.append("")
        arrow0_label.config(text=list_aux[0])
        arrow1_label.config(text=list_aux[1])
        arrow2_label.config(text=list_aux[2])
        arrow3_label.config(text=list_aux[3])
        arrow4_label.config(text=list_aux[4])
        arrow5_label.config(text=list_aux[5])
        arrow6_label.config(text=list_aux[6])
        arrow7_label.config(text=list_aux[7])
        arrow8_label.config(text=list_aux[8])
        arrow9_label.config(text=list_aux[9])
        arrow10_label.config(text=list_aux[10])
        arrow11_label.config(text=list_aux[11])
        arrow12_label.config(text=list_aux[12])

def scroll_menu_down():
    global index
    global menu_auxiliar
    if(index+12>=len(menu_auxiliar)):
        index=index
    else:index=index+12
    write_to_menu()

def scroll_menu_up():
    global index
    global menu_auxiliar
    if(index-12<0):
        index=index
    else:index=index-12
    write_to_menu()

def write_to_terminal():
    global terminal_index
    global terminal_history
    can_show=True
    for i in range(len(terminal_history)):
        if(terminal_index+i > 23):
            can_show=False
            break
        else: continue
    if(len(terminal_history)<23):
        can_show=False
    if(can_show):
        Terminal_label_0.config(text=menu_auxiliar[terminal_index])
        Terminal_label_1.config(text=menu_auxiliar[terminal_index+1])
        Terminal_label_2.config(text=menu_auxiliar[terminal_index+2])
        Terminal_label_3.config(text=menu_auxiliar[terminal_index+3])
        Terminal_label_4.config(text=menu_auxiliar[terminal_index+4])
        Terminal_label_5.config(text=menu_auxiliar[terminal_index+5])
        Terminal_label_6.config(text=menu_auxiliar[terminal_index+6])
        Terminal_label_7.config(text=menu_auxiliar[terminal_index+7])
        Terminal_label_8.config(text=menu_auxiliar[terminal_index+8])
        Terminal_label_9.config(text=menu_auxiliar[terminal_index+9])
        Terminal_label_10.config(text=menu_auxiliar[terminal_index+10])
        Terminal_label_11.config(text=menu_auxiliar[terminal_index+11])
        Terminal_label_12.config(text=menu_auxiliar[terminal_index+12])
        Terminal_label_13.config(text=menu_auxiliar[terminal_index+13])
        Terminal_label_14.config(text=menu_auxiliar[terminal_index+14])
        Terminal_label_15.config(text=menu_auxiliar[terminal_index+15])
        Terminal_label_16.config(text=menu_auxiliar[terminal_index+16])
        Terminal_label_17.config(text=menu_auxiliar[terminal_index+17])
        Terminal_label_18.config(text=menu_auxiliar[terminal_index+18])
        Terminal_label_19.config(text=menu_auxiliar[terminal_index+19])
        Terminal_label_20.config(text=menu_auxiliar[terminal_index+20])
        Terminal_label_21.config(text=menu_auxiliar[terminal_index+21])
        Terminal_label_22.config(text=menu_auxiliar[terminal_index+22])
        Terminal_label_23.config(text=menu_auxiliar[terminal_index+23])
        
    else:
        list_aux=[]
        for i in range(terminal_index,len(terminal_history)):
            list_aux.append(terminal_history[i])
        while(len(list_aux)<24):
            list_aux.append("")
        Terminal_label_0.config(text=list_aux[0])
        Terminal_label_1.config(text=list_aux[1])
        Terminal_label_2.config(text=list_aux[2])
        Terminal_label_3.config(text=list_aux[3])
        Terminal_label_4.config(text=list_aux[4])
        Terminal_label_5.config(text=list_aux[5])
        Terminal_label_6.config(text=list_aux[6])
        Terminal_label_7.config(text=list_aux[7])
        Terminal_label_8.config(text=list_aux[8])
        Terminal_label_9.config(text=list_aux[9])
        Terminal_label_10.config(text=list_aux[10])
        Terminal_label_11.config(text=list_aux[11])
        Terminal_label_12.config(text=list_aux[12])
        Terminal_label_13.config(text=list_aux[13])
        Terminal_label_14.config(text=list_aux[14])
        Terminal_label_15.config(text=list_aux[15])
        Terminal_label_16.config(text=list_aux[16])
        Terminal_label_17.config(text=list_aux[17])
        Terminal_label_18.config(text=list_aux[18])
        Terminal_label_19.config(text=list_aux[19])
        Terminal_label_20.config(text=list_aux[20])
        Terminal_label_21.config(text=list_aux[21])
        Terminal_label_22.config(text=list_aux[22])
        Terminal_label_23.config(text=list_aux[23])

def scroll_terminal_down():
    global terminal_index
    global terminal_history
    if(terminal_index+23>=len(terminal_history)):
        terminal_index=terminal_index
    else:terminal_index=terminal_index+23
    write_to_terminal()

def scroll_terminal_up():
    global terminal_index
    global terminal_history
    if(terminal_index-23<0):
        terminal_index=terminal_index
    else:terminal_index=terminal_index-23
    write_to_terminal()

def split_string():
    global str1_aux
    global new_message_to_show
    if(len(message_to_send)>max_AR_lenght*3):
        str_1="CANNOT DISPLAY LONG INSTRUCTION"
        str_2=""
        return str_1,str_2
    if(len(message_to_send)<=max_AR_lenght*2 and len(message_to_send)>max_AR_lenght): #USES 2 LABELS
        ''' function to split string by closest space'''
        mid_point = int(len(message_to_send)/3)+10
        if message_to_send[mid_point]==' ':
            # the middle point is a space
            str_1 = message_to_send[:mid_point]
            str_2 = message_to_send[mid_point+1:]
            return str_1, str_2


        for i in range(1,mid_point):
            # the middle point is a character
            if message_to_send[mid_point-i] == ' ':
                break_point = mid_point-i
                break

            if message_to_send[mid_point+i] == ' ':
                break_point = mid_point+i
                break

        str_1 = message_to_send[:break_point]
        str_2 = message_to_send[break_point+1:]
        str1_aux=str_1
        new_message_to_show=str_2
        return str_1, str_2

    elif(len(message_to_send)<max_AR_lenght+1): #USES 1 LABELS
        str_1=message_to_send
        str_2=""
        return str_1,str_2
    else: #USES 3 LABELS
        str_1="CANNOT DISPLAY LONG INSTRUCTION"
        str_2=""
        return str_1,str_2

def write_to_action_required():
    tuple=split_string()
    msg1=tuple[0]
    msg2=tuple[1]
    action_required_label1.config(text=msg1)
    action_required_label2.config(text=msg2)

def get_menu_values():
    labels=[]
    values=[]
    labels.append(arrow0_label.cget("text"))
    labels.append(arrow1_label.cget("text"))
    labels.append(arrow2_label.cget("text"))
    labels.append(arrow3_label.cget("text"))
    labels.append(arrow4_label.cget("text"))
    labels.append(arrow5_label.cget("text"))
    labels.append(arrow6_label.cget("text"))
    labels.append(arrow7_label.cget("text"))
    labels.append(arrow8_label.cget("text"))
    labels.append(arrow9_label.cget("text"))
    labels.append(arrow10_label.cget("text"))
    labels.append(arrow11_label.cget("text"))
    labels.append(arrow12_label.cget("text"))
    values.append(arrow0_textbox.get())
    values.append(arrow1_textbox.get())
    values.append(arrow2_textbox.get())
    values.append(arrow3_textbox.get())
    values.append(arrow4_textbox.get())
    values.append(arrow5_textbox.get())
    values.append(arrow6_textbox.get())
    values.append(arrow7_textbox.get())
    values.append(arrow8_textbox.get())
    values.append(arrow9_textbox.get())
    values.append(arrow10_textbox.get())
    values.append(arrow11_textbox.get())
    values.append(arrow12_textbox.get())
    list_aux=[]
    list_aux.append(labels)
    list_aux.append(values)
    return list_aux

def textbox_activator(status):
    arrow0_textbox.config(state=status)
    arrow1_textbox.config(state=status)
    arrow2_textbox.config(state=status)
    arrow3_textbox.config(state=status)
    arrow4_textbox.config(state=status)
    arrow5_textbox.config(state=status)
    arrow6_textbox.config(state=status)
    arrow7_textbox.config(state=status)
    arrow8_textbox.config(state=status)
    arrow9_textbox.config(state=status)
    arrow10_textbox.config(state=status)
    arrow11_textbox.config(state=status)
    arrow12_textbox.config(state=status)

def clear_textbox():
    arrow0_textbox.delete(0,END)
    arrow1_textbox.delete(0,END)
    arrow2_textbox.delete(0,END)
    arrow3_textbox.delete(0,END)
    arrow4_textbox.delete(0,END)
    arrow5_textbox.delete(0,END)
    arrow6_textbox.delete(0,END)
    arrow7_textbox.delete(0,END)
    arrow8_textbox.delete(0,END)
    arrow9_textbox.delete(0,END)
    arrow10_textbox.delete(0,END)
    arrow11_textbox.delete(0,END)
    arrow12_textbox.delete(0,END)

def get_now_time():
    now = datetime.datetime.now()
    hour=now.hour
    minutes=now.minute
    seconds=now.second
    year=now.year
    month=now.month
    day=now.day
    if(hour<10):
        hour="0"+str(hour)
    else:hour=str(hour)
    if(minutes<10):
        minutes="0"+str(minutes)
    else:minutes=str(minutes)
    if(seconds<10):
        seconds="0"+str(seconds)
    else:seconds=str(seconds)

    Hour=hour+":"+minutes+":"+seconds
    Date=str(month)+"/"+str(day)+"/"+str(year)
    Terminal_hour="["+Date+"]"+"["+Hour+"]"+"  "
    return Terminal_hour

#PARAM CHANGER FUNCTIONS----------------------------------------------------------------------------
def get_modules():
    global menu_modules
    while 1:
        # Getting TP path
        getPath = os.popen('%HDMTTOS%\Runtime\Release\SingleScriptCmd.exe getTPRoot').read()
        TP_path = getPath.split('TP root path: ')[-1].strip()
        TP_path = TP_path+"\\Modules"
        
        newmodules = []
        try:
            modules = os.listdir(TP_path)
        except OSError:
            '''resp=input("No TP loaded. Try again? (y/n)\n") #FALTA
            if resp == "n":
                exit()'''
            msg_box = tk.messagebox.askquestion('No TP loaded.', 'No TP loaded. Try again?',
                                        icon='warning')
            if msg_box == 'yes':
                get_modules()
            else:
                tk.messagebox.showinfo('Exiting program.', 'Bye!')
                return window.destroy()
        else:       
            menu_modules=[]
            num = 0
            for module in modules:
                #print(str(num) + ") " + module)
                menu_modules.append(str(num) + ") " + module)
                module = TP_path+"\\"+module+"\\"+module+".mtpl"
                num += 1
                newmodules.append(module)
            break
    return newmodules
    
def getDefModules(newmodules,nummodules):
    while 1:
        listModulesDef = []
        try:
            listMod = nummodules.split(",")
            print("You selected:")
            terminal_history.append("You selected:")
            write_to_terminal()
            for ind in listMod:
                print(str(ind)+") "+newmodules[int(ind)])
                print(newmodules[int(ind)])
                terminal_history.append(str(ind)+") "+newmodules[int(ind)])
                terminal_history.append(newmodules[int(ind)])
                write_to_terminal()
                listModulesDef.append(newmodules[int(ind)])
        except ValueError:
            if(nummodules == "all"):
                terminal_history.append("You selected all the modules")
                write_to_terminal()
                print("You selected all the modules")
                listModulesDef = newmodules
                break
            elif nummodules == "exit":
                terminal_history.append("Exiting program.")
                write_to_terminal()
                exit()
            else:
                terminal_history.append("Error, Invalid value, please try again! (Input with comma separated)")
                write_to_terminal()
                print("Error, Invalid value, please try again! (Input with comma separated)")
        else:
            terminal_history.append("Success")
            write_to_terminal()
            print("Success")
            break
        write_to_terminal()
    return listModulesDef

def runCmd(run_cmd,log):
    log.write(run_cmd +"\n")
    try:
        output = os.popen(run_cmd).read()
        print(str(output))
        log.write(str(output)+"\n")
    except Exception as e:
        print(e)
        log.write(str(e)+"\n")


#----------------------------------------------------------------------------------INTERFACE--------------------------------------------------------------------------------
#Main Window
window = tk.Tk()
window.title("Parameter Changer") #TITLE
window.pack_propagate(False) #DONT LET WIDGETS RESIZE THE WINDOW
window.geometry("1045x615")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 615,
    width = 1045,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.pack(fill="both",expand=True)

img0 = PhotoImage(file = f"./img0.png")
background = tk.Label(window, image=img0)
background.place(x = 0, y = 0,width = 1045,height = 615)

#HOUR LABEL
now = datetime.datetime.now()
Hour=ttk.Label(window,text=str(now.hour)+":"+str(now.minute)+":"+str(now.second),background="white",foreground="black",font=('Inter', 10,'bold'))
Hour.place(x=980, y=20)
Date=ttk.Label(window,text=str(now.month)+"/"+str(now.day)+"/"+str(now.year),background="white",foreground="black",font=('Inter', 10,'bold'))
Date.place(x=975,y=1)
#DATE LABEL
clock()

#Command TextBox
base_y=100
base_x=122
width_textbox=22
font_size=9
highlight_thickness=1
AR_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
AR_textbox.place(x=base_x,y=base_y)

#OPTIONS TEXTBOX
base_y=144
base_x=225
delta=32
width_textbox=14
font_size=9
highlight_thickness=1
arrow0_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow0_textbox.place(x=base_x,y=base_y+delta*0)
arrow1_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow1_textbox.place(x=base_x,y=base_y+delta*1)
arrow2_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow2_textbox.place(x=base_x,y=base_y+delta*2)
arrow3_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow3_textbox.place(x=base_x,y=base_y+delta*3)
arrow4_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow4_textbox.place(x=base_x,y=base_y+delta*4)
arrow5_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow5_textbox.place(x=base_x,y=base_y+delta*5)
arrow6_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow6_textbox.place(x=base_x,y=base_y+delta*6)
arrow7_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow7_textbox.place(x=base_x,y=base_y+delta*7)
arrow8_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow8_textbox.place(x=base_x,y=base_y+delta*8)
arrow9_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow9_textbox.place(x=base_x,y=base_y+delta*9)
arrow10_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow10_textbox.place(x=base_x,y=base_y+delta*10)
arrow11_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow11_textbox.place(x=base_x,y=base_y+delta*11)
arrow12_textbox=tk.Entry(window,width=width_textbox,bg = "#d9d9d9",font=('Inter', font_size),highlightthickness = highlight_thickness)
arrow12_textbox.place(x=base_x,y=base_y+delta*12)
#textbox_activator("disabled")

#SEND BUTTON
img1 = PhotoImage(file = f"./img1.png")
send_command = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = send_clicked,relief = "flat")
send_command.place(x = 290, y = 104,width = 68,height = 20)

#SCROLL BUTTONS
img2 = PhotoImage(file = f"./img3.png")
scroll_up = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = scroll_menu_up,relief = "flat")
scroll_up.place(x = 189, y = 571,width = 176,height = 29)

img3 = PhotoImage(file = f"./img2.png")
scroll_down = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = scroll_menu_down,relief = "flat")
scroll_down.place(x = 13, y = 570,width = 176,height = 30)

#MENU BUTTONS
base_y=142
base_x=330
delta=32
width_button=26
height_button=24
img4 = PhotoImage(file = f"./img4.png")
arrow0 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_0,relief = "flat")#BUTTON 0
arrow0.place(x = base_x, y = base_y+delta*0, width = width_button, height = height_button)
arrow1 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_1,relief = "flat")#BUTTON 1
arrow1.place(x = base_x, y = base_y+delta*1, width = width_button, height = height_button)
arrow2 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_2,relief = "flat")#BUTTON 2
arrow2.place(x = base_x, y = base_y+delta*2, width = width_button, height = height_button)
arrow3 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_3,relief = "flat")#BUTTON 3
arrow3.place(x = base_x, y = base_y+delta*3, width = width_button, height = height_button)
arrow4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_4,relief = "flat")#BUTTON 4
arrow4.place(x = base_x, y = base_y+delta*4, width = width_button, height = height_button)
arrow5 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_5,relief = "flat")#BUTTON 5
arrow5.place(x = base_x, y = base_y+delta*5, width = width_button, height = height_button)
arrow6 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_6,relief = "flat")#BUTTON 6
arrow6.place(x = base_x, y = base_y+delta*6, width = width_button, height = height_button)
arrow7 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_7,relief = "flat")#BUTTON 7
arrow7.place(x = base_x, y = base_y+delta*7, width = width_button, height = height_button)
arrow8 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_8,relief = "flat")#BUTTON 8
arrow8.place(x = base_x, y = base_y+delta*8, width = width_button, height = height_button)
arrow9 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_9,relief = "flat")#BUTTON 9
arrow9.place(x = base_x, y = base_y+delta*9, width = width_button, height = height_button)
arrow10 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_10,relief = "flat")#BUTTON 10
arrow10.place(x = base_x, y = base_y+delta*10, width = width_button, height = height_button)
arrow11 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_11,relief = "flat")#BUTTON 11
arrow11.place(x = base_x, y = base_y+delta*11, width = width_button, height = height_button)
arrow12 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = arrow_clicked_12,relief = "flat")#BUTTON 11
arrow12.place(x = base_x, y = base_y+delta*12, width = width_button, height = height_button)

#ACTION REQUIRED LABELS
base_y=53
base_x=120
delta=20
font_size=10
action_required_label1=ttk.Label(window,text="This is a test to verify the action required",background="white",foreground="black",font=('Inter', font_size)) #AR LABEL
action_required_label1.place(x = base_x, y = base_y)
action_required_label2=ttk.Label(window,text="This is a test to verify the action required",background="white",foreground="black",font=('Inter', font_size)) #AR LABEL
action_required_label2.place(x = base_x, y = base_y+delta)
write_to_action_required()

#TABLE LABELS
base_y=144
base_x=18
delta=32
font_size=9
arrow0_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow0_label.place(x = base_x, y = base_y+delta*0)
arrow1_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow1_label.place(x = base_x, y = base_y+delta*1)
arrow2_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow2_label.place(x = base_x, y = base_y+delta*2)
arrow3_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow3_label.place(x = base_x, y = base_y+delta*3)
arrow4_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow4_label.place(x = base_x, y = base_y+delta*4)
arrow5_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow5_label.place(x = base_x, y = base_y+delta*5)
arrow6_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow6_label.place(x = base_x, y = base_y+delta*6)
arrow7_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow7_label.place(x = base_x, y = base_y+delta*7)
arrow8_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow8_label.place(x = base_x, y = base_y+delta*8)
arrow9_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow9_label.place(x = base_x, y = base_y+delta*9)
arrow10_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow10_label.place(x = base_x, y = base_y+delta*10)
arrow11_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow11_label.place(x = base_x, y = base_y+delta*11)
arrow12_label=ttk.Label(window,text="Here comes one option.",background="#D9D9D9",foreground="black",font=('Inter', font_size,'bold')) #TERMINAL LABEL
arrow12_label.place(x = base_x, y = base_y+delta*12)

#TERMINAL LABELS
base_y=100
base_x=400
delta=20
font_size=9
Terminal_label_0=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_0.place(x = base_x, y = base_y+delta*0)
Terminal_label_1=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_1.place(x = base_x, y = base_y+delta*1)
Terminal_label_2=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_2.place(x = base_x, y = base_y+delta*2)
Terminal_label_3=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_3.place(x = base_x, y = base_y+delta*3)
Terminal_label_4=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_4.place(x = base_x, y = base_y+delta*4)
Terminal_label_5=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_5.place(x = base_x, y = base_y+delta*5)
Terminal_label_6=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_6.place(x = base_x, y = base_y+delta*6)
Terminal_label_7=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_7.place(x = base_x, y = base_y+delta*7)
Terminal_label_8=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_8.place(x = base_x, y = base_y+delta*8)
Terminal_label_9=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_9.place(x = base_x, y = base_y+delta*9)
Terminal_label_10=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_10.place(x = base_x, y = base_y+delta*10)
Terminal_label_11=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_11.place(x = base_x, y = base_y+delta*11)
Terminal_label_12=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_12.place(x = base_x, y = base_y+delta*12)
Terminal_label_13=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_13.place(x = base_x, y = base_y+delta*13)
Terminal_label_14=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_14.place(x = base_x, y = base_y+delta*14)
Terminal_label_15=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_15.place(x = base_x, y = base_y+delta*15)
Terminal_label_16=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_16.place(x = base_x, y = base_y+delta*16)
Terminal_label_17=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_17.place(x = base_x, y = base_y+delta*17)
Terminal_label_18=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_18.place(x = base_x, y = base_y+delta*18)
Terminal_label_19=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_19.place(x = base_x, y = base_y+delta*19)
Terminal_label_20=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_20.place(x = base_x, y = base_y+delta*20)
Terminal_label_21=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_21.place(x = base_x, y = base_y+delta*21)
Terminal_label_22=ttk.Label(window,text="Here comes termminal.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_22.place(x = base_x, y = base_y+delta*22)
Terminal_label_23=ttk.Label(window,text="Here comes termminal23.",background="#252850",foreground="white",font=('Inter', font_size,'bold')) #TERMINAL LABEL
Terminal_label_23.place(x = base_x, y = base_y+delta*23)

#TERMINAL SCROLLS
#SCROLL BUTTONS
base_x=995
base_y=85
delta=485
img5 = PhotoImage(file = f"./img5.png")
terminal_scroll_up = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = scroll_terminal_up,relief = "flat")
terminal_scroll_up.place(x = base_x, y = base_y,width = 20,height = 18)

img6 = PhotoImage(file = f"./img6.png")
terminal_scroll_down = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = scroll_terminal_down,relief = "flat")
terminal_scroll_down.place(x = base_x, y = base_y+delta,width = 20,height = 20)

window.resizable(False, False)
#-------------------------------------------------------------------------AFTER ALL WINDOW IS GENERATED--------------------------------------------
#Creating logs Folder with date included in name
date = "D"+str(time.strftime("%x")).replace("/","")+"H"+str(time.strftime("%X")).replace(":","")
dir = "ParamChangerLogs"
try:
    os.mkdir(dir)
except OSError:
    terminal_history.append(get_now_time()+"Failed to create Dir %s " % dir + ": Folder already exists")
    write_to_terminal()
    print("Failed to create Dir %s " % dir + ": Folder already exists\n")
else:
    terminal_history.append(get_now_time()+"Dir created: %s " % dir)
    write_to_terminal()
    print("Dir created: %s " % dir)

listModulesDef = get_modules()
menu_auxiliar=menu_modules
message_to_send="Enter the modules you want or the word all for all the modules or exitt"
write_to_menu()
write_to_action_required()

window.mainloop()
#----------------------------------------------------------------------------------EOF INTERFACE--------------------------------------------------------------------------------