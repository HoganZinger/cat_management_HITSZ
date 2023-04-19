import tkinter as tk  # 在代码里面导入库，起一个别名，以后代码里面就用这个别名
from tkinter import messagebox,ttk
import globalvars,db
import numpy as np
class GUI:

    def __init__(self,arg_x:int,db:db.my_db):
        self.db=db
        self.top=tk.Toplevel()
        self.top.title('增加')
        self.top.geometry("650x200+600+280")
        text_to_show=''
        frame1=tk.Frame(self.top,width=600,height=150,relief='groove',bd=1,bg='lightgreen') 
        frame1.pack(side=tk.TOP)
        frame1.pack_propagate(0)
        label1=tk.Label(self.top,width=15,text=text_to_show,font=('PMingLiu',12))
        label1.pack_propagate(0)
        label1.pack(side=tk.TOP)
        if arg_x==1:
            text_to_show='增加：地点'
            label_1_1=tk.Label(frame1,width=15,text='已有地点',font=('PMingLiu',12))
            label_1_2=tk.Label(frame1,width=15,text='新建地点',font=('PMingLiu',12))
            combobox1_1=ttk.Combobox(frame1,textvariable='2-2')
            data_locations=db.execute_sql('select location_where from location')
            combobox1_1['values']=data_locations
            combobox1_1.current(0)
            combobox1_1.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox1_1.pack_propagate(0)
            
        elif arg_x==2:
            text_to_show='增加：猫食'
            label_1_1=tk.Label(frame1,width=15,text='已有猫食',font=('PMingLiu',12))
            label_1_2=tk.Label(frame1,width=15,text='新建猫食',font=('PMingLiu',12))
            combobox1_1=ttk.Combobox(frame1,textvariable='4-3')
            data_locations=db.execute_sql('select foodtype_name from catfood ')
            combobox1_1['values']=data_locations
            combobox1_1.current(0)
            combobox1_1.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox1_1.pack_propagate(0)
        else:
            pass
        entry_1_2=tk.Entry(frame1,width=16)
        label_1_1.grid(row=1,column=1,padx=10,pady=3)
        label_1_2.grid(row=1,column=2,padx=10,pady=3)
        combobox1_1.grid(row=2,column=1,padx=10,pady=3)
        entry_1_2.grid(row=2,column=2,padx=10,pady=3)
        
        frame1=tk.Frame(self.top,width=600,height=350,relief='groove',bd=1,bg='lightgreen') 
        frame1.pack(side=tk.TOP)
        frame1.pack_propagate(0)
        
        button_add=tk.Button(frame1,text='新建',bg='pink',font=('PMingLiu',12),command=lambda:self.add_item(
            arg_x=arg_x,things=entry_1_2.get()
        ))
        button_add.grid(row=3,column=1,columnspan=2)
        self.label_notice=tk.Label(self.top,text='--------------------',font=('PMingLiu',12))

        self.label_notice.pack(side=tk.TOP)
        pass
    def add_item(self,arg_x:int,things:str):
        if things.strip()=='':
            self.label_notice['text']='属性不可以为空！'
            return

        ifhav=0
        index=0
        if arg_x==1:
            if len(things)>128:
                self.label_notice['text']='不可以超过128个字！'
                return
            sql='select * from location where location_where=\''+things+'\' '
            data=self.db.execute_sql(sql)
            ifhav=len(data)
            index=len(self.db.execute_sql('select * from location'))+1
        elif arg_x==2:
            if len(things)>10:
                self.label_notice['text']='不可以超过10个字！'
                return
            sql='select * from catfood where foodtype_name=\''+things+'\' '
            data=self.db.execute_sql(sql)
            ifhav=len(data)
            index=len(self.db.execute_sql('select * from catfood'))+1
        if ifhav !=0:
            self.label_notice['text']='属性不可以重复！'
            return
        sql2=' '
        if arg_x==1:
            sql2='insert into location values(\''+things+'\','+str(index)+')'
        elif arg_x==2:
            sql2='insert into catfood values(\''+things+'\','+str(index)+')'       
        self.db.execute_sql(sql2) 
        self.top.destroy()