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
        if arg_x==1:
            text_to_show='新增：  猫猫'
        elif arg_x==2:
            text_to_show='新增：猫猫出现记录'
        elif arg_x==3:
            text_to_show='新增：猫猫投喂记录'
        elif arg_x==4:
            text_to_show='新增：猫猫生病记录'
        else:
            pass
        label1=tk.Label(self.top,width=15,text=text_to_show,font=('PMingLiu',12))
        label1.pack_propagate(0)
        label1.pack(side=tk.TOP)
        frame1=tk.Frame(self.top,width=600,height=350,relief='groove',bd=1,bg='lightgreen') 
        frame1.pack(side=tk.TOP)
        frame1.pack_propagate(0)
        label_list=list()
       
        if arg_x==1:
            strs=['名字','品种','颜色','性别']
            for i in range(0,len(strs)):
                label_list.append(tk.Label(frame1,text=strs[i],font=('PMingLiu',12)))
                label_list[i].grid(row=1,column=i+1,padx=10,pady=3)
            entry_1_1=tk.Entry(frame1,width=16)
            entry_1_2=tk.Entry(frame1,width=16)
            entry_1_3=tk.Entry(frame1,width=16)
            combobox_1_4=ttk.Combobox(frame1,textvariable='cbx1')
            combobox_1_4['values']=('公猫','母猫')
            combobox_1_4.current(0)
            combobox_1_4.pack_propagate(0)
            entry_1_1.grid(row=2,column=1,padx=10,pady=3)
            entry_1_2.grid(row=2,column=2,padx=10,pady=3)
            entry_1_3.grid(row=2,column=3,padx=10,pady=3)
            combobox_1_4.grid(row=2,column=4,padx=10,pady=3)
            insert_button_1=tk.Button(self.top,text='上传',bg='pink',font=('PMingLiu',12),
                                    command=lambda:self.prs_insertbtn(arg_x=arg_x,
                                                                      cat_gender=combobox_1_4.get(),
                                                                      cat_name=entry_1_1.get(),
                                                                      cat_color=entry_1_3.get(),
                                                                      cat_type=entry_1_2.get()))   
            insert_button_1.pack(pady=10) 
            
            pass
        elif arg_x==2:
            strs=['名字','地点','时间']
            for i in range(0,len(strs)):
                label_list.append(tk.Label(frame1,text=strs[i],font=('PMingLiu',12)))
                label_list[i].grid(row=1,column=i+1,padx=10,pady=3)
            combobox2_1=ttk.Combobox(frame1,textvariable='2-1')
            data_cats=db.execute_sql('select cat_name from cat')
            combobox2_1['values']=data_cats
            combobox2_1.current(0)
            combobox2_1.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox2_1.pack_propagate(0)
            

            combobox2_2=ttk.Combobox(frame1,textvariable='2-2')
            data_locations=db.execute_sql('select location_where from location')
            combobox2_2['values']=data_locations
            combobox2_2.current(0)
            combobox2_2.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox2_2.pack_propagate(0)
            
            
            combobox2_3=ttk.Combobox(frame1,textvariable='2-3')
            combobox2_3['values']='现在'
            combobox2_3.current(0)
            combobox2_3.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox2_3.pack_propagate(0)
            
            
            combobox2_1.grid(row=2,column=1,padx=10,pady=3)
            combobox2_2.grid(row=2,column=2,padx=10,pady=3)
            combobox2_3.grid(row=2,column=3,padx=10,pady=3)

            insert_button_2=tk.Button(self.top,text='上传',bg='pink',font=('PMingLiu',12),
                                    command=lambda:self.prs_insertbtn(arg_x=arg_x,
                                                                      cat_name=combobox2_1.get(),
                                                                      location=combobox2_2.get()))   
            insert_button_2.pack(pady=10) 
            pass
        elif arg_x==3:
            strs=['名字','时间','地点','食物']
            for i in range(0,len(strs)):
                label_list.append(tk.Label(frame1,text=strs[i],font=('PMingLiu',12)))
                label_list[i].grid(row=1,column=i+1,padx=10,pady=3)
            combobox3_1=ttk.Combobox(frame1,textvariable='3-1',width=12)
            data_cats=db.execute_sql('select cat_name from cat')
            combobox3_1['values']=data_cats
            combobox3_1.current(0)
            combobox3_1.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox3_1.pack_propagate(0)
            

            combobox3_3=ttk.Combobox(frame1,textvariable='3-3',width=12)
            data_locations=db.execute_sql('select location_where from location')
            combobox3_3['values']=data_locations
            combobox3_3.current(0)
            combobox3_3.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox3_3.pack_propagate(0)
            
            
            combobox3_2=ttk.Combobox(frame1,textvariable='3-2',width=12)
            combobox3_2['values']='现在'
            combobox3_2.current(0)
            combobox3_2.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox3_2.pack_propagate(0)
            
            combobox3_4=ttk.Combobox(frame1,textvariable='3-4',width=12)
            data_food=db.execute_sql('select foodtype_name from catfood ')
            combobox3_4['values']=data_food
            combobox3_4.current(0)
            combobox3_4.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox3_4.pack_propagate(0)
            
            
            combobox3_1.grid(row=2,column=1,padx=10,pady=3)
            combobox3_2.grid(row=2,column=2,padx=10,pady=3)
            combobox3_3.grid(row=2,column=3,padx=10,pady=3)
            combobox3_4.grid(row=2,column=4,padx=10,pady=3)

            insert_button_3=tk.Button(self.top,text='上传',bg='pink',font=('PMingLiu',12),
                                    command=lambda:self.prs_insertbtn(arg_x=arg_x,
                                                                      cat_name=combobox3_1.get(),
                                                                      location=combobox3_3.get(),
                                                                      food=combobox3_4.get()))   
            insert_button_3.pack(pady=10) 
            pass
        elif arg_x==4:
            strs=['名字','医院','花销','病情']
            for i in range(0,len(strs)):
                label_list.append(tk.Label(frame1,text=strs[i],font=('PMingLiu',12)))
                label_list[i].grid(row=1,column=i+1,padx=10,pady=3)
            combobox4_1=ttk.Combobox(frame1,textvariable='4-1',width=12)
            data_cats=db.execute_sql('select cat_name from cat')
            combobox4_1['values']=data_cats
            combobox4_1.current(0)
            combobox4_1.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox4_1.pack_propagate(0)
            

            combobox4_2=ttk.Combobox(frame1,textvariable='4-2',width=12)
            data_locations=db.execute_sql('select hsptl_name from pet_hospital')
            combobox4_2['values']=data_locations
            combobox4_2.current(0)
            combobox4_2.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox4_2.pack_propagate(0)
            
            
            entry_4_3=tk.Entry(frame1,width=16)
            entry_4_4=tk.Entry(frame1,width=16)
            
            
            combobox4_1.grid(row=2,column=1,padx=10,pady=3)
            combobox4_2.grid(row=2,column=2,padx=10,pady=3)
            entry_4_3.grid(row=2,column=3,padx=10,pady=3)
            entry_4_4.grid(row=2,column=4,padx=10,pady=3)

            insert_button_4=tk.Button(self.top,text='上传',bg='pink',font=('PMingLiu',12),
                                    command=lambda:self.prs_insertbtn(arg_x=arg_x,
                                                                      cat_name=combobox4_1.get(),
                                                                      hospital=combobox4_2.get(),
                                                                      cost=entry_4_3.get(),
                                                                      sick_content=entry_4_4.get()))   
            insert_button_4.pack(pady=10) 
            pass
        else:
            pass

        self.label_notice=tk.Label(self.top,text='--------------------',font=('PMingLiu',12))  
        self.label_notice.pack(side=tk.TOP)
   
        pass
    
    def prs_insertbtn(self,arg_x:int,cat_name=None,cat_type=None,cat_color=None,
                      cat_gender=None,location=None,food=None,
                      hospital=None,cost=None,sick_content=None
                      ):
        
        if arg_x==1:
            if len(cat_name)==0 or len(cat_type)==0 or len(cat_color)==0:
                self.label_notice['text']='不能为空！'
                return
            if len(cat_name)>15:
                self.label_notice['text']='名字 不能超过15个字！'
                return
            if len(cat_type)>15:
                self.label_notice['text']='品种 不能超过15个字！'
                return
            if len(cat_color)>15:
                self.label_notice['text']='颜色 不能超过15个字！'
                return
            sql='select * from cat where cat_name=\''+cat_name+'\' '
            data=self.db.execute_sql(sql)
            if len(data)!=0 :
                self.label_notice['text']='猫的名字不能重复！'
                return
            data=self.db.execute_sql('select * from cat')
            cid=len(data)+1
            gender=0 if cat_gender=='公猫' else 1
            sql='insert into cat values(\''+cat_name+'\',\''+cat_type+'\',\''+cat_color+'\','+str(gender)+','+str(cid)+',0)'
            self.db.execute_sql(sql)
            pass
        elif arg_x==2:
            location_id=self.db.execute_sql("select location_id from location where location_where=\'"+location+"\' ")[0][0]
            cat_id=self.db.execute_sql("select cat_id from cat where cat_name=\'"+cat_name+"\' ")[0][0]
            apid=self.db.execute_sql('select * from appearance')
            apid=len(apid)+1
            sql='insert into appearance values('+str(cat_id)+','+str(location_id)+',now(),'+str(apid)+')'
            self.db.execute_sql(sql)
            pass
        elif arg_x==3:
            location_id=self.db.execute_sql("select location_id from location where location_where=\'"+location+"\' ")[0][0]
            cat_id=self.db.execute_sql("select cat_id from cat where cat_name=\'"+cat_name+"\' ")[0][0]
            food_id=self.db.execute_sql("select foodtype_id from catfood where foodtype_name=\'"+food+"\' ")[0][0]
            fpid=self.db.execute_sql('select * from feed')
            fpid=len(fpid)+1
            sql='insert into feed values('+str(globalvars.user_id)+','+str(cat_id)+',now(),'+str(location_id)+','+str(food_id)+','+str(fpid)+')'
            self.db.execute_sql(sql)
            pass
        elif arg_x==4:
            hsptl_id=self.db.execute_sql("select hsptl_id from pet_hospital where hsptl_name=\'"+hospital+"\' ")[0][0]
            cat_id=self.db.execute_sql("select cat_id from cat where cat_name=\'"+cat_name+"\' ")[0][0]
            try:
                cost=float(cost)
                pass
            except Exception as e:
                self.label_notice['text']='花销请输入数字！'
                return            
                
            srid=self.db.execute_sql('select * from sickness_record')
            srid=len(srid)+1
            sql='insert into sickness_record values('+str(srid)+','+str(globalvars.user_id)+','+str(cat_id)+','+str(hsptl_id)+','+str(cost)+',\''+sick_content+'\')'
            self.db.execute_sql(sql)
            pass
        else:
            pass
        
        self.top.destroy()
        pass