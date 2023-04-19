import db,layout_login,layout_main,globalvars
import threading,time
#global login_ui,database
login_ui=None
database=None
lock_init_db=threading.RLock()#初始化db的锁
lock_login=threading.RLock()#是否登陆的锁

def login_event():
    # 初始化登入界面，将数据库作为参数
    global login_ui
    lock_login.acquire()#还没登陆，要上锁
    time.sleep(0.5)
    lock_init_db.acquire()
    login_ui=layout_login.GUI(database)


    login_ui.root.mainloop()
    lock_init_db.release()
    lock_login.release()
    
def db_event():
    # 初始化数据库
    global database
    lock_init_db.acquire()#上锁（初始化db）
    database=db.my_db()
    database.execute_sql('use mycatsys')
    lock_init_db.release()#释放锁

def main_evevt():
    time.sleep(0.5)
    lock_login.acquire()
    a=layout_main.GUI(database)
    a.root.mainloop()
    


class main:
    
    # @property
    # def success_login(self):
    #     return login_ui.success_login
    # @success_login.setter
    # def success_login(self):
    #     if self.success_login:
    #         print("Success!!!")
    #     else :
    #         print("Fail!!!")
        


    
    def __init__(self):
        #声明线程
        thr_db=threading.Thread(name='thrdb',target=db_event)
        thr_login=threading.Thread(name='thrlgn',target=login_event)
        thr_main=threading.Thread(name='thrmn',target=main_evevt)
        
        
        
        thr_db.start()
        thr_login.start()
        thr_main.start()







main()