import CNC_info
import AccessDB
import DB_query
import Job
import CNC
import pyodbc

server = "221.161.62.124,2433"
database = "Han_Eng_Back"
username = "Han_Eng_Back"
password = "HseAdmin1991"

cncs = []
jobs = []

start = '20181227'
end = '20181231'

CNC_info.getCNCinfo(cncs)
cursor1 = AccessDB.AccessDB(server,database,username,password)
cursor2 = AccessDB.AccessDB(server,database,username,password)
DB_query.search_job_by_deadline(jobs,start,end,cursor1,cursor2)

