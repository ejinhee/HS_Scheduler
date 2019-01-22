

class Job:
    def __init__(self):
        self.workno=0
        self.workdate=0
        self.deliverydate=0
        self.goodcd=0
        self.orderqty =0
        self.gubun = 0
        self.spec=0
        self.processcd=0
        self.Cycletime = 0
        self.required_time=0
        self.isFinish = False

    def __repr__(self):
        return repr((self.workno,self.workdate,self.deliverydate,self.goodcd,self.orderqty,self.gubun,self.spec,self.processcd,self.Cycletime,self.required_time,self.isFinish))

    def __iter__(self):
        return self


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

    def setGubun(self,gubun):
        self.gubun = gubun
    def getGubun(self):
        return self.gubun

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

