import tkinter as tk  # 在代码里面导入库，起一个别名，以后代码里面就用这个别名
import globalvars,db

class GUI:
    
    
    
    def __init__(self,database:db.my_db):
        self.database=database
        self.root = tk.Tk()
        self.root.title('校园猫猫管理系统')
        self.root.geometry("400x300+400+80")
        self.success_login=False
        

        text_label=tk.Label(self.root,width=175,text="欢迎来到\n校园猫猫管理系统",
                            font=('PMingLiu',15),bg='white')
        text_label.pack(padx=3,pady=20)
        
        frm_1 = tk.Frame(self.root,width=400,height=300,relief='groove',bd=1)  
        label_user=tk.Label(frm_1,text="用户名：",font=('PMingLiu',12))
        entry_user=tk.Entry(frm_1)
        label_password=tk.Label(frm_1,text="密码：",font=('PMingLiu',12))
        entry_password=tk.Entry(frm_1)
        
        label_user.grid(row=1,column=1)
        entry_user.grid(row=1,column=2,columnspan=3,pady=5,padx=5)
        label_password.grid(row=2,column=1)
        entry_password.grid(row=2,column=2,columnspan=3,pady=5,padx=5)
        
        button_login=tk.Button(frm_1,text='登陆',font=('PMingLiu',12),
                               command=lambda:login(entry_user.get(),entry_password.get()))
        button_login.grid(row=3,column=2)
        button_rgstr=tk.Button(frm_1,text='注册',font=('PMingLiu',12),
                               command=lambda:register(entry_user.get(),entry_password.get()))
        button_rgstr.grid(row=3,column=3)
        self.notice_label=tk.Label(frm_1,text="数据库实验四 @ 200110631 张景昊",font=('PMingLiu',12),
                              background='lightblue')
        self.notice_label.grid(row=4,column=1,columnspan=4)
        
        frm_1.pack()
        

        
        def login(usrnm:str,pswd:str):
            if usrnm.strip()=='' or pswd.strip()=='':
                self.notice_label['text']='账号或密码不能为空！'
                return
            sql='select * from userinfo where user_account=\''+usrnm+'\' and user_pwd=\''+pswd+'\' '
            result=self.database.execute_sql(sql)
            if len(result)==1:
                #查询成功，登陆
                self.success_login=True
                globalvars.user_id=result[0][2]
                globalvars.username=usrnm
                print("layout_login : Success")
                self.root.destroy()
            else:
                print("layout_login : Fail")
                self.notice_label['text']='登陆失败。请检查用户名和密码是否正确。\n或点击『注册』来注册新账号。'
                
        def register(usrnm,pswd):
            if usrnm.strip()=='' or pswd.strip()=='':
                self.notice_label['text']='账号或密码不能为空！'
                return
            sql='select * from userinfo where user_account=\''+usrnm+'\' '
            result=self.database.execute_sql(sql)
            if len(result)==0:
                #可以创建账号
                #分配一个user_id
                result=self.database.execute_sql('select * from userinfo')
                curr_id=len(result)+1
                sql='insert into userinfo values ( \''+usrnm+'\',\''+pswd+'\','+str(curr_id)+') '
                self.database.execute_sql(sql)
                globalvars.user_id=curr_id
                globalvars.username=usrnm
                self.root.destroy()
            else:
                #用户名重复
                print('注册失败')
                self.notice_label['text']='注册失败。用户名与已有用户名重复。\n请尝试修改用户名。'
                
            
            
            
        
        
        
        

        

    

        

        
        

        
        
if __name__ == '__main__':
    a = GUI()
    a.root.mainloop()