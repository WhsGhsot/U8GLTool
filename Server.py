#!C:\Users\Administrator\AppData\Local\Programs\Python\Python36\python.exe
import cgi
from OpeDatabase import *
from  Database import *
import  json
form =cgi.FieldStorage()
opeDatabase=OpeDatabase()
#接收前台传来的连接数据库信息
print('Content-type:text/html\n')
flag=form['flag'].value
if(flag=='connServer'):
    serName=form['serName'].value
    serPas=form['serPas'].value
    if(serPas=='空'):
        serPas=''
    if(serName=='空'):
        serName=''
    status=opeDatabase.connData(server=serName,password=serPas)
    if(status=='fail'):
        print('fail')
    else:
        databases=opeDatabase.selDatabases('master','1=1')
        jsonStr=json.dumps(databases)
        print(jsonStr)

elif(flag=='ino_ids'):
    serName=form['serName'].value
    serPas=form['serPas'].value
    if(serPas=='空'):
        serPas=''
    if(serName=='空'):
        serName=''
    opeDatabase.connData(server=serName,password=serPas)
    sourceDatabase=form['sourceDatabase'].value
    targetDatabase=form['targetDatabase'].value
    iyear=form['iyear'].value
    iperiod=form['iperiod'].value
    condition=(' iyear=%s and iperiod=%s'%(iyear,iperiod))

    data=opeDatabase.selIno_ids(sourceDatabase,condition)
    #导入档案
    condition=(' ccode not in (select ccode from  [%s].[dbo].[gl_accvouch] where  iyear=%s and iperiod=%s)'
               %(targetDatabase,iyear,iperiod))
    opeDatabase.InsCode(sourceDatabase,targetDatabase,condition)

    condition=(' cdepcode not in (select cdept_id from  [%s].[dbo].[gl_accvouch] where  iyear=%s and iperiod=%s)'
               %(targetDatabase,iyear,iperiod))
    opeDatabase.InsDepartment(sourceDatabase,targetDatabase,condition)


    condition=(' ccuscode not in (select ccus_id from  [%s].[dbo].[gl_accvouch] where  iyear=%s and iperiod=%s)'
               %(targetDatabase,iyear,iperiod))
    opeDatabase.InsCustomer(sourceDatabase,targetDatabase,condition)

    opeDatabase.InsVc(sourceDatabase,targetDatabase,'1=1')

    condition=(' cvencode not in (select csup_id  from  [%s].[dbo].[gl_accvouch] where  iyear=%s and iperiod=%s)'
               %(targetDatabase,iyear,iperiod))
    opeDatabase.InsVendor(sourceDatabase,targetDatabase,condition)

    condition=(' cpersoncode not in (select cperson_id from  [%s].[dbo].[gl_accvouch] where  iyear=%s and iperiod=%s)'
               %(targetDatabase,iyear,iperiod))
    opeDatabase.InsPerson(sourceDatabase,targetDatabase,condition)
    opeDatabase.InsHip(sourceDatabase,targetDatabase,'1=1')
    if(len(data)==0):
        print('fail')
    else:
        jsonStr=json.dumps(data)
        print(jsonStr)
elif(flag=='copy'):
    serName=form['serName'].value
    serPas=form['serPas'].value
    if(serPas=='空'):
        serPas=''
    if(serName=='空'):
        serName=''
    opeDatabase.connData(server=serName,password=serPas)
    sourceDatabase=form['sourceDatabase'].value
    targetDatabase=form['targetDatabase'].value
    iyear=form['iyear'].value
    iperiod=form['iperiod'].value
    ino_id=form['ino_id'].value
    condition=(' iyear=%s and iperiod=%s and ino_id=%s'%(iyear,iperiod,ino_id))
    status=opeDatabase.InsertGl_vch(sourceDatabase,targetDatabase,condition)
    print(status)
elif(flag=='clear'):
    serName=form['serName'].value
    serPas=form['serPas'].value
    if(serPas=='空'):
        serPas=''
    if(serName=='空'):
        serName=''
    opeDatabase.connData(server=serName,password=serPas)
    targetDatabase=form['targetDatabase'].value
    status=opeDatabase.DelGlVch(targetDatabase,'1=1')
    print(status)
elif(flag=='codeInput'):
    serName=form['serName'].value
    serPas=form['serPas'].value
    if(serPas=='空'):
        serPas=''
    if(serName=='空'):
        serName=''
    opeDatabase.connData(server=serName,password=serPas)
    sourceDatabase=form['sourceDatabase'].value
    targetDatabase=form['targetDatabase'].value
    status=opeDatabase.InsCode(sourceDatabase,targetDatabase,'1=1')
    print(status)
elif(flag=='customerInput'):
    serName=form['serName'].value
    serPas=form['serPas'].value
    if(serPas=='空'):
        serPas=''
    if(serName=='空'):
        serName=''
    opeDatabase.connData(server=serName,password=serPas)
    sourceDatabase=form['sourceDatabase'].value
    targetDatabase=form['targetDatabase'].value
    status=opeDatabase.InsCustomer(sourceDatabase,targetDatabase,'1=1')
    print(status)
elif(flag=='vendorInput'):
    serName=form['serName'].value
    serPas=form['serPas'].value
    if(serPas=='空'):
        serPas=''
    if(serName=='空'):
        serName=''
    opeDatabase.connData(server=serName,password=serPas)
    sourceDatabase=form['sourceDatabase'].value
    targetDatabase=form['targetDatabase'].value
    status=opeDatabase.InsVc(sourceDatabase,targetDatabase,'1=1')
    status=opeDatabase.InsVendor(sourceDatabase,targetDatabase,'1=1')
    print(status)
elif(flag=='personInput'):
    serName=form['serName'].value
    serPas=form['serPas'].value
    if(serPas=='空'):
        serPas=''
    if(serName=='空'):
        serName=''
    opeDatabase.connData(server=serName,password=serPas)
    sourceDatabase=form['sourceDatabase'].value
    targetDatabase=form['targetDatabase'].value
    status=opeDatabase.InsPerson(sourceDatabase,targetDatabase,'1=1')
    status=opeDatabase.InsHip(sourceDatabase,targetDatabase,'1=1')
    print(status)
elif(flag=='departmentInput'):
    serName=form['serName'].value
    serPas=form['serPas'].value
    if(serPas=='空'):
        serPas=''
    if(serName=='空'):
        serName=''
    opeDatabase.connData(server=serName,password=serPas)
    sourceDatabase=form['sourceDatabase'].value
    targetDatabase=form['targetDatabase'].value
    status=opeDatabase.InsDepartment(sourceDatabase,targetDatabase,'1=1')
    print(status)




