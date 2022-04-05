#setting sys.path for importing modules
import os
import sys
if __name__ == "__main__":
        abspath= os.getcwd()
        parent_module= os.path.join(abspath.split("LSTrAP-denovo")[0], "LSTrAP-denovo")
        sys.path.insert(0, parent_module)

from setup import constants
import subprocess
import os
import numpy as np

def concat_rename_assemblies(assemblydir, concatpath, identifier="cds.fasta",seq_prefix_split="_cds.fasta",): 
    '''rename sequence IDs in individual assembly fasta and then concatenate them together into a single file '''
    concat_assembly= open(concatpath, "w")
    for assembly in os.listdir(assemblydir):
        if identifier in assembly:
            with open(os.path.join(assemblydir, assembly),"r") as f:
                fasta=f.read().split(">")[1:]
                fasta= [">"+ assembly.split(seq_prefix_split)[0]+"_"+str(i)+"\n"+"\n".join(seq_chunk.split("\n")[1:]) for i, seq_chunk in enumerate(fasta)]
                concat_assembly.write("".join(fasta))
    
    concat_assembly.close()
    
    
    
def launch_cdhit(concatpath, similarity, outpath, threads):
    returncode=subprocess.run([constants.cdhitpath, "-i", concatpath, "-T", str(threads), "-M", "0", "-G", "0", "-c", str(similarity), "-aS", "0.95" ,"-aL", "0.005" ,"-r","0", "-g", "1", "-o", outpath ],
    stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return returncode.returncode

            
def cluster_seq_extractor(n_threshold,pathtoclstrinfo):
    '''parsing cluster info file generated by CD-HIT-EST, 
    only retains cluster representative if number of assemblies reaches threshold'''
    with open(pathtoclstrinfo, "r") as f:
        cluster_info = f.read().split(">Cluster ")[1:]
    seq_to_retain=[]
    #iterating each cluster and quantify its consensus support from different assemblies. if consensus support > 
    for cluster in cluster_info:
        #n_consensus will contain the number of assemblies that contributed to the cluster
        n_consensus = len(set([ k.split(">")[1].split("_")[0] for k in cluster.split("\n")[1:-1]]))
        if n_consensus >= n_threshold:
            representative_seq = cluster.split("*")[0].split(">")[-1].split(".")[0]
            seq_to_retain += [representative_seq]
    return seq_to_retain
    
def fasta_subset(inputfastapath, outputfastapath, seqid):
    '''Create a subset fasta from input fasta based on seqid provided'''
    with open(inputfastapath,"r") as f:
        fasta=f.read().split(">")[1:]
        with open(outputfastapath, "w") as f:
            for line in fasta:
                if line.split("\n")[0] in seqid:
                    f.write(">"+line)

def select_CT(n_seq_list):
    ''' Find best consensus threshold based on rate of seqeunce loss. 
    Returns optimal CT as an integer'''
    array= np.array(n_seq_list)
    percentage_decrease= list((array[1:]-array[:-1])/array[:-1])
    optimum_threshold= range(1,len(n_seq_list)+1)[ percentage_decrease.index(max(percentage_decrease))]
    return optimum_threshold
    
    
def CT_from_target_CDS(n_seq_list, targetCDS):
    ''' Find consensus threshold with n_CDS similar to target n_CDS 
    Returns optimal CT as an integer'''
    array= np.array(n_seq_list)
    idx = (np.abs(array - targetCDS)).argmin()
    return idx + 1
    
