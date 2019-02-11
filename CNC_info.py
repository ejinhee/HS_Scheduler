import xlrd
import CNC

######################################## 사이즈 앞에 'H' 로 구분


def getCNCinfo(cncs):
    workbook = xlrd.open_workbook("hansun_cnc_info.xlsx")
    worksheet= workbook.sheet_by_index(0)

    rows = worksheet.nrows
    cols = worksheet.ncols
    print(rows)
    for row in range(rows):
        try:
            col_E = worksheet.cell_value(row,4)
            if(col_E != "후가공" and col_E != '' ):
                size = worksheet.cell_value(row,4)
                size = size.replace('H','')
                temp =CNC.CNC()
                temp.setSize(size.split(' ~ '))
                temp.setCNCnumber(int(worksheet.cell_value(row,1)))
                temp.setShape(worksheet.cell_value(row,2))
                temp.setType(worksheet.cell_value(row,3))
                if(worksheet.cell_value(row,5) == "코렛"):
                    temp.setIsCoret("true")
                else:
                    temp.setIsCoret("false")
                cncs.append(temp)
            else:
                pass
        except Exception as e:
            print(e)

    print("CNC갯수 : ",end="")
    print(len(cncs))


