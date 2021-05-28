from logFile import *
from jsonFile import data
import json

l=LogFile("log1")
l.row("hello[") #this [ can not be printed
l.row("world\"") #this " can not be printed
l.section() #break
l.row("hello"+scape("[")) #this [ can be printed
l.row("world"+scape("\"")) #this " can be printed
l.section() #break
l.row("by Eanorambuena")
l.read()

l2=LogFile("log2")
l2.fromDict(data)