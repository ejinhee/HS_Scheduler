import matplotlib.pylab as plt
import numpy as np

def DrawGraph(final_cncs):
    cncs_graph = []
    for cnc in final_cncs:
        cncs_graph.append('CNC'+ str(cnc.getCNCnumber()))

    y_pos = np.arange(len(cncs_graph))
    time_list =[]

    MaxNumofJobs = 0
    for cnc in final_cncs:
        if(len(cnc.joblist) > MaxNumofJobs ):
            MaxNumofJobs = len(cnc.joblist)

    print(MaxNumofJobs)
    job_idx = 0

    for i in range(MaxNumofJobs):
        temp_list = []
        for cnc in final_cncs:
            if(len(cnc.joblist) >= job_idx +1  ):
                temp_list.append(sum(cnc.joblist[job_idx].getRequiredTime())/1000)
            else:
                temp_list.append(0)
        time_list.append(temp_list)
        job_idx +=1

    print(time_list)

    time_array = np.array(time_list)
    plt.title("Schedule")

    for i in range(MaxNumofJobs-1):
        plt.barh(y_pos,sum(time_array[0:len(time_list)-i]),color='C'+str(i%10))
    plt.barh(y_pos,time_array[0],color='r')

    plt.yticks(y_pos,cncs_graph)
    plt.xlabel("time")
    plt.show()

