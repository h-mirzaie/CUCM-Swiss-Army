{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9e7182d7",
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
   "execution_count": 34,
   "id": "9e68afcb",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-34-e35a7d979ebe>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-34-e35a7d979ebe>\"\u001b[1;36m, line \u001b[1;32m6\u001b[0m\n\u001b[1;33m    filterphone={'tagfilter' :{'name':'', 'lines:' }}\u001b[0m\n\u001b[1;37m                                                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "filter = {'tagfilter' :{'userid':'','uuid':'', 'telephoneNumber':''}}\n",
    "users = ucm.get_users(**filter)\n",
    "for u in users:\n",
    "    print(u.uuid, u.userid, u.telephoneNumber)\n",
    "print(ucm.update_user(userid='davar', firstName='hasan'))\n",
    "filterphone={'tagfilter' :{'name':'', 'lines:' }}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b63a7590",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e392c84",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12946aec",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2290776b",
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
