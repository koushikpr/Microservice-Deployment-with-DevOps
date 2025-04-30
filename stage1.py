s = "PAYPALISHIRING"
numRows = 3


numcol = len(s)//numRows

arr = [[0]*numcol for i in range(numRows) ]


r = 0
col = 0

while len(s)>0:
            if r == numRows:
                r -=1
                col +=1
                arr[r][col] = s[-1]
                s = s[:-1]
                
            if r == 0:
                r +=1
                arr[r][col] = s[-1]
                s = s[:-1]
            print(s)

