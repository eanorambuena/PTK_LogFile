from logFile import *
import json

l=LogFile("log1")
l.row("hello[") #this [ can not be printed
l.row("world\"") #this " can not be printed
l.section() #break
l.row("hello"+l.vip("[")) #this [ can be printed
l.row("world"+l.vip("\"")) #this " can be printed
l.section() #break
l.row("by Eanorambuena"+l.den("this text can not be printed"))
l.read()

l.reset()
l.p.den=":"
l.row(l.den("this text can not be printed"))
l.read()

l.h.reset()

data = {}
data['clients'] = []
data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})
data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})
data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})
l2=LogFile("log2")
l2.fromDict(data)