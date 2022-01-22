def strike_rate(a,b):
	sr=((a)/(b))*100
	return sr
def bats_avg(e,f):
	if f==0:
		return e
	else:
		baavg=(e)/(f)
		return baavg
def bow_avg(g,h):
	if h==0:
		return 0
	else:
		boavg=(g)/(h)
		return boavg
def econ(i,j):
	economy=(i)/(j)
	return economy
def crunrate(c,d):
	crr=((c)/(d))*6
	return crr
def rrunrate(k,l):
	rrr=((k)/(l))*6
	return rrr
print("WELCOME TO CRICKET STATISTICS")
print("\nselect a choice among below")
print("\n1-strike rate of a batsman")
print("\n2-average of a batsman in a series or his career")
print("\n3-average of a bowler in his career or a series")
print("\n4-economy of a bowler ")
print("\n5-current runrate of ateam")
print("\n6-required run rate of a team")
print("\n7-comparing two batsman")
print("\n8-comparing two bowlers")
choice=int(input(""))
if choice==1:
	print("\nenter runs scored by the batsman and number of balls he faced in a match or a series or his career respectively")
	a=int(input(""))
	b=int(input(""))
	sr=strike_rate(a,b)
	if(sr<=360):
		print("strike rate of batsman is ",sr)
	else:
		print("its impossible to score at that rate")
elif choice==2:
	print("\nenter total number of runs scored by the batsman and number of times he got out in a series or career respectively")
	e=int(input(""))
	f=int(input(""))
	baavg=bats_avg(e,f)
	print("\naverage of batsman is ",baavg)
elif choice==3:
	print("\nenter the number of runs conceeded and number of wickets taken by the bowler in a match or series or career respectively")
	g=int(input(""))
	h=int(input(""))
	boavg=bow_avg(g,h)
	print("\naverage of the bowler is ",boavg)
elif choice==4:
	print("\nenter the number of runs conceeded and number of balls bowled by a bowler in a match or series or  his career respectively")
	i=int(input(""))
	j=int(input(""))
	economy=econ(i,j)
	print("\neconomy of the bowler is ",economy)
elif choice==5:
	print("\nenter the number of runs scored by a team and balls faced by the team")
	c=int(input(""))
	d=int(input(""))
	crr=crunrate(c,d)
	print("\ncurrent run rate of team is ",crr)
elif choice==6:
	print("\nenter runs required and balls to be faced by a team respectively")
	k=int(input(""))
	l=int(input(""))
	rrr=rrunrate(k,l)
	print("\nrequired run rate is ",rrr)
elif choice==7:
	print("\nenter the two batsmans average you want to compare respectively")
	m=float(input(""))
	n=float(input(""))
	if(m>n):
		print("\nthe first batsman is better than the second one")
	elif(m==n):
		print("\nboth batsman are equal and can be compared in terms of other")
	else:
		print("\nsecond batsman is better than the first batsman")
elif choice==8:
	print("\nenter average of two bowlers you want to compare respectively")
	o=float(input(""))
	p=float(input(""))
	if(o<p):
		print("first bowler is better than the second one")
	elif(o>p):
		print("second bowler is better than the first one")
	else:
		print("compare the bowlers in terms of wickets or economy")
		