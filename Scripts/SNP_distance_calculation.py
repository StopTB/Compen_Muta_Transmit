#judge mutual SNP distance from sum.fas
import sys

F = open(sys.argv[1]).readlines()      #sum.fas
strainList = []
output=open("output","a+")

for i in range(len(F)):
	if i %2 ==0:
		row=F[i].rstrip()
		name=row.replace(">","")
       		strainList.append(name)
	SNPoutput=open(name,"a")
	for snp in F[i+1].rstrip():
		SNPoutput.write(snp+"\n")
	SNPoutput.close()

def judge_loci(a,b):
	if a != "N" and b!= "N" and a != "?" and b!= "?" and a != "-" and b!= "-" and a !=b:
		return 1
	else:
		return 0
 
for num1 in range(len(strainList)-1):
	ref={}
	for i,j in enumerate(open(strainList[num1]).readlines()):
		ref[i]=j.rstrip()
	for num2 in range(num1+1,len(strainList)):
		compare={}
		for i,j in enumerate(open(strainList[num2]).readlines()):
			compare[i]=j.rstrip()
		distance=0
		for loci in range(len(ref)):
			distance += judge_loci(compare[loci].upper(),ref[loci].upper())
		output.write(strainList[num1]+"VS"+strainList[num2]+"\t"+str(distance)+"\n")

                




     
