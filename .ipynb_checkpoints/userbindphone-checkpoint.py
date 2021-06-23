{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1f49cfff",
   "metadata": {},
   "outputs": [],
   "source": [
    "from ciscoaxl import axl\n",
    "\n",
    "cucm = '10.8.85.190'\n",
    "username = 'axl'\n",
    "password = '1234'\n",
    "version = '11.5'\n",
    "ucm = axl(username,password,cucm,version)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "a1eb5521",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{4A31CAF7-8FD8-D951-0580-6C685410B2A9} davar 417\n",
      "{AEE5B98C-EB39-2829-9EC9-635AC4A02B83} ghaderi 987\n",
      "{DE463BFD-6286-0F68-CCFE-4C8E21D582D5} Shaida None\n",
      "{045A59CA-25EC-0022-A118-506BD545FF94} tommy 645\n",
      "{CE9BDD20-5B3C-B5F7-652C-38EAD8AF00E1} Meetings None\n",
      "{B83548BC-6179-786D-7FAA-35AC2D0037D5} S.Moshiri None\n",
      "{9B683683-7C87-7011-9C31-6CAF55021908} h.mirzaei 816\n",
      "{59A84C79-731E-68B7-F3F1-45833C5C508A} CEO-SiteA 640\n",
      "{971F6C52-A00B-EB82-473E-69D27709E993} Staff-SiteA 520\n",
      "{07583B79-5269-EA46-AC63-98AF5CF6CA92} b.babalhavaeji None\n",
      "{\n",
      "    'return': '{4A31CAF7-8FD8-D951-0580-6C685410B2A9}',\n",
      "    'sequence': None\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "filter = {'tagfilter' :{'userid':'','uuid':'', 'telephoneNumber':''}}\n",
    "users = ucm.get_users(**filter)\n",
    "for u in users:\n",
    "    print(u.uuid, u.userid, u.telephoneNumber)\n",
    "#print(ucm.update_user(userid='davar', firstName='hasan'))\n",
    "filterphone={'tagfilter' :{'name':'', 'lines:' }}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88015125",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
