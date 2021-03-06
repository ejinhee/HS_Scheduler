import CNC_info
import AccessDB
import DB_query
import CNC_shape
import Job
import CNC
import Job_determination
import pyodbc
import DateList
import graph
import copy
import numpy as np
server = "221.161.62.124,2433"
database = "Han_Eng_Back"
username = "Han_Eng_Back"
password = "HseAdmin1991"

interval_time = 0
oneday = 3600*24
today = str(input("today is :"))

cncs = [] ## 전체CNC리스트
jobs = [] ## 전체작업리스트
sorted_by_deli_jobs = [] ##같은 납기일의 작업을 가지는 리스트의 리스트(2차)
same_deli_jobs = [] ## sorted_by_deli_jobs리스트를 위한 임시 리스트
start = '20181201'
end = '20181231'
CNC_info.getCNCinfo(cncs)
cursor1 = AccessDB.AccessDB(server,database,username,password)
cursor2 = AccessDB.AccessDB(server,database,username,password)
DB_query.search_job_by_deadline(jobs,start,end,cursor1,cursor2)


for job in jobs:
    job.printJob()


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

sorted_jobs = []  # deliverydate -> required_time sorted
for job in sorted_by_deli_jobs:
    sorted_jobs.append(sorted(job,key = lambda j:j.required_time,reverse=True))

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

sorted_jobs = np.array(sorted_jobs)

temp_job = Job.Job()


for jobs in sorted_jobs:
    idx = 0
    for job in jobs:
        if(job.getRawmaterialGubun()== 1 and job.getLOKFitting()=='Y' and job.getLOKFittingSize()=='N'):
            if(10 < job.getSpec() and 20 > job.getSpec()):
                temp_job = copy.deepcopy(job)
                job.setProcessCd(1)
                temp_job.setProcessCd(2)
                cncs_3941[0].setReservedTime(cncs_3941[0].getReservedTime() + job.getRequiredTime()[0] + interval_time)
                cncs_3941[0].jobAssign(job)
                cncs_3941[1].setReservedTime(cncs_3941[1].getReservedTime() + temp_job.getRequiredTime()[1] + interval_time)
                cncs_3941[1].jobAssign(temp_job)
                del jobs[idx]
                continue

                if(cncs_3941[1].getReservedTime() >= oneday):
                    break

            elif(20.64<job.getSpec() and 22.22< job.getSpec()):
                temp_job = copy.deepcopy(job)
                job.setProcessCd(1)
                temp_job.setProcessCd(2)
                job.printJob()
                cncs_4042[0].setReservedTime(cncs_4042[0].getReservedTime() + job.getRequiredTime()[0] + interval_time)
                cncs_4042[0].jobAssign(job)
                cncs_4042[1].setReservedTime(cncs_4042[1].getReservedTime() + temp_job.getRequiredTime()[1] + interval_time)
                cncs_4042[1].jobAssign(temp_job)

                del jobs[idx]
                continue

                if(cncs_4042[1].getReservedTime() >= oneday):
                    break

        idx = idx +1
    ## 3941,4042 cnc 배정 (하루)

    for job in jobs:
        if(Job_determination.JobDetermine(job) == 1):
            cncs_forging = sorted(cncs_forging,key = lambda c:c.reservedTime)
            for cnc in cncs_forging:
                if(float(cnc.getSizeFrom()) < job.getSpec() and float(cnc.getSizeTo()) > job.getSpec()):
                    cnc.jobAssign(job)
                    cnc.setReservedTime(cnc.getReservedTime() + sum(job.getRequiredTime()) + interval_time)
                    break

        elif(Job_determination.JobDetermine(job) == 2):
            cncs_hex = sorted(cncs_hex,key = lambda c:c.reservedTime)
            for cnc in cncs_hex:
                if(float(cnc.getSizeFrom()) < job.getSpec() and float(cnc.getSizeTo()) > job.getSpec()):
                    cnc.jobAssign(job)
                    cnc.setReservedTime(cnc.getReservedTime() + sum(job.getRequiredTime()) + interval_time)
                    break

        elif(Job_determination.JobDetermine(job) == 3):
            cncs_round = sorted(cncs_round,key = lambda c:c.reservedTime)
            cncs_round[0].jobAssign(job)
            cncs_round[0].setReservedTime(cncs_round[0].getReservedTime() + sum(job.getRequiredTime()) + interval_time)

        elif(Job_determination.JobDetermine(job) == 4):
            cncs_square = sorted(cncs_square,key = lambda c:c.reservedTime)
            cncs_square[0].jobAssign(job)
            cncs_square[0].setReservedTime(cncs_square[0].getReservedTime() + sum(job.getRequiredTime()) + interval_time)

        elif(Job_determination.JobDetermine(job) == 5):
            cncs_valve = sorted(cncs_valve,key = lambda c:c.reservedTime)
            cncs_valve[0].jobAssign(job)
            cncs_valve[0].setReservedTime(cncs_valve[0].getReservedTime() + sum(job.getRequiredTime()) + interval_time)

        elif(Job_determination.JobDetermine(job) == 6):
            cncs_square = sorted(cncs_square,key = lambda c:c.reservedTime)
            cncs_lok_forging[0].jobAssign(job)
            cncs_lok_forging[0].setReservedTime(cncs_lok_forging[0].getReservedTime() + sum(job.getRequiredTime()) + interval_time)

        elif(Job_determination.JobDetermine(job) == 7):
            cncs_square = sorted(cncs_square,key = lambda c:c.reservedTime)
            cncs_lok_hex[0].jobAssign(job)
            cncs_lok_hex[0].setReservedTime(cncs_lok_hex[0].getReservedTime() + sum(job.getRequiredTime()) + interval_time)

        #jobs.remove(job)


for cnc in cncs:
    cnc.printJobList()




li = DateList.getDateList('20190320','20190410')
print(li)

graph.DrawGraph(cncs)