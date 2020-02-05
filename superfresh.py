import atexit

class SuperFresh:
    def __init__(self,displayExit=True):
        self.counter=0
        self.string=None
        print("Loading SuperFresh module...")
        self.incCounter()
        if displayExit:
            atexit.register(self.exitSummary)

    def myTest(self):
        print("This is a test")
        self.incCounter()
    def myStr(self,inStr,upper=False):
        self.string=inStr.upper() if upper==True else inStr
        self.incCounter()
        return self.string
        
    def myPrint(self,inStr="",upper=False):
        if inStr != "":
          self.string=self.myStr(inStr,upper)
          
        if self.string == None:
            raise Exception('No string defined')
        self.incCounter()
        printStr="self.String is: '%s'" % (self.string)
        print(printStr)
        return printStr
         
    def incCounter(self):
        self.counter +=1

    def getCounter(self):
        print ("Count is set to %d" % self.counter)
        self.incCounter()
    
    def exitSummary(self):
        print ("Count is set to %d, string is: '%s'" % (self.counter,str(self.string)))
    
    
if __name__ == '__main__':
    print ('Module only. Do not execute this directly.\n__name__ is \'%s\'' % __name__) 