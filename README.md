# Compen_Muta_Transmit
Compen_Muta_Transmit repository contains all the python scripts that were written and used in the article of "Have Compensatory Mutations Actually Fueled Multidrug-resistant Tuberculosis Transmission?". The abstract of this article and introduction of those python scripts can be found below.

# This study was perfromed by 
Qingyun Liu*, Tianyu Zuo*, Peng Xu, Qi Jiang, Jie Wu, Mingyu Gan, Chongguang Yang, Ravi Prakash, Guofeng Zhu, Howard E. Takiff, Qian Gao

*Equal contributions

# Abstract of this Article
It has been suggested that compensatory mutations can promote multidrug-resistant tuberculosis (MDR-TB) transmission, but their role in facilitating recent transmission of MDR-TB is unclear. To investigate the epidemiological significance of compensatory mutations, we analyzed a four-year population-based collection of MDR-TB strains from Shanghai, China, and 1,346 published global MDR-TB strains. We report that MDR-TB strains with compensatory mutations in rpoA, rpoB or rpoC genes were not more frequently clustered, nor found in larger clusters than those without compensatory mutations. Our results suggest that compensatory mutations are not a major contributor to the current epidemic MDR-TB.

# Usage of the python scripts

1. Cluster_type_analysis.py
   
   This script was written to determine the cluster type that a given transmission cluster belongs to.
   
   Usage: python3 Cluster_type_analysis.py XXXXXX

2. Identify_transmission_cluster.py
   
   This script was written to identify transmission clusters in a given M. tuberculosis WGS dataset.
   
   Usage: python3 Identify_transmission_cluster.py XXXXXX
   
3. ML_inde_evol_events.py and NJ_inde_evol_events.py
   
   These two scripts is to verify whether a given putative compensatory mutation have evolved at least twice independently.
   
   Usage: python3 ML_inde_evol_events.py(or NJ_inde_evol_events.py) phylogenetic_tree.nwk strain_index.txt
   ("phylogenetic_tree.nwk" refers to the tree file, "strain_index.txt" refers to a strain list that listed all the isolates harboring the mutation of interest)
 
 4. SNP_distance_calculation.py
    
    This script is written to calculate the each pairwise SNP distance of all M. tuberculosis isolates analyzed.
    
    Usage: python3 SNP_distance_calculation.py all_strains.fa
   ("all_strains.fa" refers to the fasta file that was used for phylogentic tree reconstruction)
