#!/usr/bin/python
#coding:utf-8
import sys
import zipfile
import shutil
import time
import datetime
import os
arg = sys.argv
del arg[0]

if(len(arg) < 3):
	print '\x1b[32m'
	print('please input zip file, exp: python /tmp/mergeZip.py haju-poker-2.0.1.zip haju-poker-2.2.1.zip haju-20180313-2.2.2 \n 1、输入的压缩文件统一放在/usr/local/var/inputzip/下面 \n 2、输出的压缩文件统一放在/usr/local/var/outputzip/下面 \n 3、/tmp/mergeZip.py为脚本的绝对路径\n 4、haju-20180313-2.2.2为最后输出的压缩文件名，不用加.zip，脚本会自动带上 \n 5、输入压缩文件支持多个，最后一个参数为输出的压缩文件名，即haju-20180313-2.2.2 \x1b[0m')
	sys.exit()
t = time.time()
t = int(t)
t = str(t)

srcDir = "/usr/local/var/inputzip/"#输入的源文件路径
outDir = '/usr/local/var/outputzip/'#输出的文件路径
desDir = '/usr/local/var/outputzip/' + t + '/'#解压之后的临时路径,用时间戳作为目录

file3 = arg.pop()#最后的输出文件名，不用带.zip

for file in arg:
	bl = os.path.exists(srcDir+ file)
	if(bl is False):
		print(srcDir+ file + '文件不存在')
		sys.exit()

for file in arg:
	z = zipfile.ZipFile(srcDir+ file, "r");
	z.extractall(desDir);

shutil.make_archive(outDir + file3, "zip", desDir)

print('输出文件路径:'+outDir + file3+'.zip')


-----09opi
