from re import search
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
filter_IPPhone = {'tagfilter' :{'name': ''}}
Directory_list = []
device=[]
Associate_Devices={'device':[]}

for p in ucm.get_phones(**filter_IPPhone):
    Phone_Name = (p.name)
    phone = (ucm.get_phone(name=Phone_Name))
    Phone_Lines = phone.lines
    Directory_Number = (Phone_Lines['line'][0]['dirn']['pattern'])
    Associate_Devices={'device':[]}
    
    for u in users:
        UserID = u.userid
        Telephone = (u.telephoneNumber)

        if Directory_Number == Telephone:
            user = ucm.get_user(UserID)
            Associate_Devices=user.associatedDevices
            print(UserID, Associate_Devices, Phone_Name)

            if Associate_Devices is not None:

                for i in  Associate_Devices:

                    if Phone_Name in i :
                        break

                    else:
                        Associate_Devices['device'].append(Phone_Name)

            else:

                Associate_Devices= Phone_Name
                print('no', Associate_Devices)

            print(ucm.update_user(**{'userid':UserID, 'associatedDevices' : Associate_Devices}))
  






