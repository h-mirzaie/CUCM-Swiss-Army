from ciscoaxl import axl

cucm = '10.8.85.190'
username = 'axl'
password = '1234'
version = '11.5'
ucm = axl(username,password,cucm,version)

filter = {'tagfilter' :{'userid':'','uuid':'', 'telephoneNumber':''}}
users = ucm.get_users(**filter)
filter_IPPhone={'tagfilter' :{'name': ''}}

Directory_list=[]
for p in ucm.get_phones(**filter_IPPhone):
    Phone_Name = (p.name)
    phone = (ucm.get_phone(name=Phone_Name))
    Phone_Lines = phone.lines
    Directory_Number = (Phone_Lines['line'][0]['dirn']['pattern'])
    Directory_list.append(Directory_Number)

for dn in Directory_list:
    for u in users:
        UserID = u.userid
        Telephone = (u.telephoneNumber)
        if dn == Telephone:
            print(ucm.update_user(userid=UserID, associatedDevices=Phone_Name))






