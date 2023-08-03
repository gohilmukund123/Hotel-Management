from tkinter import *
import datetime as dt
from tkinter.ttk import Combobox

root=Tk()
root.geometry("570x600")
root.title("Hotel Navgraha")
root.resizable(False,False)
date = dt.datetime.now()

def print_bill():
    Label(root,text="Printing the bill. Please wait...",font=("aria",20,"bold"),fg="black").place(x=90,y=520)

def reset():
    entry_dosa.delete(0,END)
    entry_paneer_tikka.delete(0,END)
    entry_aloo_sabji.delete(0,END)
    entry_butter_roti.delete(0,END)
    entry_butter_naan.delete(0,END)
    entry_cold_drink.delete(0,END)

def total():
    try: a1=int(dosa.get())
    except: a1=0
    try: a2=int(paneer_tikka.get())
    except: a2=0
    try: a3=int(aloo_sabji.get())
    except: a3=0
    try: a4=int(butter_roti.get())
    except: a4=0
    try: a5=int(butter_naan.get())
    except: a5=0
    try: a6=int(cold_drink.get())
    except: a6=0
    #cost of item per quantity
    c1=60*a1
    c2=130*a2
    c3=90*a3
    c4=50*a4
    c5=75*a5
    c6=20*a6
    lbl_total=Label(f3,font=("aria",19,"bold"),text="Total",width=5,fg="black")
    lbl_total.grid(row=9,column=0)
    entry_total=Entry(f3,font=("aria",18,"bold"),textvariable=total_bill,width=12,fg="black")
    entry_total.grid(row=9,column=1)
    total_cost=c1+c2+c3+c4+c5+c6
    string_bill=("Rs.",str('%.2f' %total_cost))
    total_bill.set(string_bill)
    
#menu card
f1=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=250,height=325)
f1.place(x=10,y=10)
Label(f1,text="Menu",font=("Gabriola",30,"bold"),fg="black",bg="lightgreen").place(x=15,y=0)
Label(f1,font=("calibri",15,"bold"),text="Dosa..........Rs.60/plate",fg="black",bg="lightgreen").place(x=15,y=70)
Label(f1,font=("calibri",15,"bold"),text="Paneer Tikka..Rs.130/plate",fg="black",bg="lightgreen").place(x=15,y=100)
Label(f1,font=("calibri",15,"bold"),text="Aloo Sabji....Rs.90/plate",fg="black",bg="lightgreen").place(x=15,y=130)
Label(f1,font=("calibri",15,"bold"),text="Butter Roti...Rs.50/plate",fg="black",bg="lightgreen").place(x=15,y=160)
Label(f1,font=("calibri",15,"bold"),text="Butter Naan...Rs.75/plate",fg="black",bg="lightgreen").place(x=15,y=190)
Label(f1,font=("calibri",15,"bold"),text="Cold Drink....Rs.20/drink",fg="black",bg="lightgreen").place(x=15,y=220)

#table and customer details
f2=Frame(root,bg="lightblue",highlightbackground="black",highlightthickness=1,width=250,height=325)
f2.place(x=10,y=350)
table_number = StringVar()
lbl_det=Label(f2,font=("Gabriola",27,"bold"),text="Customer",width=7,fg="black",bg="lightblue")
lbl_det.grid(row=1,column=0)
lbl_space=Label(f2,font=("Gabriola",27,"bold"),text="Details",width=7,fg="black",bg="lightblue")
lbl_space.grid(row=1,column=1)

lbl_date=Label(f2,font=("aria",11),text="Date",width=9,fg="black",bg="lightblue")
lbl_date.grid(row=2,column=0)
label = Label(f2,text=f"{date:%B %d, %Y}",font=("aria, 10"),bg="lightblue",fg="black")
label.grid(row=2,column=1)

lbl_table_number=Label(f2,font=("aria",10),text="Table Number",width=16,fg="black",bg="lightblue")
lbl_table_number.grid(row=3,column=0)
#entry_table_number=Entry(f2,font=("aria",10,"bold"),textvariable=table_number,width=10,bg="lightblue",fg="black",bd=3)
#entry_table_number.grid(row=3,column=1)

n = StringVar()
chooseTableNum=Combobox(f2,font=("aria",10,"bold"),textvariable=n,width=10,background="lightblue")
chooseTableNum['values']=('1','2','3','4','5','6','7','8','9','10')
chooseTableNum.grid(row=3,column=1)

lbl_customer_id=Label(f2,font=("aria",10),text="Customer ID",width=16,fg="black",bg="lightblue")
lbl_customer_id.grid(row=4,column=0)
entry_customer_id=Entry(f2,font=("aria",10,"bold"),width=10,bg="lightblue",fg="black",bd=3)
entry_customer_id.grid(row=4,column=1)

#billing
f3=Frame(root,bd=3,height=580,width=670,relief=RAISED)
f3.place(x=270,y=15)
dosa=StringVar()
paneer_tikka=StringVar()
aloo_sabji=StringVar()
butter_roti=StringVar()
butter_naan=StringVar()
cold_drink=StringVar()
total_bill=StringVar()

#dosa
lbl_dosa=Label(f3,font=("aria",15,"bold"),text="Dosa",width=11,fg="black")
lbl_dosa.grid(row=1,column=0)
entry_dosa=Entry(f3,font=("aria",20,"bold"),textvariable=dosa,bd=8,width=8 ,bg="lightpink")
entry_dosa.grid(row=1,column=1)

#paneer_tikka
lbl_paneer_tikka=Label(f3,font=("aria",15,"bold"),text="Paneer Tikka",width=11,fg="black")
lbl_paneer_tikka.grid(row=2,column=0)
entry_paneer_tikka=Entry(f3,font=("aria",20,"bold"),textvariable=paneer_tikka,bd=8,width=8 ,bg="lightpink")
entry_paneer_tikka.grid(row=2,column=1)

#aloo sabji
lbl_aloo_sabji=Label(f3,font=("aria",15,"bold"),text="Aloo Sabji",width=11,fg="black")
lbl_aloo_sabji.grid(row=3,column=0)
entry_aloo_sabji=Entry(f3,font=("aria",20,"bold"),textvariable=aloo_sabji,bd=8,width=8 ,bg="lightpink")
entry_aloo_sabji.grid(row=3,column=1)

#butter_roti
lbl_butter_roti=Label(f3,font=("aria",15,"bold"),text="Butter Roti",width=11,fg="black")
lbl_butter_roti.grid(row=4,column=0)
entry_butter_roti=Entry(f3,font=("aria",20,"bold"),textvariable=butter_roti,bd=8,width=8 ,bg="lightpink")
entry_butter_roti.grid(row=4,column=1)

#butter_naan
lbl_butter_naan=Label(f3,font=("aria",15,"bold"),text="Butter Naan",width=11,fg="black")
lbl_butter_naan.grid(row=5,column=0)
entry_butter_naan=Entry(f3,font=("aria",20,"bold"),textvariable=butter_naan,bd=8,width=8 ,bg="lightpink")
entry_butter_naan.grid(row=5,column=1)

#cold_drink
lbl_cold_drink=Label(f3,font=("aria",15,"bold"),text="Cold Drink",width=11,fg="black")
lbl_cold_drink.grid(row=6,column=0)
entry_cold_drink=Entry(f3,font=("aria",20,"bold"),textvariable=cold_drink,bd=8,width=8 ,bg="lightpink")
entry_cold_drink.grid(row=6,column=1)

#reset_button
btn_reset=Button(f3,bd=5,fg="white",bg="red",font=("calibri",16,"bold"),text="Reset",width=10,command=reset)
btn_reset.grid(row=8,column=0)

#total_button
btn_total=Button(f3,bd=5,fg="black",bg="lightblue",font=("calibri",16,"bold"),text="Total",width=10,command=total)
btn_total.grid(row=8,column=1)

#print_bill_button
btn_print_bill=Button(f3,bd=5,fg="black",bg="lightblue",font=("calibri",16,"bold"),text="Print Bill",width=10,command=print_bill)
btn_print_bill.grid(row=10,column=1)

#quit_button
btn_quit=Button(f3,bd=5,fg="white",bg="red",font=("calibri",16,"bold"),text="Quit",width=10,command=root.destroy)
btn_quit.grid(row=11,column=1)

root.mainloop()