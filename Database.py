
"""底层数据API"""
"""数据库类 封装关于数据库的各种操作方法"""
import pymssql
from   Table import  *
class Database:

    #生成游标
    def CreateCursor(self):
        self.cursor=self.conn.cursor()
        return self.cursor
    #关闭数据库
    def CloseConn(self,conn):
        conn.close()
    #server  数据库服务器名称
    #user    用户名
    #password  密码
    #database  数据库名称
    #connectState 连接状态  success表示成功   fail表示失败
    def    ConnData(self,server,password,user="sa",database="master"):
        try:
            #print(server,password)
            self.conn=pymssql.connect(server,user,password,database)
            #生成游标
            self.CreateCursor()
            return 'success'
        except:
            return 'fail'
    """数据库 insert  select  update  delete """


    #选择操作,根据传来的flag进行查询 flag='code','customer','vendorclass','vendor','person','hr_hi_person' 'sysdatabases'
    #targetDatabase 目标数据库  candition 查询条件
    def selTable(self,targetDatabase,condition,flag):
        sqlStr=''
        if(flag=='code'):
            sqlStr= sqlStr=('select  ccode from  [%s].[dbo].[code]    where %s'%(targetDatabase,condition))
        elif(flag=='customer'):
            sqlStr=('select  ccuscode from  [%s].[dbo].[customer]    where %s'%(targetDatabase,condition))
        elif(flag=='vendorclass'):
            sqlStr=('select  cvccode from  [%s].[dbo].[vendorclass]   where %s'%(targetDatabase,condition))
        elif(flag=='vendor'):
            sqlStr=('select  cvencode from  [%s].[dbo].[vendor]   where %s'%(targetDatabase,condition))
        elif(flag=='person'):
            sqlStr=('select  cpersoncode from  [%s].[dbo].[person]   where %s'%(targetDatabase,condition))
        elif(flag=='hr_hi_person'):
            sqlStr=('select  cpsn_num from  [%s].[dbo].[hr_hi_person]   where %s'%(targetDatabase,condition))
        elif(flag=='sysdatabases'):
            sqlStr=('select name from [%s].[dbo].[sysdatabases] where %s'
            %(targetDatabase,"name like 'UFDATA_%' and "+condition))
            #print("查询语句:",sqlStr)
        elif(flag=='maxIno_id'):
            sqlStr=('select max(ino_id) from [%s].[dbo].[gl_accvouch] where %s'
                    %(targetDatabase,condition))
        elif(flag=='ino_id'):
            sqlStr=('select ino_id from [%s].[dbo].[gl_accvouch] where %s group by ino_id  '
                    %(targetDatabase,condition))
        elif(flag=='department'):
            sqlStr=('select cdepcode from [%s].[dbo].[department] where %s'%(targetDatabase,condition))

        self.cursor.execute(sqlStr)
        values=[]
        row=self.cursor.fetchone()
        while row:
            values.append(row[0])
            row=self.cursor.fetchone()
        return values

    #主要是插入基础档案的
    #插入操作,根据传来的flag进行查询 flag='code','customer','vendorclass','vendor','person','hr_hi_person'
    #targetDatabase 目标数据库  condition 查询条件
    def InsTable(self,sourceData,targetData,condition,flag):
        sqlStr=''
        if(flag=='code'):
            sqlStr=(r'insert into  [%s].[dbo].[code](%s)  select %s from [%s].[dbo].[code] where  %s'
                    r' and ccode not in (select ccode  from [%s].[dbo].[code])'
                    %(targetData,Table.table['code'],Table.table['code'],sourceData,condition,targetData))
        elif(flag=='customer'):
            sqlStr=(r'insert into  [%s].[dbo].[customer](%s)  select %s from [%s].[dbo].[customer] where  %s'
                    r' and  ccuscode not in (select ccuscode from   [%s].[dbo].[customer])'
                    %(targetData,Table.table['customer'],Table.table['customer'],sourceData,condition,targetData))
        elif(flag=='vendorclass'):
            sqlStr=(r'insert into  [%s].[dbo].[vendorclass](%s)  select %s from [%s].[dbo].[vendorclass] where  %s'
                    r' and cvccode not in (select  cvccode from  [%s].[dbo].[vendorclass])'
                    %(targetData,Table.table['vendorclass'],Table.table['vendorclass'],sourceData,condition,targetData))
        elif(flag=='vendor'):
            sqlStr=(r'insert into  [%s].[dbo].[vendor](%s)  select %s from [%s].[dbo].[vendor] where  %s and '
                    r' cvencode not in (select cvencode from [%s].[dbo].[vendor])'
                    %(targetData,Table.table['vendor'],Table.table['vendor'],sourceData,condition,targetData))
        elif(flag=='person'):
            sqlStr=(r'insert into  [%s].[dbo].[person](%s)  select %s from [%s].[dbo].[person] where  %s and '
                    r' cpersoncode  not  in (select cpersoncode from [%s].[dbo].[person])'
                    %(targetData,Table.table['person'],Table.table['person'],sourceData,condition,targetData))
        elif(flag=='hr_hi_person'):
            sqlStr=(r'insert into  [%s].[dbo].[hr_hi_person](%s)  select %s from [%s].[dbo].[hr_hi_person] where  %s and  cpsn_num not in (select cpsn_num from [%s].[dbo].[hr_hi_person] )'
                    %(targetData,Table.table['hr_hi_person'],Table.table['hr_hi_person'],sourceData,condition,targetData))
        elif(flag=='department'):
            sqlStr=(r'insert into [%s].[dbo].[department](%s) select %s from  [%s].[dbo].[department] where %s '
                    r' and cdepcode not in (select  cdepcode from  [%s].[dbo].[department])'
                   %(targetData,Table.table['department'],Table.table['department'],sourceData,condition, targetData))
        try:
            self.cursor.execute(sqlStr)
            self.conn.commit()
            return 'success'
        except:
            return 'fail'
    #插入凭证专用方法
    #sourceData:源数据库 targetData：目标数据库    condition:插入条件
    def InsertGl_vch(self,sourceData,targetData,condition):
        #得到最大Ino_id
        maxIno_id=0
        ino_id=self.selTable(targetData,'1=1','maxIno_id')
        if(len(ino_id)>=1):
            if(ino_id[0]!=None):
                maxIno_id=ino_id[0]
        ino_Id="'"+str(int(maxIno_id)+1)+"'"
        strs=(Table.table['gl_InsVch'] %(ino_Id))
        sqlStr=('insert into [%s].[dbo].[gl_accvouch](%s) select %s  from  [%s].[dbo].[gl_accvouch] where  %s'
                %(targetData,Table.table['gl_accvouch'],strs,sourceData,condition))
        try:
            self.cursor.execute(sqlStr)
            self.conn.commit()
            return 'success'
        except :
            return 'fail'

    #删除,根据传来的flag进行查询 flag='code','customer','vendorclass','vendor','person','hr_hi_person'
    #targetDatabase 目标数据库  sourceData 源数据库 condition 查询条件
    def  DelTable(self,targetData,condition,flag):
        sqlStr=('delete from  [%s].[dbo].[%s] where %s'%(targetData,flag,condition))
        if(flag=='gl_accvouch'):
            sqlStr=('delete from  [%s].[dbo].[%s] where %s and ibook=0'%(targetData,flag,condition))
        try:
            self.cursor.execute(sqlStr)
            self.conn.commit()
            return 'success'
        except:
            return 'fail'
















