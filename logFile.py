import json

def scape(t):
  return "\\"+t

class Parser():
  def __init__(self,name="Parser"):
    self.sep=[',']
    self.sec=['|',"["]
    self.ski=[']',"{","}","\""]
    self.vip=["\\"]
    self.name=name
  def compare(self,x,arr):
    k = False
    for i in arr:
      k =( k or x==i)
    return k
  def separator(self,x):
    return self.compare(x,self.sep)
  def section(self,x):
    return self.compare(x,self.sec)
  def skip(self,x):
    return self.compare(x,self.ski)
  def isvip(self,x):
    return self.compare(x,self.vip)

class LogFile:
  def __init__(self,name="log",form=".ptklf"):
    self.text=""
    self.name=name
    self.format=form
    self.adress=self.name+self.format
    self.p=Parser()
  def row(self,t):
    self.text=self.text+str(t)+","
  def section(self):
    self.text=self.text+"|"
  def export(self):
    f=open(self.adress,"w")
    f.write(self.text)
    f.close()
  def readFrom(self,adress,printYesOrNo=1):
    f=open(adress,"r")
    k=f.read()
    self.text=k
    f.close()
    if printYesOrNo:
      t=""
      m=0
      for i in range(0,len(k)):
        if m==1:
          t+=k[i]
          m=0
        if self.p.separator(k[i]):
          print(t)
          t=""
        elif self.p.section(k[i]):
          print("")
        elif  self.p.skip(k[i]):
          pass
        elif  self.p.isvip(k[i]):
          m=1
        else:
          t+=k[i]
  def read(self,printYesOrNo=0):
    self.export()
    self.readFrom(self.adress,1)
  def fromDict(self,data):
    name=self.name+".json"
    with open(name, 'w') as file:
      json.dump(data, file, indent=4)
    self.readFrom(name)