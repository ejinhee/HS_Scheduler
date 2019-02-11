import Job

def search_cycle_time(cursor2,Goodcd):

    cursor2.execute("""
    select TWRC.Processcd, AVG(TWRC.Cycletime)
from TWorkreport_CNC TWRC
inner join TGood g on g.GoodCd = TWRC.Goodcd
where g.GoodCd = """+Goodcd+"""  and (TWRC.Processcd = 'P1' or TWRC.Processcd = 'P2' or TWRC.Processcd = 'P3' )
group by TWRC.Processcd 
order by Processcd
    """)
    row = cursor2.fetchone()
    cycletime = []
    i = 0
    while row:
        cycletime.append(row[1])
        row = cursor2.fetchone()
    return cycletime

def search_job_by_deadline(jobs,start,end,cursor1,cursor2):

    cursor1.execute("""
     select a.Workno, g.GoodNo,  g.GoodCd, i.GoodCd as 'RawMaterialCd', m4.Minorcd,
            a.OrderQty , a.DeliveryDate, 
            --case when i.Class3 = '061038' then '단조' else 'HEX' end as Gubun,
            case when m3.minorNm = 'Forging' then 0
			when m3.minorNm = 'Hex Bar' then 1
			when m3.minorNm = 'Round Bar' then 2
			when m3.MinorNm = 'Square Bar' then 3
			when m3.MinorNm = 'VALVE 선작업' then 4 end as RawMaterialGubun,
            --    소재사이즈
            ISNULL(i.Size, 0) as RawMaterialSize,
            --    LOK FITTING 유무
            case when g.Class3 = '061001' then 'Y' else 'N' end as LOKFITTINGYN, --LOK FITTING
            --    LOK FITTING  일때 반제품 품번 사이즈에 따른 기계배정
            case when g.Class3 = '061001' and ((LEFT(REPLACE(g.GoodNo, RTRIM(m4.MinorNm),''),3) = '-1-') or
                                               (LEFT(REPLACE(g.GoodNo, RTRIM(m4.MinorNm),''),3) = '-2-') or
                                               (LEFT(REPLACE(g.GoodNo, RTRIM(m4.MinorNm),''),3) = '-3-') or
                                               (LEFT(REPLACE(g.GoodNo, RTRIM(m4.MinorNm),''),4) = '-2M-') or
                                               (LEFT(REPLACE(g.GoodNo, RTRIM(m4.MinorNm),''),4) = '-3M-') or
                                               (LEFT(REPLACE(g.GoodNo, RTRIM(m4.MinorNm),''),4) = '-4M-')) then 'Y' else 'N' end as LOKFITTINGSIZEYN, a.CloseDate, a.Credate, a.Moddate
     from TWorkreport_Han_Eng a
     inner join TGood g on a.Goodcd = g.GoodCd
     inner join TGood i on a.Raw_Materialcd = i.GoodCd
     left outer join TMinor m3 on i.Class3 = m3.MinorCd
     left outer join TMinor m4 on g.Class4 = m4.MinorCd

     where DeliveryDate between '20181227' and '20181231'
        and PmsYn = 'N'
        and ContractYn = '1' 
       --    단조    Hex Bar    Round Bar    Square Bar    VALVE 선작업
       and i.Class3 in ('061038', '061039', '061040', '061048', '061126')
	 order by DeliveryDate
    """)
    row = cursor1.fetchone()

    while row:
        temp = Job.Job()
        temp2 = Job.Job()
        temp.setWorkNo(row[0])
        temp.setGoodNo(row[1])
        temp.setGoodCd(row[2])
        goodcd = row[2]
        temp.setRawmaterialCd(row[3])
        temp.setOrderQty(row[5])
        temp.setDeliveryDate(row[6])
        temp.setRawmaterialGubun(row[7])
        temp.setSpec(row[8])
        temp.setLOKFitting(row[9])
        temp.setLOKFittingSize(row[10])
        temp.setCycletime(search_cycle_time(cursor2,  goodcd))

        jobs.append(temp)

        row = cursor1.fetchone()

    total_number = len(jobs)
    print("the total # of job : %d"%(total_number))
