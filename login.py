#import library
import os
import csv
import sys
import time
from time import sleep

#kode warna
biru='\033[1;34m'
ijo='\033[1;32m'
cyan='\033[1;36m'
merah='\033[1;31m'
ungu='\033[1;35m'
kuning='\033[1;33m'
putih='\033[1;37m'
#waktu
bulan = ('01','02','03','04','05','06','07','08','09','10','11','12')

sekarang = time.time()
infowaktu = time.localtime(sekarang)

waktu = cyan + '    [ '+str(infowaktu[2])+'-'+str(bulan[infowaktu[1]-1])+'-'+str(infowaktu[0])+' ]'

#list untuk menyimpan sementara user & pass
pas = []

def index():
	os.system('clear')
	print('')
	print('')
	print('')
	print(merah + '        ╔══════════════════════════════════════╗')
	print(merah + '        ║             Login' + putih + ' Termux' + merah + '             ║')
	print(merah + '        ║                                      ║')
	print(putih + '        ║          ' + merah + 'Author :' + putih + ' Pandas ID          ║')
	print('        ╚══════════════════════════════════════╝')
	print(merah+'                ║'+waktu+merah+'    ║')
	print(merah+'                ╚═════════════════════╝')
	try:
		file = open('_n', 'r').read()
		file2 = open('data', 'r').read()
	except FileNotFoundError:		
		input_name()
		print('')
		print(putih+ '          ['+ijo+'•'+putih+']'+kuning+' silahkan buat username & password')
		buat_pass()
	login()
	
def buat_pass():
	print('')
	user = input(putih+'          ['+ijo+'•'+putih+']'+ijo+' username : '+kuning)	
	pasw = input(putih+'          ['+ijo+'•'+putih+']'+ijo+' password : '+kuning)
	
	pas.append(user)
	pas.append(pasw)	
	with open('data', 'w') as data:
		tulis = csv.writer(data)
		tulis.writerow(pas)

	print('')
	print(putih+'          ['+ijo+'•'+putih+']'+kuning+' username & password berhasil dibuat')
	print(putih+'          ['+ijo+'•'+putih+']'+kuning+' silahkan keluar dari termux lalu')
	print('              masuk kembali')
	print('')
	print(putih+'        ═════════ '+cyan+'[•] terima kasih [•]'+putih+' ═════════')
	exit()
	
def input_name():
	print('')
	nama = input(putih+'          ['+ijo+'•'+putih+']'+ijo+' nama kamu : '+kuning)
	file = open('_n', 'w')
	file.write(nama)

def banner():
	os.system('clear')
	file = open('_n', 'r').read()
	print('')
	print('')
	print('')
	print(merah + '        ╔══════════════════════════════════════╗')
	print(merah + '        ║             Login' + putih + ' Termux' + merah + '             ║')
	print(merah + '        ║                                      ║')
	print(putih + '        ║          ' + merah + 'Author :' + putih + ' Pandas ID          ║')
	print('        ╚══════════════════════════════════════╝')
	print(merah+'                ║'+waktu+merah+'    ║')
	print(merah+'                ╚═════════════════════╝')
	print(putih)
	exit()

def login():
	os.system('clear')
	print()
	print()
	print()	
	with open('data') as data:
		lihat = csv.reader(data, delimiter=',')
		for row in lihat:
			pas.append(row)
	
	name = open('_n', 'r').read()
	print(merah+'        ╔════════════════════════════════════════╗')		
	print(merah+'        ║        '+putih+'['+ijo+'•'+putih+']'+kuning+' Selamat Datang '+putih+'['+ijo+'•'+putih+']'+merah+'          ║')
	print('        ║                                        ║')
	print('        ║ '+putih+'['+ijo+'•'+putih+']'+kuning+' Silahkan login terlebih dahulu '+putih+'['+ijo+'•'+putih+']'+merah+' ║')
	print('        ╚════════════════════════════════════════╝')
	print(merah+'                 ║'+waktu+merah+'    ║')
	print(merah+'                 ╚═════════════════════╝')
	print('')
	user = input(putih+'            ['+ijo+'•'+putih+']'+ijo+' username : '+kuning)
	pasw = input(putih+'            ['+ijo+'•'+putih+']'+ijo+' password : '+kuning)
	print()
	if user == pas[0][0] and pasw == pas[0][1]:
		print(putih+'            ['+ijo+'•'+putih+']'+ijo+' login berhasil') 
		sleep(1)
		banner()
	elif user == pas[0][0] and pasw != pas[0][1]:
		print(putih+'            ['+merah+'!'+putih+']'+merah+' password salah')
		sleep(1)
		login()
	elif user != pas[0][0] and pasw == pas[0][1]:
		print(putih+'            ['+merah+'!'+putih+']'+merah+' username salah')
		sleep(1)
		login()
	else:
		print(putih+'            ['+merah+'!'+putih+']'+merah+'username & password salah')
		sleep(1)
		login()

index()
