import CNC_info
import AccessDB
import DB_query
import CNC_shape
import Job
import CNC
import pyodbc

import copy
import numpy as np
server = "221.161.62.124,2433"
database = "Han_Eng_Back"
username = "Han_Eng_Back"
password = "HseAdmin1991"

cncs = [] ## 전체CNC리스트
jobs = [] ## 전체작업리스트
sorted_by_deli_jobs = [] ##같은 납기일의 작업을 가지는 리스트의 리스트(2차)
same_deli_jobs = [] ## sorted_by_deli_jobs리스트를 위한 임시 리스트
start = '20181227'
end = '20181231'

CNC_info.getCNCinfo(cncs)
cursor1 = AccessDB.AccessDB(server,database,username,password)
cursor2 = AccessDB.AccessDB(server,database,username,password)
DB_query.search_job_by_deadline(jobs,start,end,cursor1,cursor2)

date = jobs[0].getDeliveryDate()
for job in jobs:
    if(job.deliverydate != date):
        sorted_by_deli_jobs.append(same_deli_jobs)
        same_deli_jobs = []
        date = job.getDeliveryDate()
        same_deli_jobs.append(job)
    else:
        same_deli_jobs.append(job)
sorted_by_deli_jobs.append(same_deli_jobs)

for j in sorted_by_deli_jobs:
    print(j[0].getJobState(), end=" ")
    print(j[0].getRequiredTime())
    print(len(j))

cncs = np.array(cncs)
cncs_forging = CNC_shape.getForgingCNC(cncs)
cncs_hex = CNC_shape.getHexCNC(cncs)
cncs_valve = CNC_shape.getValveCNC(cncs)
cncs_round = CNC_shape.getRoundCNC(cncs)
cncs_square = CNC_shape.getSquareCNC(cncs)
cncs_lok_forging = CNC_shape.getLokfittingForging(cncs) # 1,2,3,2m,3m,4m 단조
cncs_lok_hex = CNC_shape.getLokfittingHex(cncs) # 1,2,3,2m,3m,4m hex
cncs_3941 = CNC_shape.get3941cnc(cncs)
cncs_4042 = CNC_shape.get4042cnc(cncs)

