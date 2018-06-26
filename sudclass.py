class sudoku:
    def __init__(self):
        self.row = list('ABCDEFGHI')
        self.col = 10
        self.numset = {'1','2','3','4','5','6','7','8','9'}
        self.grid = {}
        self.subgrid = list()
        self.blanks=list()
        self.fillOrder = list()
        self.prefOrder = list()
        self.lastvalue = ''
        self.lastkey   = ''
        self.wrongopt = dict()

    def CreateGrid(self):
        row = self.row
        col = self.col
        for R in row:
            for c in range(1,col):
                d = str(R)+str(c)
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
            rname = str(row[num-1])
            rstring = input('Enter the values,0 for blank :')
            while len(rstring) !=9:
                print('Invalid Input,Check number of terms and blanks')
                rstring = input('Enter the values,0 for blank')
            rname = list(rstring)
            d = str(row[num-1])
            for index in range(1,col):
                key = d +str(index)
                self.grid[key] =rname[index-1]
        print(self.grid)
        #return self.grid

    def GetBlanks(self):
        dict = self.grid
        self.blanks=[key for key,value in dict.items() if value == '0']
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
        return options

   

    def UpdateWrong(self,key,value):
        # get the already exiusting list of wrong values for given spot
        triedopt = self.wrongopt[key]
        if value not in triedopt:
            triedopt.append(value)
            self.wrongopt[key] = triedopt #update the
            print('Option %s is wrong'%value)
            print('for position %s'%key)

    def CheckWrongV(self,key,value):
        triedopt = self.wrongopt[key]
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
            print(" with Value %s" %d)
            s.grid[blank] = list(d)[0]
            s.fillOrder.append(blank)
            print('Filled in order')
            print(s.fillOrder)
            s.lastkey = blank
            s.lastvalue = list(d)[0]
            SingleElement = True
        elif len(d) > 1: #When There are Multiple possible options.
            print('Slot %s has multiple options:' %blank)
            print(d)
            if len(d)<min:
                min = len(d)
                s.prefOrder.append(blank)
    # if there are no clear value for any blanks
    print('Any option with single choice ?')
    print(SingleElement)
    s.GetBlanks()  # Refresh the Blank table.
    if SingleElement == False:
        s.GetBlanks()  # Refresh the Blank table.
        print('Remaining blanks')
        print(s.blanks)
        print('Order of filling of blanks')
        print(s.prefOrder)
        if len(s.prefOrder) != 0:
            keyf = s.prefOrder.pop()   # get the key with minimum number of options
            if keyf in s.blanks:
                avl = s.GetOptions(keyf)
                if avl == None: # No option available for the Blank
                   #Remove the last filled value
                   #Pop the key from FillOrder
                   keyl = s.fillOrder.pop()
                   s.lastkey = keyl
                   s.lastvalue= s.grid[keyl]
                   s.grid[keyl] = '0'
                   s.GetBlanks()
                   # regenerate the list of blanks
                   #update the wrong value dictionary structure
                   s.UpdateWrong(s.lastkey,s.lastvalue)
                   avl = s.GetOptions(keyf)
                else: # Multiple options available
                   # We are not trying to fill the same grid position
                   if s.lastkey != keyf:
                        process1 = True
                        for v in list(avl):
                            if process1 == True:
                                check = s.CheckWrongV(keyf,v)
                                if check :
                                    s.grid[keyf] = v
                                    s.lastvalue = v
                                    s.lastkey = keyf
                                    process1 = False
                                    s.fillOrder.append(keyf)
                   elif s.lastkey == keyf:
                        process = True
                        for v in list(avl):
                            if v != s.lastvalue and process == True:
                                check = s.CheckWrongV(keyf,v)
                                if check :
                                    s.grid[keyf] = v
                                    s.lastvalue = v
                                    s.lastkey = keyf
                                    process = False
                                    s.fillOrder.append(keyf)

    s.GetBlanks()
    if s.blanks == []:
        ExitProcessing = True
    else:
        Q = input('Press Q to Exit program')
        if Q == 'Q' or Q == 'q':
            ExitProcessing = True


print('Final Grid')
print(s.grid)







