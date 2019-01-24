

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
        self.processcd=0
        self.Cycletime = 0
        self.required_time=0
        self.isFinish = False
        self.rawmaterialcd=0
        self.lokfitting=0
        self.lokfittingsize=0
    def __repr__(self):
        return repr((self.workno,self.workdate,self.deliverydate,self.goodcd,self.goodno,self.orderqty,self.rawmaterialgubun,self.spec,self.processcd,self.Cycletime,self.required_time,self.isFinish,self.rawmaterialcd,self.lokfitting,self.lokfittingsize))

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
    def getLOKFitting(self):
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
        if (self.Cycletime != 0):
            self.required_time = int(float(self.orderqty) * float(self.Cycletime))
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
            self.required_time = int(float(self.orderqty) * float(self.Cycletime))
    def getCycletime(self):
        return self.Cycletime

    def getRequiredTime(self):
        return self.required_time

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
        print(self.getProcessCd(),end=" ")
        print(self.getSpec(),end=" ")
        print(self.getRequiredTime())

