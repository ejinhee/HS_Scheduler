
def getDateList(start, end):
    li = {}
    if( (int(end) - int(start)) < 50):
        for i in range(int(end) - int(start) +1):
            li[str(int(start) +i)] = 0
    else:
        if(int(start) - 20190000  <200):
            for i in range(20190131-int(start) +1):
                li[str(int(start) +i)] = 0

            start = '20190201'
            for i in range(int(end) - int(start) +1):
                li[str(int(start) +i)] = 0
        elif(int(start) - 20190000  <300):
            for i in range(20190228-int(start) +1):
                li[str(int(start) +i)] = 0

            start = '20190301'
            for i in range(int(end) - int(start) +1):
                li[str(int(start) +i)] = 0
        elif(int(start) - 20190000  <400):
            for i in range(20190331-int(start) +1):
                li[str(int(start) +i)] = 0

            start = '20190401'
            for i in range(int(end) - int(start) +1):
                li[str(int(start) +i)] = 0

        elif(int(start) - 20190000  <500):
            for i in range(20190430-int(start) +1):
                li[str(int(start) +i)] = 0

            start = '20190501'
            for i in range(int(end) - int(start) +1):
                li[str(int(start) +i)] = 0
        elif(int(start) - 20190000  <600):
            for i in range(20190531-int(start) +1):
                li[str(int(start) +i)] = 0

            start = '20190601'
            for i in range(int(end) - int(start) +1):
                li[str(int(start) +i)] = 0
        elif(int(start) - 20190000  <700):
            for i in range(20190630-int(start) +1):
                li[str(int(start) +i)] = 0

            start = '20190701'
            for i in range(int(end) - int(start) +1):
                li[str(int(start) +i)] = 0
        elif(int(start) - 20190000  <800):
            for i in range(20190731-int(start) +1):
                li[str(int(start) +i)] = 0

            start = '20190801'
            for i in range(int(end) - int(start) +1):
                li[str(int(start) +i)] = 0
        elif(int(start) - 20190000  <900):
            for i in range(20190831-int(start) +1):
                li[str(int(start) +i)] = 0

            start = '20190901'
            for i in range(int(end) - int(start) +1):
                li[str(int(start) +i)] = 0
        elif(int(start) - 20190000  <1000):
            for i in range(20190930-int(start) +1):
                li[str(int(start) +i)] = 0

            start = '20191001'
            for i in range(int(end) - int(start) +1):
                li[str(int(start) +i)] = 0
        elif(int(start) - 20190000  <1100):
            for i in range(20191031-int(start) +1):
                li[str(int(start) +i)] = 0

            start = '20191101'
            for i in range(int(end) - int(start) +1):
                li[str(int(start) +i)] = 0
        elif(int(start) - 20190000  <1200):
            for i in range(20191130-int(start) +1):
                li[str(int(start) +i)] = 0

            start = '20191201'
            for i in range(int(end) - int(start) +1):
                li[str(int(start) +i)] = 0
        else:
            print("DateList error")
            exit(1)


    return  li
