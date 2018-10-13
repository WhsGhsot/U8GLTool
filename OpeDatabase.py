"""中间层  传输数据"""
"""select  update insert  delete """
from Database import  *
class  OpeDatabase:


    #初始化创建数据库实例
    def __init__(self):
        self.conn=Database()
    #连接数据库,连接成功后建立游标  server 为数据库实例  password为数据库密码
    def connData(self,server,password):
        status=self.conn.ConnData(server,password)
    #数据库连接成功  生成游标
        if(status=='success'):
            self.CreateCursor()
            return 'success'
    #数据库连接失败 返回给用户
        else:
            return 'fail'

    #生成游标
    def CreateCursor(self):
        self.cursor= self.conn.CreateCursor()
    #关闭数据库
    def CloseConn(self):
        self.conn.CloseConn(self.conn)

    #选择目的账套的会计科目的id   targetDatabase为目的账套 candition为条件 --未实现
    #return  ccodes:[]
    def  selCodeId(self,targetDatabase,condition):
        return self.conn.selTable(targetDatabase,condition,'code')
    #选择目的账套的客户档案的id   targetDatabase为目的账套 candition为条件 --未实现
    #return  cccodes:[]
    def   selCusId(self,targetDatabase,condition):
       return self.conn.selTable(targetDatabase,condition,'customer')
    #选择目的账套的供应商分类的id   targetDatabase为目的账套 candition为条件 --未实现
    #return  cvccodes:[]
    def   selVCId(self,targetDatabase,condition):
        return self.conn.selTable(targetDatabase,condition,'vendorclass')
    #选择目的账套的供应商id   targetDatabase为目的账套 candition为条件
    def   selVId(self,targetDatabase,condition):
        return  self.conn.selTable(targetDatabase,condition,'vendor')
    #选择目的账套个人档案id   targetDatabase为目的账套 candition为条件 --未实现
    def   selPId(self,targetDatabase,condition):
        return  self.conn.selTable(targetDatabase,condition,'person')
    #选择目的账套部门档案id   targetDatabase为目的账套 candition为条件 --未实现
    def   selDeId(self,targetDatabase,condition):
        return  self.conn.selTable(targetDatabase,condition,'department')
    #选择目的账套人事档案的个人id   targetDatabase为目的账套 candition为条件 --未实现
    def   selHiId(self,targetDatabase,condition):
        return  self.conn.selTable(targetDatabase,condition,'hr_hi_person')
    #选择全部账套信息
    def   selDatabases(self,targetDatabase,condition):
        return  self.conn.selTable(targetDatabase,condition,'sysdatabases')
    #选择目的账套最大的ino_id
    def  selMaxIno_id(self,targetDatabase,condition):
        return  self.conn.selTable(targetDatabase,condition,'maxIno_id')
    #选择目标账套的ino_ids   return  ino_ids:[]
    def  selIno_ids(self,targetDatabase,condition):
        return  self.conn.selTable(targetDatabase,condition,'ino_id')

    #插入code  sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def InsCode(self,sourceData,targetData,condition):
        return  self.conn.InsTable(sourceData,targetData,condition,'code')
    #插入Customer  sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def InsCustomer(self,sourceData,targetData,condition):
        return self.conn.InsTable(sourceData,targetData,condition,'customer')
    #插入Vendorclass  sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def InsVc(self,sourceData,targetData,condition):
        return self.conn.InsTable(sourceData,targetData,condition,'vendorclass')
    #插入Vendor  sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def InsVendor(self,sourceData,targetData,condition):
        return self.conn.InsTable(sourceData,targetData,condition,'vendor')
    #插入person  sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def InsPerson(self,sourceData,targetData,condition):
        return self.conn.InsTable(sourceData,targetData,condition,'person')
    #插入hr_hi_person sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def InsHip(self,sourceData,targetData,condition):
        return self.conn.InsTable(sourceData,targetData,condition,'hr_hi_person')
    def InsertGl_vch(self,sourceData,targetData,condition):
        return self.conn.InsertGl_vch(sourceData,targetData,condition)
    def InsDepartment(self,sourceData,targetData,condition):
        return self.conn.InsTable(sourceData,targetData,condition,'department')

    #删除code  sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def DelCode(self,targetData,condition):
       return self.conn.DelTable(targetData,condition,'code')
    #删除Customer  sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def DelCustomer(self,targetData,condition):
        return self.conn.DelTable(targetData,condition,'customer')
    #删除Vendorclass  sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def DelVc(self,targetData,condition):
        return self.conn.DelTable(targetData,condition,'vendorclass')
    #删除Vendor  sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def DelVendor(self,sourceData,targetData,condition):
        return self.conn.DelTable(targetData,condition,'vendor')
    #删除person  sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def DelPerson(self,targetData,condition):
        return self.conn.DelTable(sourceData,targetData,condition,'person')
    #删除hr_hi_person sourceData 为源数据库   TargetData为目的数据库   candition为条件  -未实现
    def DelHip(self,targetData,condition):
        return self.conn.DelTable(targetData,condition,'hr_hi_person')
    #删除异常(未记账凭证)
    def DelGlVch(self,targetData,condition):
        return self.conn.DelTable(targetData,condition,'gl_accvouch')



