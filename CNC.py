class CNC:
    def __init__(self):
        #self.num_code = 0
        #self.shape_code = 0
        #self.type_code = 0
        self.size = []
        self.cnc_num = 0
        self.cnc_shape = 0
        self.cnc_type = 0
        self.cnc_iscoret = 0
        self.reservedTime = 0
        self.numOfJobs = 0

        self.joblist = []

    def __repr__(self):
        return repr(self.size,self.cnc_num,self.cnc_shape,self.reservedTime,self.numOfJobs,self.joblist)
    def setSize(self,size):
        self.size = size
    def setCNCnumber(self,num):
        self.cnc_num = num
    def setShape(self,shape):
        self.cnc_shape = shape
    def setType(self,type):
        self.cnc_type = type
    def setIsCoret(self,coret):
        self.cnc_iscoret = coret
    def setReservedTime(self,time):
        self.reservedTime = time
    def increaseNumOfJobs(self):
        self.numOfJobs +=1

    def getCNCnumber(self):
        return self.cnc_num
    def getNumCode(self):
        return self.num_code
    def getShapeCode(self):
        return self.shape_code
    def getTypeCode(self):
        return self.type_code
    def getSizeFrom(self):
        return self.size[0]
    def getSizeTo(self):
        if (self.size[1] == 'MAX'):
            return 1000
        else:
            return self.size[1]
    def getReservedTime(self):
        return self.reservedTime
    def getShape(self):
        return self.cnc_shape
    def getType(self):
        return self.cnc_type
    def isCoret(self):
        return self.cnc_iscoret
    def getNumOfJobs(self):
        return self.numOfJobs

    def jobAssign(self,job):
        self.joblist.append(job)
        self.numOfJobs +=1
    def printJobList(self):
        print("-------------------------------")
        print("CNC ",end="")
        print(self.getCNCnumber(),end=": ")
        print(self.getNumOfJobs(),end=" ")
        print("Jobs")
        for job in self.joblist:
            print("Workno:", end="")
            print(job.getWorkNo())
            print("WorkDate:", end="")
            print(job.getWorkDate(), end=" WorkEnd:")
            print(job.getDeliveryDate())
            print(job.getProcessCd(), end=" ")
            print(job.getSpec())
            if(job.getProcessCd() == 0):
                print("~ P",end="")
                print(len(job.getRequiredTime()),end=" ")
                print(job.getRequiredTime())
            else:
                print("P",end="")
                print(job.getProcessCd(),end=" ")
                print(job.getRequiredTime()[job.getProcessCd()-1])
        print(self.getReservedTime())
        print("-------------------------------")

    def printCode(self):
        print("CNC번호:",end="")
        print(self.cnc_num, end = " ")
        print(self.cnc_shape,end = " ")
        print(self.getSizeFrom(),end = " ~ ")
        print(self.getSizeTo())

