from ciscoaxl import axl



cucm = '10.8.85.190'
username = 'axl'
password = '1234'
version = '11.5'
ucm = axl(username,password,cucm,version)

filter = {'tagfilter' :{'userid':'','uuid':'', 'telephoneNumber':''}}
users = ucm.get_users(**filter)

for u in users:
    telephone=(u.telephoneNumber)
    userids=(u.userid)
    for i in ucm.get_phones():
         phonename=(i.name)
         phone1=(ucm.get_phone(name=phonename))
         mydict=phone1.lines
         DN=(mydict['line'][0]['dirn']['pattern'])
         if telephone==DN:
             print(ucm.update_user(userid=userids, associatedDevices=phonename))




