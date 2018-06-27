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
            self.options  = dict()
            self.opcount   = dict()
            
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

    def GetBlanks(self):
        dict = self.grid
        self.cblanks=[key for key,value in dict.items() if value == '0']
        #return self.blanks
    
    def CheckRow(self,row):
        col = self.col
        pset = set()
        aset = set()
        for i in col:
            key = row+i
            if self.grid[key] in self.numset:
                pset.add(self.grid[key])
        aset = self.numset - pset
        return aset
    
    def CheckCol(self,col):
        r = self.row
        pset = set()
        aset = set()
        for row in r:
            key = str(row)+col
            if self.grid[key] in self.numset:
                pset.add(self.grid[key])
        aset = self.numset -pset
        return aset    
        
    def CheckSubgrid(self,key):
        pset = set()
        aset = set()
        pos = []
        if key in self.subgrid[0]:
            pos = self.subgrid[0]
        elif key in self.subgrid[1]:
            pos = self.subgrid[1]
        elif key in self.subgrid[2]:
            pos = self.subgrid[2]
        elif key in self.subgrid[3]:
            pos = self.subgrid[3]
        elif key in self.subgrid[4]:
            pos = self.subgrid[4]
        elif key in self.subgrid[5]:
            pos = self.subgrid[5]
        elif key in self.subgrid[6]:
            pos = self.subgrid[6]
        elif key in self.subgrid[7]:
            pos = self.subgrid[7]
        elif key in self.subgrid[8]:
            pos = self.subgrid[8]

        for key in pos:
            if self.grid[key] in self.numset:
                pset.add(self.grid[key])

        aset = self.numset - pset
        return aset

    def CheckWrong(self,key):
        #eliminate wrong options.return valid options
        wopt = s.wrongopt[key]
        pset = set()
        aset = set()
        for v in wopt:
            pset.add(v)
        aset = self.numset - pset
        return aset
    
    def GetOptions(self,key):
        #keyst = str(key)
        options = set()
        rname = key[0]
        cname = key[1]
        rmiss = self.CheckRow(rname)
        cmiss = self.CheckCol(cname)
        gmiss = self.CheckSubgrid(key)
        wmiss = self.CheckWrong(key)
        options = wmiss.intersection(gmiss.intersection(cmiss.intersection(rmiss)))
        options = list(options)
        return options

    def ProcessBlank(self,key):
        options = self.GetOptions(position)
        self.options[key] = options
        self.opcount[key] = len(options)
        if len(options) == 0: # No option found
            print(" No options found for position:%s"%key)
            
        
    def ProcessBlanks(self):
        blist = self.cblanks
        for position in blist:
            self.ProcessBlank(position)
            
            
    def FillPosition(self,key,value):
        self.grid[key] = value
        self.fillOrder.append(key)
        self.lastvalue = key
        self.lastkey  = value
        

        
    def ProcessSblanks(self):
        CurrBlanks = self.cblanks
        for blank in CurrBlanks:
            SingleOptFlag = False
            if self.opcount[blank] == 1:
               #fill the grid
               self.FillPosition(blank,self.options[blank][0])
               self.grid[blank] = self.options[blank][0]
               SingleOptFlag = True
        return SingleOptFlag 
        
    def RowContradiction(self,row,value):
        
        
    def ColContradiction(self,col,value):
        
        
    def GridContradiction(self,key,value):
        
        
    
    def RemoveValue(self,key):
        #remove value only if it was part of initial blank.
        if key not in self.iblanks:
            self.grid[key] = '0'
        else:
            # When a key value results in contradiction.
            row = key[0]
            col = key[1]
            
            
    def CheckGrid(Self):
        # Update the List of Blanks
        self.GetBlanks()
        # Get Options for Each Blank
        self.ProcessBlanks()
        NoOption= [key for key,value in self.opcount if value == 0]
        if len(NoOption) == 0:
            #remove last filled position
            #add the key value pair to wrong option
            
        
#1. Create Grid and Subgrid.       
s = Sudoku()
s.CreateGrid()
s.CreateSubgrid()
# Fill Grid
s.FillGrid()
s.PrintGrid()
#2. Find out Blank Positions.        
s.GetBlanks()
s.ibanks = s.cblanks
#3. Get Available options for Each given blank
s.processBlanks()
#4. Fill the positions with only one possible option, update the Fill order
d = s.ProcessSblanks()
if not d:
    s.Getblanks()  # Update the current Blanks
    currlist = s.cblanks
    s.ProcesBlanks()
    if currlist == []:#no blanks
        print('All positions filled')
        s.PrintGrid()
    else:
        for position in currlist:
            curoptions = self.options[position]
            for value in curoptions:
                s.CheckGrid(self,key,value)
                s.Fillposition(position,value)
                #check if the current config of Grid creates any exceptions.
                
                
#5. Check for conflicts, compare with original blanks. Remove the recently filled value as well as previously filled clashing value if it was part of initial blank, Update the wrong option log.
#6. Re-genrate the blanks and repeat the process till all the blanks are filled.
