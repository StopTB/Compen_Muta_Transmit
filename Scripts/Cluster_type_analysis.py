import re
import sys

f1=open("rough_transmission_chain").readlines()
f2=open("C_type_cluster_size","a")
f3=open("M_type_cluster_size","a")
f4=open("N_type_cluster_size","a")
f5=open(sys.argv[1]).readlines()      #SNP_compare_outcome
tran_list=[i.rstrip().split()[0] for i in f5 if int(i.rstrip().split()[1])<=12]
C_type_num=0
N_type_num=0
M_type_N=0
M_type_C=0
M_type_N_substract=0
M_type_C_substract=0

def find_transmission_chain(strain_list):
	if len(strain_list) == 1:
		return len(strain_list)
	else:
		combination_chain=[strainA+"VS"+strainB for strainA in strain_list for strainB in strain_list if strainA != strainB]
		meet_chain=[i for i in combination_chain if i in tran_list]
		strain_in_chain=[]
		for i in meet_chain:
			strain_in_chain.extend(i.split("VS"))
		return len(set(strain_in_chain))
		
	
for row in f1:
	row=row.rstrip().split()
	prefix=[re.split("_",item)[-2]+"_"+re.split("_",item)[-1] if "rpo" in re.split("_",item)[-1] else "" for item in row]
	if len(set(prefix)) == 1 and all([re.search("rpo",i) for i in set(prefix)]) == True:
		f2.write(str(len(row))+"\n")
		C_type_num+=len(row)
	elif any([re.search("rpo",i) for i in set(prefix)]) == True:
		f3.write(str(len(row))+"\n")
		if len(row) == 2:
			M_type_C_substract+=len([i for i in row if "rpo" in i])
			M_type_N_substract+=len([i for i in row if "rpo" not in i])
		else:
			C_prefix=[i for i in set(prefix) if "rpo" in i]
			N_strain=[i for i in row if "rpo" not in i]
			a=find_transmission_chain(N_strain)
			M_type_N+=int(a)
			M_type_N_substract+=len(N_strain)-int(a)
			for prefix_type in C_prefix:
				C_strain=[i for i in row if prefix_type in i]
				b=find_transmission_chain(C_strain)
				if int(b) == 1:
					M_type_C_substract+=int(b)
				else:
					M_type_C+=int(b)
					M_type_C_substract+=len(C_strain)-int(b)
	else:		
		f4.write(str(len(row))+"\n")
		N_type_num+=len(row)

print("C_type_num: "+str(C_type_num))
print("N_type_num: "+str(N_type_num))
print("M_type_N: "+str(M_type_N))
print("M_type_C: "+str(M_type_C))
print("M_type_N_substract: "+str(M_type_N_substract))
print("M_type_C_substract: "+str(M_type_C_substract))

