import threading

def add(a,i,strrr):
    a=a+i
    print(str(a)+'aa'+strrr)


global a
a=3
thr1=threading.Thread(name='1',target=add,args=(a,2,'aaaaaa'))
thr2=threading.Thread(name='1',target=add,args=(a,4,'qqqqqq'))
thr1.start()
thr2.start()
print(a)