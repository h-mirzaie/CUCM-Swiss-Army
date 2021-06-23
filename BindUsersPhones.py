from ciscoaxl import axl

cucm = '10.8.85.190'
username = 'axl'
password = '1234'
version = '11.5'
ucm = axl(username,password,cucm,version)
for name in ucm.get_users():
       print(name.telephoneNumber)
for phone in ucm.get_phones():
    print(phone.name)

user = ucm.get_user(userid='davar')
print(user.userid)
mydn=(user.telephoneNumber)
print(mydn)
TL=(user.associatedDevices)
print(TL)
#for phone in ucm.get_phones():
    #myphone=phone.lines
    #DN=(myphone['line'][0]['dirn']['pattern'])
    #print(DN)
    #print(phone.lines)

phone=ucm.get_phone(name='SEP74A02FC0E2B8')
mydict=phone.lines
DN=(mydict['line'][0]['dirn']['pattern'])
print(DN)
myphone=phone.name
print(myphone)
ucm.update_user(user_id='davar', firstName='hasan')
#if TL==None and mydn==DN:
  #  ucm.update_user(user_id='davar', firstName='hasan')
 #   print("no assign")
    

#else:
   # print("assign")

#print(mydict)
#mydict=str(mydict)

#if DN == TL:



#with open("D:/Python/Test-With-Sina/data_file.json", "w") as write_file:
   # json.dump(mydict, write_file)
#json_string=json.dumps(mydict)
#print(json_string)
#with open("D:/Python/Test-With-Sina/data_file.json", 'r') as f:
#    distros_dict = json.load(f)


#list1=distros_dict[1]
#print(list1)
#for distro in distros_dict:
    #print(distro['line'])


#f=open('D:/Python/Test-With-Sina/line.txt', 'r')
#f=str(f)
#json_file=json.load(f)
#print(json_file)
#f.close()


#with open('D:/Python/Test-With-Sina/line.txt') as json_file:
#    data = json.load(json_file)
#    for i in data['line']:
#        print(i)
    
#f= open('D:/Python/Test-With-Sina/line.json', 'w')
#f.write(mydict)

#print(mydict)

#print(mydict[line].0)
#x=mydict.values()
#line1=mydict['line']
#print(mydict)

#x=line1{}.keys()
#print(x)

#for phone in ucm.get_phones():
#   print(phone.model)