class sudoku:
    def __init__(self):
        self.row = list('ABCDEFGHI')
        self.col = 10
        self.numset = set(list[range(1,col)])
        self.grid = {}
        self.subgrid = []
        self.blanks=[]
        self.fillOrder = []
        self.prefOrder = []
        self.lastvalue = ''
        self.lastkey   = ''
        self.wrongopt = {}
        
    def CreateGrid(self):
        row = self.row
        col = self.col
        for R in row:
            for c in range(1,cpl):
                d = str(R)+str(e)
                self.grid[d] = ''
                self.wrongopt[d] = []
        #return self.grid
        
    def GenSubgrid(self):
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
            for c in range(1,col):
                d = str(R)+str(c)
                if row.index(R) < 3:
                    if c<4:
                        subgrid1.append(d)
                    elif c >3 and c <7:
                        subgrid2.append(d)
                    else:
                        subgrid3.append(d)
                elif row.index(R) < 7 and row.index(R) >3:
                     if c<4:
                        subgrid4.append(d)
                    elif c >3 and c <7:
                        subgrid5.append(d)
                    else:
                        subgrid6.append(d)
                else:
                     if c<4:
                        subgrid7.append(d)
                    elif c >3 and c <7:
                        subgrid8.append(d)
                    else:
                        subgrid9.append(d)                    
        subgrid = [subgrid1,subgrid2,subgrid3,subgrid4,subgrid5,subgrid6,subgrid7,subgrid8,subgrid9]
        self.subgrid = subgrid
    
    def FillGrid(self):
        row = self.row
        col = self.col
        for num in range(1,col):
            print("for row{}".format(num))
            rname = str(row[num])
            rstring = input('Enter the values,0 for blank :']
            while len(rstring) !=9:
                print('Invalid Input,Check number of terms and blanks')
                rstring = input('Enter the values,0 for blank :']
            rname = list(rstring)
            d = str(row[num-1])
            for index in range(1,col):
                key = d +str(index)
                self.grid[key] =rname[index-1]
        #return self.grid
        
    def GetBlanks(self):
        blanks=[key for key,value in self.grid.items() is value == 0]
        self.blanks = blanks
        #return self.blanks
    def CheckRow(self,row):
        col = self.col
        pset = set()
        aset = set()
        for i in range(1,col):
            c = str(i)
            key = row+c
            if self.grid[key] in self.numset:
                pset.add(self.grid[key])
        aset = numset - pset
        return aset
    
    def CheckCol(self,col):
        r = self.row
        pset = set()
        aset = set()
        for row in r:
            key = str(row)+col
            if self.grid[key] in self.numset:
                pset.add(self.grid[key])
        aset = numet -pset
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
            pos = self.subgridc[7]
        elif key in self.subgrid[8]:
            pos = self.subgrid[8]

     for key in pos:
         if grid[key] in self.numset:
             pset.add(self.grid[key])

     aset = numset - pset
     return aset
        
        
    def CheckWrong(self,key):
        #eliminate wrong options.return valid options
        wopt = s.wrongopt[key]
        pset = set()
        aset = set()
        for v in wopt:
            pset.add(v)
        aset = s.numset - pset
        return aset
        
        
    def GetOptions(self,key):
        keyst = str(key)
        options = set()
        rname = key[0]
        cname = key[1]
        rmiss = CheckRow(rname)
        cmiss = CheckCol(cname)
        gmiss = CheckSubgrid(key)
        wmiss = CheckWrong(key)
        options = wmiss.intersection(gmiss.intersection(cmiss.intersection(rmiss)))
        return options
        
    
    def UpdateWrong(self,key,value):
        # get the already exiusting list of wrong values for given spot
        triedopt = s.wrongopt[key]
        if value not in triedopt:
            triedopt.append(value)
            s.wrongspot[key] = triedopt #update the 
            print('Option %s is wrong for position %s' %key %value)
            
    def CheckWrong(self,key,value):
        triedopt = s.wrongopt[key]
        if value in triedopt:
            return False
        else:
            return True
            
s = sudoku()
s.CreateGrid()
s.GenSubgrid()
s.FillGrid()
s.GetBlanks()
min = 9
ExitProcessing = False
while ExitProcessing is False:
    SingleElement = False
    for blank in s.blanks:
        d = set()
        d = s.GetOptions(blank)
        if len(d) == 1:
            print(" Updating %s"%blank)
            s.grid[blank] = d[0]
            s.fillOrder.append[blank]
            s.lastkey = blank
            s.lastvalue = d[0]
            SingleElement = True
        else: #When There are Multiple possible options.
            print('Slot %s has multiple options:' %blank)
            print(d)
            if len(d)<min:
                min = len(d)
                s.prefOrder.append(blank)
    # if there are no clear value for any blanks
    if SingleElement = False:
        s.GetBlanks()  # Refresh the Blank table.
        if len(s.prefOrder) != 0:
            keyf = prefOrder.pop()   # get the key with minimum number of options
            if keyf in s.blanks:
                avl = GetOptions(keyf)
                if avl == None: # No option available for the Blank
                   #Remove the last filled value
                   #Pop the key from FillOrder
                   keyl = s.fillOrder.pop()
                   s.lastkey = keyl
                   s.lastvalue= s.grid[keyl]
                   s.grid[keyl] = '0'
                   s.GetBlanks()
                   " regenerate the list of blanks
                   "update the wrong value dictionary structure 
                   s.UpdateWrong(s.lastkey,s.lastvalue)
                   avl = GetOptions(keyf)
                else: " Multiple options available
                   " We are not trying to fill the same grid position
                   if s.lastkey != keyf:
                        process1 = True
                        for v in avl:
                            if process1 = True:
                                check = s.CheckWrong(keyf,v)
                                if check : 
                                    s.grid[keyf] = v
                                    s.lastvalue = v
                                    s.lastkey = keyf
                                    process1 = False                        
                   else s.lastkey = keyf:
                        process = True
                        for v in avl:
                            if v != s.lastvalue and process = True:
                                check = s.CheckWrong(keyf,v)
                                if check : 
                                    s.grid[keyf] = v
                                    s.lastvalue = v
                                    s.lastkey = keyf
                                    process = False
            

    s.GetBlanks()
    if s.blanks == []:
        ExitProcessing = True
    else:
        Q = input('Press Q to Exit program')
        if Q = 'Q' or Q = 'q':
            ExitProcessing = True
print('Final Grid')
print(s.grid)
        
        
        
            
            
        
        
        
