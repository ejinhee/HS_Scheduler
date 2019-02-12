import CNC

def getForgingCNC(cncs):
    cncs_forging = []
    for cnc in cncs:
         if(cnc.getShape() == "2JAW"): ## 2JAW cnc
             cncs_forging.append(cnc)

    return cncs_forging

def getHexCNC(cncs):
    cncs_hex = []
    for cnc in cncs:
        if(cnc.getShape() == "3JAW"):## 3JAW cnc
            cncs_hex.append(cnc)

    return cncs_hex

def getRoundCNC(cncs):
    cncs_round = []
    for cnc in cncs:
        if(cnc.getShape() == "3JAW" and cnc.isCoret() == "false"): ## 3 JAW이면서 코렛아닌 cnc
            cncs_round.append(cnc)

    return cncs_round

def getSquareCNC(cncs):
    cncs_square = []
    for cnc in cncs:
        if(cnc.getShape() == "2JAW"): ##2JAW cnc
            cncs_square.append(cnc)

    return cncs_square

def getValveCNC(cncs):
    cncs_valve = []
    valve_cncnum_list = [1,2,3,32,33,34,37,38,44] ##  밸브선작업 cnc리스트
    for cnc in cncs:
        for num in valve_cncnum_list:
            if(cnc.getCNCnumber()== num ):
                cncs_valve.append(cnc)
                break

    return cncs_valve

def getLokfittingForging(cncs):
    cncs_lokfitting_forging_size = []
    lokfitting_size_forging_num_list = [10,15]
    for cnc in cncs:
        for num in lokfitting_size_forging_num_list:
            if(cnc.getCNCnumber() == num):
                cncs_lokfitting_forging_size.append(cnc)
                break

    return cncs_lokfitting_forging_size

def getLokfittingHex(cncs):
    cncs_lokfitting_hex_size = []
    lokfitting_size_hex_num_list = [8,9,11,12,13]
    for cnc in cncs:
        for num in lokfitting_size_hex_num_list:
            if(cnc.getCNCnumber() == num):
                cncs_lokfitting_hex_size.append(cnc)
                break

    return cncs_lokfitting_hex_size

def get3941cnc(cncs):
    cncs_3941 = []
    for cnc in cncs:
        if(cnc.getCNCnumber()== 39 or cnc.getCNCnumber() == 41):
            cncs_3941.append(cnc)

    return cncs_3941

def get4042cnc(cncs):
    cncs_4042 = []
    for cnc in cncs:
        if(cnc.getCNCnumber()== 40 or cnc.getCNCnumber() == 42):
            cncs_4042.append(cnc)

    return cncs_4042