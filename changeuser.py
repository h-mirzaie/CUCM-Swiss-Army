from ciscoaxl import axl
import yaml



with open('info.yml', 'r') as stream:
    yamlInfo = yaml.safe_load(stream)
yamlConfig = yamlInfo['config']
cucm = yamlConfig['cucm']
username = yamlConfig['username']
password = yamlConfig['password']
version = yamlConfig['version']
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






