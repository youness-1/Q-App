def getdp(x):
	o=[5.46,06.11,6.31,7.06,7.31,8.01,8.27,8.57,09.27,09.57,10.27,10.57,11.27,11.57,12.32,13.11,13.37,14.02,14.27,14.57,15.27,15.57,16.27,16.57,17.27,17.57,18.27,19.02,19.32,20.07]
	now=float(x)
	i=0.0
	out="DMI-PSG Prossimo Q: "
	for i in o:
		if now < float(i):
			out=out+str(i)[0]+str(i)[1]+str(i)[2]+str(i)[3]+str(i)[4]+"\nAltrimenti c'è quello delle ore: "
			if o.index(i)==len(o)-1:
				out+str(o[0])[0]+str(o[0])[1]+str(o[0])[2]+str(o[0])[3]+str(o[0])[4]
			else:
				out=out+str(o[o.index(i)+1])[0]+str(o[o.index(i)+1])[1]+str(o[o.index(i)+1])[2]+str(o[o.index(i)+1])[3]+str(o[o.index(i)+1])[4]
			return out
	out=out+str(o[0])[0]+str(o[0])[1]+str(o[0])[2]+str(o[0])[3]+str(o[0])[4]
	return out
def getpd(x):
	o=[6.10,6.40,7.10,7.28,08.05,8.28,9.03,9.33,10.03,10.33,11.03,11.33,12.03,12.33,12.53,13.43,14.01,14.33,15.03,15.33,16.03,16.33,17.03,17.33,18.03,18.33,19.03,19.23,20.03,20.33]
	now=float(x)
	i=0.0
	out="PSG-DMI Prossimo Q: "
	for i in o:
		if now < float(i):
			out=out+str(i)[0]+str(i)[1]+str(i)[2]+str(i)[3]+str(i)[4]+"\nAltrimenti c'è quello delle ore: "
			if o.index(i)==len(o)-1:
				out=out+str(o[0])[0]+str(o[0])[1]+str(o[0])[2]+str(o[0])[3]+str(o[0])[4]
			else:
				out=out+str(o[o.index(i)+1])[0]+str(o[o.index(i)+1])[1]+str(o[o.index(i)+1])[2]+str(o[o.index(i)+1])[3]+str(o[o.index(i)+1])[3]
			return out
	out=out+str(o[0])[0]+str(o[0])[1]+str(o[0])[2]+str(o[0])[3]+str(o[0])[4]
	return out