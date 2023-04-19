import tkinter as tk  # 在代码里面导入库，起一个别名，以后代码里面就用这个别名
from tkinter import messagebox,ttk
import globalvars
from db import my_db
import numpy as np
import layout_insert,layout_add


class GUI:
    
    def __init__(self,database:my_db):
        self.root = tk.Tk()
        self.root.title('校园猫猫管理系统')
        self.root.geometry("1000x800+400+80")
        global db
        db=database
        
        frm = tk.Frame(self.root,width=970,height=770,bd=5)             # #创建一个frame控件
        frm.pack()
        
        # 左侧
        frm_1 = tk.Frame(frm,width=175,height=700,relief='groove',bd=1,bg='lightgreen') #创建一个frm_1并且放到frm上
        frm_1.pack_propagate(0);
        #左侧的所有内容与控件
        text_label=tk.Label(frm_1,width=175,text="校园猫猫管理系统",font=('PMingLiu',15))
        text_label.pack(padx=3,pady=10)
        
        text_user=tk.Label(frm_1,width=175,text='用户名：'+globalvars.username,
                           font=('PMingLiu',12))
        text_user.pack(padx=3,pady=20)

        
        
        btn1=tk.Button(frm_1,text='查看猫猫讯息',font=('PMingLiu',14),command=lambda:self.press_button(1))
        btn1.pack(pady=20)
        btn2=tk.Button(frm_1,text='猫猫出现记录',font=('PMingLiu',14),command=lambda:self.press_button(2))
        btn2.pack(pady=20)
        
        btn3=tk.Button(frm_1,text='猫猫投喂记录',font=('PMingLiu',14),command=lambda:self.press_button(3))
        btn3.pack(pady=20)
        btn4=tk.Button(frm_1,text='猫猫生病记录',font=('PMingLiu',14),command=lambda:self.press_button(4))
        btn4.pack(pady=20)
        
        text_me=tk.Label(frm_1,width=175,text='数据库实验四\n@200110631 张景昊',
                           font=('PMingLiu',12))
        text_me.pack(side=tk.BOTTOM)
        btn3=tk.Button(frm_1,text='增加地点',font=('PMingLiu',12),command=lambda:self.prs_addbtn(1))
        btn3.pack(pady=10,side=tk.BOTTOM)
        btn4=tk.Button(frm_1,text='增加猫食',font=('PMingLiu',12),command=lambda:self.prs_addbtn(2))
        btn4.pack(pady=10,side=tk.BOTTOM)
        
        frm_1.pack(side=tk.LEFT)         # #frm_1的位置放在左侧
        
        frm_2 = tk.Frame(frm,width=725,height=700,relief='groove',bd=1,bg='lightblue')
        frm_2.pack_propagate(0);
        
        self.frm_up=tk.Frame(frm_2,width=725,height=100,relief='groove',bd=1,bg='violet')
        self.frm_down=tk.Frame(frm_2,width=725,height=600,relief='groove',bd=1,bg='lightpink')
        self.frm_up.pack()
        self.frm_down.pack()
        self.frm_up.pack_propagate(0)
        self.frm_down.pack_propagate(0)
        
        
        frm_2.pack(side=tk.RIGHT)
        self.currpage=0
        
    def refresh_up(self):
        for x in self.frm_up.winfo_children():
            x.destroy()
        return
    def refresh_down(self):
        for x in self.frm_down.winfo_children():
            x.destroy()
        return
    
    def prs_addbtn(self,arg_x:int):
        layout_add.GUI(arg_x,db)
        pass
    def press_button(self,arg_page:int,restrictions=' ',need_refresh_upfrm=True):        
        need_refresh_upfrm= False if(arg_page==self.currpage) else True
        self.currpage=arg_page
        if need_refresh_upfrm==True:
            self.refresh_up()
            self.load_upframe()
        self.refresh_down()
        
        data_to_show=self.load_data(restrictions=restrictions)
        tree=ttk.Treeview(self.frm_down,show='headings',height=20)
        
        # messagebox.showinfo("窗口名称","点击成功")
        if self.currpage==1:
            #查看猫猫讯息
            for i in range(0,len(data_to_show)):
                data_to_show[i][3]= '公猫' if(data_to_show[i][3]=='0' )  else '母猫'
            tree['columns']=('名字','性别','品种','颜色','被发现总次数')
            tree.column('名字',width=125)
            tree.column('性别',width=125)
            tree.column('品种',width=125)
            tree.column('颜色',width=125)
            tree.column('被发现总次数',width=125)
            tree.heading('名字',text='名字')
            tree.heading('性别',text='性别')
            tree.heading('品种',text='品种')
            tree.heading('颜色',text='颜色')
            tree.heading('被发现总次数',text='被发现总次数')
            for i in range(0,len(data_to_show)):
                tree.insert('',i,text='',values=(
                    data_to_show[i][0],data_to_show[i][3],data_to_show[i][1],data_to_show[i][2],data_to_show[i][5]
                ))
            
            pass
        elif self.currpage==2:
            #猫猫出现记录
            tree['columns']=('名字','时间','地点')
            tree.column('名字',width=100)
            tree.column('时间',width=270)
            tree.column('地点',width=270)
            tree.heading('名字',text='名字')
            tree.heading('时间',text='时间')
            tree.heading('地点',text='地点')
            for i in range(0,len(data_to_show)):
                tree.insert('',i,text='',values=(
                    data_to_show[i][0],data_to_show[i][1],data_to_show[i][2]
                ))
        elif self.currpage==3:
            #猫猫投喂记录
            tree['columns']=('名字','食物','地点','时间','用户')
            tree.column('名字',width=100)
            tree.column('食物',width=80)
            tree.column('地点',width=200)
            tree.column('时间',width=200)
            tree.column('用户',width=100)
            tree.heading('名字',text='名字')
            tree.heading('时间',text='时间')
            tree.heading('地点',text='地点')
            tree.heading('食物',text='食物')
            tree.heading('用户',text='用户')
            for i in range(0,len(data_to_show)):
                tree.insert('',i,text='',values=(
                    data_to_show[i][0],data_to_show[i][1],data_to_show[i][2],
                    data_to_show[i][3],data_to_show[i][4]
                ))
            pass
        elif self.currpage==4:
            #猫猫生病记录
            tree['columns']=('名字','品种 性别','疾病','医院','带它看病的用户','开销')
            tree.column('名字',width=80)
            tree.column('品种 性别',width=100)
            tree.column('疾病',width=100)
            tree.column('医院',width=175)
            tree.column('带它看病的用户',width=150)
            tree.column('开销',width=100)
            tree.heading('名字',text='名字')
            tree.heading('品种 性别',text='品种 性别')
            tree.heading('疾病',text='疾病')
            tree.heading('医院',text='医院')
            tree.heading('带它看病的用户',text='带它看病的用户')
            tree.heading('开销',text='开销')
            for i in range(0,len(data_to_show)):
                data_to_show[i][2]= '公猫' if(data_to_show[i][2]=='0' )  else '母猫'
                tree.insert('',i,text='',values=(
                    data_to_show[i][0],data_to_show[i][1]+data_to_show[i][2],
                    data_to_show[i][3],data_to_show[i][4],data_to_show[i][5],data_to_show[i][6]
                ))
            pass
        else:
            pass
        self.vscroll=tk.Scrollbar(self.frm_down,orient='vertical',command=tree.yview)
        tree.configure(yscrollcommand=self.vscroll.set)
        tree.grid(row=0,column=0)
        self.vscroll.grid(row=0,column=1,sticky='ns')
        
    def load_data(self,restrictions=''):
        sql=' '
        if self.currpage==1:
            sql='select * from cat'
        elif self.currpage==2:
            sql="select c.cat_name,DATE_FORMAT(a.aprnc_time,\'%Y-%m-%d %H:%i:%s\'),l.location_where from cat c,appearance a,location l"
            sql=sql+" where c.cat_id=a.aprnc_cat_id "
            sql=sql+" and a.aprnc_location_id=l.location_id "
        elif self.currpage ==3:
            sql='select c.cat_name,cf.foodtype_name,l.location_where,'
            sql=sql+' DATE_FORMAT(f.feed_time,\'%Y-%m-%d %H:%i:%s\'),u.user_account '
            sql=sql+' from feed f,catfood cf,cat c,userinfo u,location l '
            sql=sql+' where c.cat_id=f.feed_cat_id '
            sql=sql+' and f.feed_foodtype_id=cf.foodtype_id '
            sql=sql+' and u.user_id=f.feed_user_id '
            sql=sql+' and l.location_id=f.feed_loacation_id '
        elif self.currpage ==4:
            sql='select c.cat_name,c.cat_type,c.cat_gender,sr.sick_content,ph.hsptl_name, '
            sql=sql+' u.user_account,sr.sick_cost '
            sql=sql+' from userinfo u,cat c,sickness_record sr,pet_hospital ph '
            sql=sql+' where sr.user_id=u.user_id and sr.cat_id=c.cat_id '
            sql=sql+' and sr.hospital_id=ph.hsptl_id '
            
        else:
            pass
        sql=sql+restrictions
        print(sql)
        return np.array(db.execute_sql(sql))

    
    def load_upframe(self):
        if self.currpage==1:
            label1=tk.Label(self.frm_up,width=15,text="筛选：  性别",font=('PMingLiu',12))
            label1.pack(fill=tk.X,side=tk.LEFT)
            label1.pack_propagate(0)
            combobox=ttk.Combobox(self.frm_up,textvariable='111',width=12)
            combobox['values']=('公猫','母猫')
            combobox.current(0)
            combobox.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox.pack_propagate(0)
            check_button=tk.Button(self.frm_up,text='查询',font=('PMingLiu',12),
                                   command=lambda:self.prs_chkbtn(1,gender=combobox.get()))
            check_button.pack(fill=tk.X,side=tk.LEFT,padx=5)
            check_button.pack_propagate(0)
            insert_button1=tk.Button(self.frm_up,text='新增猫猫',font=('PMingLiu',12),
                                   command=lambda:self.press_insrtbtn(1),bg='mediumblue',fg='white')
            insert_button1.pack(fill=tk.X,side=tk.RIGHT,padx=5)
            insert_button1.pack_propagate(0)
            pass
        elif self.currpage==2:
            label2=tk.Label(self.frm_up,width=15,text="筛选：  猫猫",font=('PMingLiu',12))
            label2.pack(fill=tk.X,side=tk.LEFT)
            label2.pack_propagate(0)
            combobox2=ttk.Combobox(self.frm_up,textvariable='222',width=12)
            data_cats=np.array(db.execute_sql('select cat_name from cat'))
            data_cats=np.insert(data_cats,0,'任意')
            combobox2['values']=tuple(data_cats)
            combobox2.current(0)
            combobox2.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox2.pack_propagate(0)
            
            label3=tk.Label(self.frm_up,width=5,text="地点",font=('PMingLiu',12))
            label3.pack(fill=tk.X,side=tk.LEFT)
            label3.pack_propagate(0)
            combobox22=ttk.Combobox(self.frm_up,textvariable='333',width=20)
            data_locations=np.array(db.execute_sql('select location_where from location'))
            data_locations=np.insert(data_locations,0,'任意')
            combobox22['values']=tuple(data_locations)
            combobox22.current(0)
            combobox22.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox22.pack_propagate(0)
            check_button2=tk.Button(self.frm_up,text='查询',font=('PMingLiu',12),
                                   command=lambda:self.prs_chkbtn(2,cat_name=combobox2.get(),
                                                                  location=combobox22.get()))
            check_button2.pack(fill=tk.X,side=tk.LEFT,padx=5)
            check_button2.pack_propagate(0)
            insert_button2=tk.Button(self.frm_up,text='新增出现记录',font=('PMingLiu',12),
                                   command=lambda:self.press_insrtbtn(2),bg='mediumblue',fg='white')
            insert_button2.pack(fill=tk.X,side=tk.RIGHT,padx=5)
            insert_button2.pack_propagate(0)
        elif self.currpage==3:
            label3=tk.Label(self.frm_up,width=15,text="筛选：  猫猫",font=('PMingLiu',12))
            label3.pack(fill=tk.X,side=tk.LEFT)
            label3.pack_propagate(0)
            combobox3=ttk.Combobox(self.frm_up,textvariable='444',width=12)
            data_cats=np.array(db.execute_sql('select cat_name from cat'))
            data_cats=np.insert(data_cats,0,'任意')
            combobox3['values']=tuple(data_cats)
            combobox3.current(0)
            combobox3.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox3.pack_propagate(0)
            check_button3=tk.Button(self.frm_up,text='查询',font=('PMingLiu',12),
                                   command=lambda:self.prs_chkbtn(3,cat_name=combobox3.get()))
            check_button3.pack(fill=tk.X,side=tk.LEFT,padx=5)
            check_button3.pack_propagate(0)
            insert_button3=tk.Button(self.frm_up,text='新增投喂记录',font=('PMingLiu',12),
                                   command=lambda:self.press_insrtbtn(3),bg='mediumblue',fg='white')
            insert_button3.pack(fill=tk.X,side=tk.RIGHT,padx=5)
            insert_button3.pack_propagate(0)
            pass
        elif self.currpage==4:
            label4=tk.Label(self.frm_up,width=15,text="筛选：  猫猫",font=('PMingLiu',12))
            label4.pack(fill=tk.X,side=tk.LEFT)
            label4.pack_propagate(0)
            combobox4=ttk.Combobox(self.frm_up,textvariable='555',width=12)
            data_cats=np.array(db.execute_sql('select cat_name from cat'))
            data_cats=np.insert(data_cats,0,'任意')
            combobox4['values']=tuple(data_cats)
            combobox4.current(0)
            combobox4.pack(fill=tk.X,side=tk.LEFT,padx=5)
            combobox4.pack_propagate(0)
            check_button4=tk.Button(self.frm_up,text='查询',font=('PMingLiu',12),
                                   command=lambda:self.prs_chkbtn(4,cat_name=combobox4.get()))
            check_button4.pack(fill=tk.X,side=tk.LEFT,padx=5)
            check_button4.pack_propagate(0)
            insert_button4=tk.Button(self.frm_up,text='新增看病记录',font=('PMingLiu',12),
                                   command=lambda:self.press_insrtbtn(4),bg='mediumblue',fg='white')
            insert_button4.pack(fill=tk.X,side=tk.RIGHT,padx=5)
            insert_button4.pack_propagate(0)
            pass
        else:
            pass
    
    
    def prs_chkbtn(self,arg_x:int,gender=None,cat_name=None,location=None):
        appn=' '
        if arg_x==1:
            gen=1
            if gender=='公猫':
                gen=0
            appn=' where cat_gender = '+str(gen)+' ' 
            self.press_button(arg_page=1,restrictions=appn,need_refresh_upfrm=False)
            pass
        elif arg_x==2:
            if location!='任意':
                appn=appn+' and l.location_where = \''+location+'\' '
            if cat_name!='任意':
                appn=appn+' and c.cat_name = \''+cat_name+'\' '
            self.press_button(arg_page=2,restrictions=appn,need_refresh_upfrm=False)
            pass
        elif arg_x==3:
            if cat_name!='任意':
                appn=appn+' and c.cat_name = \''+cat_name+'\' '
            self.press_button(arg_page=3,restrictions=appn,need_refresh_upfrm=False)
            pass
        elif arg_x==4:
            if cat_name!='任意':
                appn=appn+' and c.cat_name = \''+cat_name+'\' '
            self.press_button(arg_page=4,restrictions=appn,need_refresh_upfrm=False)
            pass
        else:
            pass
        pass
    
    def press_insrtbtn(self,arg_x:int):
        layout_insert.GUI(arg_x,db)
        pass
        


if __name__ == '__main__':
    a = GUI()
    a.root.mainloop()
