import CNC

def getForgingCNC(cncs):
    cncs_forging = []
    for cnc in cncs:
         if(cnc.getShape() == "2JAW"):
             cncs_forging.append(cnc)

    return cncs_forging

def getHexCNC(cncs):
    cncs_hex = []
    for cnc in cncs:
        if(cnc.getShape() == "3JAW"):
            cncs_hex.append(cnc)

    return cncs_hex

def getRoundCNC(cncs):
    cncs_round = []
    for cnc in cncs:
        if(cnc.getShape() == "3JAW" and cnc.isCoret() == "false"):
            cncs_round.append(cnc)

    return cncs_round

def getSquareCNC(cncs):
    cncs_square = []
    for cnc in cncs:
        if(cnc.getShape() == "2JAW"):
            cncs_square.append(cnc)

    return cncs_square

def getValveCNC(cncs):
    cncs_valve = []
    valve_cncnum_list = [1,2,3,32,33,34,37,38,44]
    for cnc in cncs:
        for num in valve_cncnum_list:
            if(cnc.getCNCnumber()== num ):
                cncs_valve.append(cnc)
                break

    return cncs_valve