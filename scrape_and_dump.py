import json
import re
import requests
from bs4 import BeautifulSoup

def get_warp(stage):
    url = "http://www.cute.hm/hogehoge/html/zone{}.html".format(stage)

    response = requests.get(url)
    response.encoding = response.apparent_encoding

    bs = BeautifulSoup(response.text, 'html.parser')

    warps = []
    for table in bs.select("table"):
        tds = table.select("td")
        if len(tds) == 0:
            continue
        if 'ゾーン' in tds[0].text:
            warps_text = tds[3].get_text(',').split(',')
            destination = []
            for warp_text in warps_text:
                for warp in warp_text.split('　'):
                    m = re.match('→([0-9]*)(（.*)', warp)
                    if m:
                        destination.append((m.group(1), m.group(2)))
                        continue
                    m = re.match('→([0-9]*)', warp)
                    if m:
                        destination.append((m.group(1), None))
            m = re.match('■ゾーン([0-9]*).*■', tds[0].text)
            for to, warp in destination:
                if warp:
                    if '隠し扉' in warp:
                        warp = '隠し扉'
                    elif '特殊' in warp:
                        warp = '特殊'
                    else:
                        warp = None
                warps.append({'from': int(m.group(1)), 'to': int(to), 'warp': warp})

    return warps

warps = []
warps += get_warp('01-10')
warps += get_warp('11-20')
warps += get_warp('21-30')
warps += get_warp('31-40')
warps += get_warp('41-50')
warps += get_warp('51-60')
warps += get_warp('61-70')
warps += get_warp('71-80')
warps += get_warp('81-90')
warps += get_warp('91-99')

with open('atlantis.json', 'w') as file:
    json.dump(warps, file)
