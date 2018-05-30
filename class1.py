# Logic gate class definations
class LogicGate:
  def __init__(self,n):
    self.label = n
    self.output = None
  
  def getlabel:
    return self.label
    
 def getoutput:
    self.output = self.perfromgatelogic()
    return self.output
 
 #Binary gate
 
 class BinaryGate(Logicgate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None
        
     def getPinA(self):
        return int(input('Enter Input for Pin A for gate" + self.getlabel() +'-->'))
     def getPinB(self):
        return int(input('Enter Input for Pin B for gate" + self.getlabel() +'-->')) 
     def setnextpin(self,source):
        if self.pinA == None:
          self.pinA = source
        else:
          if self.pinB == None:
            self.pinB = source
          else:
            print('Cannot connect')
  
  class UniaryGate(Logicgate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None
       
     
     def getPin(self):
        return int(input('Enter Input for Pin A for gate" + self.getlabel() +'-->'))
        
     def setnextpin(self,source):
      if self.pin = None:
         self.pin = source
      else:
         print("Cannot connect")

class AndGate(BinaryGate):
      def __init__(self,n):
        BinaryGate.__init__(self,n)
        
      def performgatelogic(self):
        a = self.getpinA()
        b = self.getpinB()
        
        if a==1 and b==1:
          return 1
        else:
          return 0
 
 class OrGate(BinaryGate):
    def __init__(self,n):
      BinaryGate.__init__(self,n)
      
    def performgatelogic(self):
      a = self.getpinA()
      b = self.getpinB()
      
      if a ==1 or b == 1:
        return 1
      else:
        return 0
        
  class NotGate(UniaryGate):
    def __init__(self,n):
      UniaryGate.__init(self.n)
      
    def perfromgatelogic(self):
      a = self.getpin()
      if a == 1:
        return 0
      elif a == 0:
        return 1
  
  class connector:
    def __init__(self,fgate,tgate):
      self.fromgate = fgate
      self.togate   = tgate
      
      tgate.setnextpin(self)
    
    def getFrom(self):
      return self.fromgate
      
    def getTo(self):
      return self.togate
      
def main():
  g1 = AndGate("G1")
  g2 = AndGate("G2")
  g3 = OrGate("G3")
  g4 = NotGate("G4")
  
  c1 = connector(g1,g3)
  c2 = connector(g2,g3)
  c3 = connector(g3,g4)
  print(g4.getOutput())
 
main()
     
