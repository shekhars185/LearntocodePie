class Sudoku:
    
    #initialization function
    def __init__(self):
            self.row = list('ABCDEFGHI')
            self.col = list('123456789')
            self.numset = {'1','2','3','4','5','6','7','8','9'}
            self.grid = {}
            self.subgrid = list()
            self.iblanks = list()
            self.cblanks = list()
            self.fillOrder = list()
            self.prefOrder = list()
            self.lastvalue = ''
            self.lastkey  = ''
            self.wrongopt = dict()
            
    def CreateGrid(self):
        row = self.row
        col = self.col
        for R in row:
            for C in col:
                d = str(R)+str(C)
                self.grid[d] = ''
                self.wrongopt[d] = []
                
    def CreateSubgrid(self):
        row = self.row
        col = self.col
        subgrid = []
        subgrid1 =[]
        subgrid2 =[]
        subgrid3 =[]
        subgrid4 =[]
        subgrid5 =[]
        subgrid6 =[]
        subgrid7 =[]
        subgrid8 =[]
        subgrid9 =[]

        for R in row:
            for C in col:
                d = str(R)+str(C)
                if row.index(R) < 2:
                    if col.index(C)<3:
                        subgrid1.append(d)
                    elif col.index(C) >2 and col.index(C) <6:
                        subgrid2.append(d)
                    else:
                        subgrid3.append(d)
                elif row.index(R) < 6 and row.index(R) >2:
                    if col.index(C)<3:
                        subgrid4.append(d)
                    elif col.index(C) >2 and col.index(C) <6:
                        subgrid5.append(d)
                    else:
                        subgrid6.append(d)
                else:
                    if col.index(C)<3:
                        subgrid7.append(d)
                    elif col.index(C) >2 and col.index(C) <6:
                        subgrid8.append(d)
                    else:
                        subgrid9.append(d)
        subgrid = [subgrid1,subgrid2,subgrid3,subgrid4,subgrid5,subgrid6,subgrid7,subgrid8,subgrid9]
        self.subgrid = subgrid
            
    def FillGrid(self):
        row = self.row
        col = self.col
        for R in row:
            print(' For row %s' %R)
            istring = input('Enter the values, Put 0 for Blank : ')
            while len(istring) != 9:
                print('Invalid Input for row %s'%R)
                istring = input('Enter the values, Put 0 for Blank : ')
            ilist = list(istring)
            for C in col:
                i = col.index(C)
                d = str(R) + str(C)
                self.grid[d] = ilist[i]

    
    def PrintGrid(self):
        row = self.row
        col = self.col
        for R in row:
          #  print(" ")
            if (row.index(R) == 0 or row.index(R) == 3 or row.index(R) == 6):
                print('_'*24)
            print('|',end= " ")
            for C in col:
                d = str(R)+str(C)
                if col.index(C)<3:
                   print(self.grid[d],end = " ")
                elif col.index(C) >2 and col.index(C) <6:
                    if col.index(C) == 3:
                        print('|',end = " ")
                    print(self.grid[d],end = " ")
                else:
                    if col.index(C) == 6:
                        print('|',end = " ")
                    print(self.grid[d],end = " ")
                    if col.index(C) == 8:
                        print('|')
        print('_'*24)
        
        
        
s = Sudoku()
s.CreateGrid()
s.CreateSubgrid()
s.FillGrid()
s.PrintGrid()
        


#1. Create Grid and Subgrid.
# Fill Grid
#2. Find out Blank Positions.
#3. Get Available options for Each given blank
#4. Fill the positions with only one possible option, update the Fill order
#5. Check for conflicts, compare with original blanks. Remove the recently filled value as well as previously filled clashing value if it was part of initial blank, Update the wrong option log.
#6. Re-genrate the blanks and repeat the process till all the blanks are filled.
