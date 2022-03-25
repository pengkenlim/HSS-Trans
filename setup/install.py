import os

print("Checking if required programs are installed...")
programdir=os.path.join(os.getcwd(),"programs")

#installing aspera if not installed
installpath= os.path.join(programdir,"aspera")
if not os.path.exists(installpath):
	print("Downloading and installing Aspera CLI into programs directory...")
	os.system("wget https://download.asperasoft.com/download/sw/cli/3.9.2/ibm-aspera-cli-3.9.2.1426.c59787a-linux-64-release.sh -O trashme.sh")
	os.system(f"sed -i \'s|~/.aspera|{installpath}|g\' trashme.sh")
	os.system("bash trashme.sh")
	os.system("rm trashme.sh")
else:
	print("Aspera found.")


#installing soapdenovotrans if not installed
installpath = os.path.join(programdir, "SOAPdenovo-Trans-1.0.4")
if not os.path.exists(installpath):
	print("Downloading and installing SOAPdenovo-Trans into programs directory.")
	os.system("wget https://github.com/aquaskyline/SOAPdenovo-Trans/archive/refs/tags/1.0.4.tar.gz -O trashme.tar.gz")
	os.system("tar -xf trashme.tar.gz")
	os.system("rm trashme.tar.gz")
	os.system(f"mv SOAPdenovo-Trans-1.0.4 {installpath}")
	os.system(f"cd {installpath} ; bash make.sh" )
else:
	print("SOAPdenovo-Trans found.")


#installing fastp if not installed
installpath= os.path.join(programdir, "fastp")
if not os.path.exists(installpath):
	print("Downloading and installing fastp into programs directory")
	os.system("wget http://opengene.org/fastp/fastp.0.23.2 -O fastp")
	os.system("chmod a+x fastp")
	os.system(f"mv fastp {installpath}")
else:
	print("Fastp found.")


#installing CD-HIT if not installed
installpath= os.path.join(programdir, "CD-HIT")
if not os.path.exists(installpath):
	print("Downloading and installing CD-HIT into programs directory")
	os.system("wget https://github.com/weizhongli/cdhit/releases/download/V4.8.1/cd-hit-v4.8.1-2019-0228.tar.gz -O trashme.tar.gz")
	os.system("tar -xf trashme.tar.gz")
	os.system("rm trashme.tar.gz")
	os.system(f"mv cd-hit-v4.8.1-2019-0228 {installpath}")
else:
	print("CD-HIT found.")

#installing Transdecoder if not installed
installpath= os.path.join(programdir, "TransDecoder")
if not os.path.exists(installpath):
	print("Downloading and installing TransDecoder into programs directory")
	os.system("wget https://github.com/TransDecoder/TransDecoder/archive/refs/tags/TransDecoder-v5.5.0.tar.gz -O trashme.tar.gz")
	os.system("tar -xf trashme.tar.gz")
	os.system("rm trashme.tar.gz")
	os.system(f"mv TransDecoder-TransDecoder-v5.5.0 {installpath}")
else:
	print("TransDecoder found.")
    
 
installpath= os.path.join(programdir, "ORFfinder")
if not os.path.exists(installpath):
    print("Downloading and installing ORFfinder into programs directory")
    os.system("wget https://ftp.ncbi.nlm.nih.gov/genomes/TOOLS/ORFfinder/linux-i64/ORFfinder.gz")
    os.system("gunzip ORFfinder.gz")
    os.system(f"mv ORFfinder {installpath}")



