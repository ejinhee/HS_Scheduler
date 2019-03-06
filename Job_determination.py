import  Job

def JobDetermine(job):
    if(job.getRawmaterialGubun()==0):#단조
        if(job.getLOKFittingSize()== 'Y'):
            return 6
        else:
            return 1
    if(job.getRawmaterialGubun()==1):#Hex bar
        if(job.getLOKFittingSize()=='Y'):
            return 7
        else:
            return 2
    if(job.getRawmaterialGubun()==2):#round bar
        return 3

    if(job.getRawmaterialGubun()==3):#square bar
        return 4

    if(job.getRawmaterialGubun()==4):#valve
        return 5