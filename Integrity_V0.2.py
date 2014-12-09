import os
import hashlib
import re
import smtplib
import socket
from email.mime.text import MIMEText
curdir='C:\\Windows','C:\\Windows\\System32','C:\\Windows\\SysWoW64','C:\\Windows\\System32\\Drivers'
WriteC=''
ResultC=''
def md5(filename):
	try:
		fileHandle=open(filename,"rb")
	except IOError:
		return
	md5hash=hashlib.md5()
	while True:
		data=fileHandle.read()
		if not data:
			break
		md5hash.update(data)
	fileHandle.close()
	return md5hash.hexdigest()

def check():
	try:
		WriteF=open("c:\\sysops\\pchunter\\oldsum.txt",'rt')
		WriteF.close()
		resultC=1

	except IOError:
		resultC=0

	
	return (resultC)


HOST='10.10.10.215'
Tat=''
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)
MailL=open('c:\\sysops\\pchunter\\MailList.txt','r')

for t in MailL.readlines():
	Tat+=t

SplitT=Tat.split('\n')
me=SplitT[0]
you=SplitT[1]
MailL.close()
ExlT=''
ExceptList=open('c:\\sysops\\pchunter\\ExceptList.txt','r')
for Exl in ExceptList.readlines():
	ExlT+=Exl

ExlSpliT=ExlT.split('\n')
contin=0
for cur in curdir:
	Files = [f for f in os.listdir(cur) if os.path.isfile(os.path.join(cur,f))]
	for FileL in Files:
		FileFL=os.path.join(cur,FileL)
		result=md5(FileFL)
		for tat2 in ExlSpliT:
			if FileFL == tat2:
				contin=1
				continue
		if contin==1:
			contin=0
			continue
		WriteC+=(FileFL+":"+str(result)+"\n")

resultC2=check()
if resultC2:
	WriteF=open('c:\\sysops\\pchunter\\oldsum.txt','r+')
	SearchFT=WriteF.read()
	power=WriteC.split('\n')
	FileSwitch=0
	for SearchT in power:
		FindR=SearchFT.find(SearchT)
		if FindR>=0:
			continue
		else :
			ResultC+=(SearchT+'\n')
			FileSwitch=1
				
	
	if FileSwitch>0:

		tap=open('c:\\sysops\\pchunter\\ChangeMD5.txt','w+')
		tap.write(ResultC)
		tap.close()
		print (ResultC)
		contents=hostname+":"+ip+" "+ResultC
		msg=MIMEText(contents, _charset='euc-kr')
		msg['Subject']='Icarus Integrity Change!!'
		msg['From']=me
		msg['To']=you
		try:
			s=smtplib.SMTP(HOST)
			s.sendmail(me, [you], msg.as_string())
			s.quit()
		except:
			print ("sendmail error")
			

	WriteF.seek(0)
	WriteF.write(WriteC)
	WriteF.close()

else:
	WriteF=open('c:\\sysops\\pchunter\\oldsum.txt','w')
	WriteF.write(WriteC)
	WriteF.close()


