import pymysql

class my_db:
    def __init__(self):
        # 连接数据库需要的参数
        self.conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            database="mysql",
            charset="utf8",
            user="root",
            passwd="zjh2001905/"
        )
    
    '''
        param:command要执行的一条sql语句
        当前只是在控制台输出执行结果
    '''
    def execute_sql(self,command):
        data=None
        try:
            with self.conn.cursor() as cursor:
                # 准备SQL语句
                cursor.execute(command)
                # 执行完SQL语句后的返回结果都是保存在cursor中
                # 所以要从cursor中获取全部数据
                data = cursor.fetchall()
                #print(data==())
                for i in data:
                    print(i)
        except Exception as e:
            print("数据库操作异常：\n", e)
        finally:
            # 不管成功还是失败，都要关闭数据库连接
            # self.conn.close()
            self.conn.commit()
        return data
