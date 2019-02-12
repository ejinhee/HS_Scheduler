

class Job:
    def __init__(self):
        self.workno=0
        self.workdate=0
        self.deliverydate=0
        self.goodcd=0
        self.goodno =0
        self.orderqty =0
        self.rawmaterialgubun = 0
        self.spec=0
        self.processcd=0 #몇차까지 있는지
        self.cycletime = []
        self.required_time= [] #1차, 2차, 3차 걸리는시간
        self.possible_time = 0 # 현재 job_state에 있는 차수작업 가능한시간
        self.job_state = 0 #현재 배정해야 할 작업 차수

        self.isFinish = False
        self.rawmaterialcd=0
        self.lokfitting=0
        self.lokfittingsize=0
    def __repr__(self):
        return repr((self.workno,self.workdate,self.deliverydate,self.goodcd,self.goodno,self.orderqty,self.rawmaterialgubun,self.spec,self.processcd,self.cycletime,self.required_time,self.possible_time,self.job_state,self.isFinish,self.rawmaterialcd,self.lokfitting,self.lokfittingsize))

    def __iter__(self):
        return self

    def setRawmaterialCd(self,cd):
        self.rawmaterialcd=cd
    def getRawmaterialCd(self):
        return self.rawmaterialcd

    def setLOKFitting(self,lok):
        self.lokfitting = lok
    def getLOKFitting(self):
        return self.lokfitting
    def setLOKFittingSize(self,size):
        self.lokfittingsize = size
    def getLOKFittingSize(self):
        return self.lokfittingsize


    def setWorkNo(self,workno):
        self.workno = workno
    def getWorkNo(self):
        return self.workno

    def setWorkDate(self,workdate):
        self.workdate = workdate
    def getWorkDate(self):
        return self.workdate

    def setDeliveryDate(self,deliverydate):
        self.deliverydate = deliverydate
    def getDeliveryDate(self):
        return self.deliverydate

    def setGoodNo(self,goodno):
        self.goodno = goodno
    def getGoodNo(self):
        return self.goodno

    def setGoodCd(self,goodcd):
        self.goodcd = goodcd
    def getGoodCd(self):
        return self.goodcd

    def setOrderQty(self,orderqty):
        self.orderqty = orderqty
        if (self.cycletime != 0):
            for i in range(len(self.required_time)):
                self.required_time[i] = int(float(self.orderqty) * float(self.cycletime[i]))
    def getOrderQty(self):
        return self.orderqty

    def setRawmaterialGubun(self,gubun):
        self.rawmaterialgubun = gubun
    def getRawmaterialGubun(self):
        return self.rawmaterialgubun

    def setSpec(self,spec):
        self.spec = spec
    def getSpec(self):
        return self.spec

    def setProcessCd(self,processcd):
        self.processcd = processcd
    def getProcessCd(self):
        return self.processcd

    def setCycletime(self,Cycletime):
        self.Cycletime = Cycletime
        if (self.orderqty != 0):
            for i in range(len(self.Cycletime)):
                self.required_time.append(int(float(self.orderqty) * float(self.Cycletime[i])))

        self.setProcessCd(0) # 0일경우 1차,2차,3차 모두 포함
        self.setPossibleTime(0)
        self.job_state = 1

    def getCycletime(self):
        return self.Cycletime

    def getRequiredTime(self):
        return self.required_time

    def setPossibleTime(self,time):
        self.possible_time = time
    def getPossibleTime(self):
        return self.possible_time

    def setJobState(self,state):
        self.job_state = state
    def getJobState(self):
        return self.job_state



    def jobFinish(self):
        self.isFinish = True
    def jobCheck(self):
        return self.isFinish

    def printJob(self):
        print("Workno:",end="")
        print(self.getWorkNo())
        print("WorkDate:",end="")
        print(self.getWorkDate(),end=" WorkEnd:")
        print(self.getDeliveryDate())
        print(self.getGoodNo(),end=" ")
        print(self.getSpec(),end=" ")
        print(self.getRequiredTime())

