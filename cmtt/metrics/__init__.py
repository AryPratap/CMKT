# Finding CMI using only tags
# N - total number of tokens exclusing independent tags
# max_cnt - count of words occuring in maximum language
# P - number of switches between langauges
# CMI of a utternace Cu = ((N-max_cnt+P)*100)/(2*N)

tags = {'0':'EN', '1':'HI', '2':'UN'}

def utteranceCMI(sentence):
	count = [0,0,0]
	listOfUtterance = sentence.split(" ")
	print(listOfUtterance)  
	count[0] = listOfUtterance.count("EN")
	count[1] = listOfUtterance.count("HI")
	count[2] = listOfUtterance.count("UN")
	print(count)
	max_cnt = max(count)
	N = count[0]+count[1]
	if N==0:
		return 0
	P = 0
	prev = listOfUtterance[0]
	for i in range(1, len(listOfUtterance)):
		if listOfUtterance[i]!='UN':
			if prev!=listOfUtterance[i]:
				P+=1
				prev = listOfUtterance[i]
	Cu = (100.0*(N-max_cnt+P))/(2.0*N)
	return Cu


def cmi(sentence):
  count = [0,0,0]
  listOfUtterance = sentence.split(" ")
  count[0] = listOfUtterance.count("EN")
  count[1] = listOfUtterance.count("HI")
  count[2] = listOfUtterance.count("UN")

  max_cnt = max(count)

  N = count[0]+count[1]+count[2]

  cmi = 100.0*(1.0 - (max_cnt)/(N - count[2]))
  return cmi