def split():
	idlist = []
	i = 0
	a = 1
	f = open('/home/jiangln/weibo/xp_uid.txt','r')
	for line0 in f:
		idlist.append(line0)
		i = i + 1
		if i % 10000 = 0:
			f1 = open('/home/jiangln/weibo/xp_uid'+ str(a) +'.txt','wt')
			for line in idlist:
				f1.write(line)
				idlist = []
			print a 
			a = a + 1

if __name__ == '__main__':
	split()