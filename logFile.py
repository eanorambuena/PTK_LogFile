import json, os

class Parser():
  def __init__(self,name="Parser"):
    self.sep=[',']
    self.sec=['|',"["]
    self.ski=[']',"{","}","\""]
    self.vip=["\\"]
    self.den=["~"]
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
  def isVip(self,x):
    return self.compare(x,self.vip)
  def isDeny(self,x):
    return self.compare(x,self.den)

class FilesTree:
  def __init__(self,familyName="tree",form=".ptklf"):
    self.name=familyName
    self.format=form
    self.reset()
  def reset(self):
    self.adress=self.name+"_hist"+self.format
    try:
      lines=self.getLines()
      for i in lines:
        os.remove(self.name+"_"+i+self.format)
    except:
      pass
  def getLines(self):
    h=open(self.adress,"r")
    lines=h.readlines()
    h.close()
    return lines
  def lastLine(self):
    lines=self.getLines()
    return lines[len (lines)-1]
  def register(self,t):
    with open(self.adress, 'a') as h:
      h.write(t+"\r\n")


class LogFile:
  def __init__(self,name="log",form=".ptklf"):
    self.name=name
    self.format=form
    self.reset()
    self.h=FilesTree(self.name)
  def row(self,t):
    self.text=self.text+str(t)+","
  def section(self):
    self.text=self.text+"|"
  def vip(self,t):
    s=self.p.vip[0]
    text=""
    for i in t:
      text+=s+i
    return text
  def den(self,t):
    s=self.p.den[0]
    text=""
    for i in t:
      text+=s+i
    return text
  def reset(self,resetParserYesOrNo=1):
    self.text=""
    self.adress=self.name+self.format
    if resetParserYesOrNo:
      self.p=Parser()
  def export(self):
    try:
      i=int(self.h.lastLine())+1
    except:
      i=0
    f=open(self.name+"_"+str(i)+self.format,"w")
    f.write(self.text)
    f.close()
    self.h.register(str(i))
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
        elif m==2:
          m=0
        elif self.p.separator(k[i]):
          print(t)
          t=""
        elif self.p.section(k[i]):
          print("")
        elif  self.p.skip(k[i]):
          pass
        elif  self.p.isVip(k[i]):
          m=1
        elif  self.p.isDeny(k[i]):
          m=2
        else:
          t+=k[i]
  def read(self,name="|",printYesOrNo=1):
    self.export()
    i=int(self.h.lastLine())
    if name=="|":
      self.readFrom(self.name+"_"+str(i)+self.format,printYesOrNo)
    else:
      self.readFrom(name,printYesOrNo)
  def fromDict(self,data):
    name=self.name+".json"
    with open(name, 'w') as file:
      json.dump(data, file, indent=4)
    self.readFrom(name)