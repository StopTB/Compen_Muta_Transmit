import sys
import re

f1=open(sys.argv[1]).readlines()   #strain distance
f2=open(sys.argv[2]).readlines()   #distance <= 12 strain list
f3=open("rough_transmission_chain","a")

sum_chain_list=[i.rstrip().split()[0] for i in f1 if int(i.rstrip().split()[1])<=12]

def find_transmission_strain(strain):
	cycle_strain=[]
	match_strain=[]
	True_strain=[i for i in sum_chain_list if i.startswith(strain+"VS") or i.endswith("VS"+strain)]
	for item in True_strain:
		temp=re.sub("VS","",item)
		sum_chain_list.remove(item)
		if temp[:len(strain)] == strain:
			match_strain.append(temp[len(strain):])
			cycle_strain.append(temp[len(strain):])
		else:
			match_strain.append(temp[0:len(temp)-len(strain)])
			cycle_strain.append(temp[0:len(temp)-len(strain)])
	if len(cycle_strain) > 0:
		for a in range(len(cycle_strain)):
			for b in range(len(cycle_strain)):
				try:
					sum_chain_list.remove(cycle_strain[a]+"VS"+cycle_strain[b])
				except ValueError as e:
					pass
		for i in cycle_strain:
			match_strain.extend(find_transmission_strain(i))
	return set(match_strain)
#A will be included in a transmission chain B if distance bewteen A and (any strain in B) is <=12
temp=[]

for i in f2:
	i=i.rstrip()
	if i not in temp:
		a=list(find_transmission_strain(i))
		a.append(i)
		temp.extend(a)
		for strain in a:
			f3.write(strain+"\t")
		f3.write("\n")

	else:
		pass
