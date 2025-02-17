# Libraries
import datetime

import requests
import json
import math




import requests
import pandas as pd
import time

url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'



headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

session = requests.Session()
request = session.get(url,headers=headers)
cookies = dict(request.cookies)
response = session.get(url,headers=headers,cookies=cookies).json()
#print(response)
rawdata = pd.DataFrame(response)
rawop = pd.DataFrame(rawdata['filtered']['data']).fillna(0)
#print('This is length',len(rawop))

def dataframe(rawop):
    data =[]
    for i in range(0,len(rawop)):
        calloi = callcoi= cltp = putoi = putcoi = pltp =0
        stp = rawop['strikePrice'][i]
        if(rawop['CE'][i]==0):
            calloi = callcoi = 0
        else:
            calloi = rawop['CE'][i]['openInterest']
            callcoi = rawop['CE'][i]['changeinOpenInterest']
            cltp = rawop['CE'][i]['lastPrice']
        if (rawop['PE'][i] == 0):
            putoi = putcoi = 0
        else:
            putoi = rawop['PE'][i]['openInterest']
            putcoi= rawop['PE'][i]['changeinOpenInterest']
            pltp = rawop['PE'][i]['lastPrice']

        opdata = {
            'CALL OI': calloi, 'CALL CHNG OI': callcoi, 'CALL LTP': cltp , 'STRIKE PRICE': stp,
            'PUT OI': putoi, 'PUT CHNG OI': putcoi, 'PUT LTP': pltp
        }
        data.append(opdata)
    optionchain =pd.DataFrame(data)
    return optionchain
'''
#normal oi
optionchain = dataframe(rawop)
print(optionchain['CALL OI'])
TotalCallOI = optionchain['CALL OI'].sum()
print(TotalCallOI)
print(optionchain['PUT OI'])
TotalPutOI = optionchain['PUT OI'].sum()
print(TotalPutOI)

#change in oi
optionchain = dataframe(rawop)
print(optionchain['CALL CHNG OI'])
TotalChangeCallOI = optionchain['CALL CHNG OI'].sum()
print(TotalChangeCallOI)
print(optionchain['PUT CHNG OI'])
TotalChangePutOI = optionchain['PUT OI'].sum()
print(TotalChangePutOI)


print('this is call',TotalCallOI)
print('this is put',TotalPutOI)

print('this is Change call',TotalChangeCallOI)
print('this is Change put',TotalChangePutOI)
print('The PCR =',TotalPutOI/TotalCallOI)
print('The Change PCR =',TotalChangePutOI/TotalChangeCallOI)
'''
import requests
import pandas as pd

url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'



headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

session = requests.Session()
request = session.get(url,headers=headers)
cookies = dict(request.cookies)
response = session.get(url,headers=headers,cookies=cookies).json()
#print(response)
rawdata = pd.DataFrame(response)
rawop = pd.DataFrame(rawdata['filtered']['data']).fillna(0)
#print(rawop)

def dataframe(rawop):
    data =[]
    for i in range(0,len(rawop)):
        calloi = callcoi= cltp = putoi = putcoi = pltp =0
        stp = rawop['strikePrice'][i]
        if(rawop['CE'][i]==0):
            calloi = callcoi = 0
        else:
            calloi = rawop['CE'][i]['openInterest']
            callcoi = rawop['CE'][i]['changeinOpenInterest']
            cltp = rawop['CE'][i]['lastPrice']
        if (rawop['PE'][i] == 0):
            putoi = putcoi = 0
        else:
            putoi = rawop['PE'][i]['openInterest']
            putcoi= rawop['PE'][i]['changeinOpenInterest']
            pltp = rawop['PE'][i]['lastPrice']

        opdata = {
            'CALL OI': calloi, 'CALL CHNG OI': callcoi, 'CALL LTP': cltp , 'STRIKE PRICE': stp,
            'PUT OI': putoi, 'PUT CHNG OI': putcoi, 'PUT LTP': pltp
        }
        data.append(opdata)
    optionchain =pd.DataFrame(data)
    return optionchain


# Python program to print
# colored text and background
def strRed(skk):         return "\033[91m {}\033[00m".format(skk)
def strGreen(skk):       return "\033[92m {}\033[00m".format(skk)
def strYellow(skk):      return "\033[93m {}\033[00m".format(skk)
def strLightPurple(skk): return "\033[94m {}\033[00m".format(skk)
def strPurple(skk):      return "\033[95m {}\033[00m".format(skk)
def strCyan(skk):        return "\033[96m {}\033[00m".format(skk)
def strLightGray(skk):   return "\033[97m {}\033[00m".format(skk)
def strBlack(skk):       return "\033[98m {}\033[00m".format(skk)
def strBold(skk):        return "\033[1m {}\033[0m".format(skk)

# Method to get nearest strikes
def round_nearest(x,num=50): return int(math.ceil(float(x)/num)*num)
def nearest_strike_bnf(x): return round_nearest(x,100)
def nearest_strike_nf(x): return round_nearest(x,50)

# Urls for fetching Data
url_oc      = "https://www.nseindia.com/option-chain"
url_bnf     = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'
url_nf      = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
url_indices = "https://www.nseindia.com/api/allIndices"

# Headers
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'accept-language': 'en,gu;q=0.9,hi;q=0.8',
            'accept-encoding': 'gzip, deflate, br'}

sess = requests.Session()
cookies = dict()

# Local methods
def set_cookie():
    request = sess.get(url_oc, headers=headers, timeout=5)
    cookies = dict(request.cookies)

def get_data(url):
    set_cookie()
    response = sess.get(url, headers=headers, timeout=5, cookies=cookies)
    if(response.status_code==401):
        set_cookie()
        response = sess.get(url_nf, headers=headers, timeout=5, cookies=cookies)
    if(response.status_code==200):
        return response.text
    return ""

def set_header():
    global bnf_ul
    global nf_ul
    global bnf_nearest
    global nf_nearest
    response_text = get_data(url_indices)
    data = json.loads(response_text)
    for index in data["data"]:
        if index["index"]=="NIFTY 50":
            nf_ul = index["last"]
            print("nifty")
        if index["index"]=="NIFTY BANK":
            bnf_ul = index["last"]
            print("banknifty")
    bnf_nearest=nearest_strike_bnf(bnf_ul)
    nf_nearest=nearest_strike_nf(nf_ul)

# Showing Header in structured format with Last Price and Nearest Strike

def print_header(index="",ul=0,nearest=0):
    print(strPurple( index.ljust(12," ") + " => ")+ strLightPurple(" Last Price: ") + strBold(str(ul)) + strLightPurple(" Nearest Strike: ") + strBold(str(nearest)))

def print_hr():
    print(strYellow("|".rjust(70,"-")))

# Fetching CE and PE data based on Nearest Expiry Date
def print_oi(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                #print(strCyan(str(item["strikePrice"])) + strGreen(" CE ") + "[ " + strBold(str(item["CE"]["openInterest"]).rjust(10," ")) + " ]" + strRed(" PE ")+"[ " + strBold(str(item["PE"]["openInterest"]).rjust(10," ")) + " ]")
                print(data["records"]["expiryDates"][0] + " " + str(item["strikePrice"]) + " CE " + "[ " + strBold(str(item["CE"]["openInterest"]).rjust(10," ")) + " ]" + " PE " + "[ " + strBold(str(item["PE"]["openInterest"]).rjust(10," ")) + " ]")
                strike = strike + step

# Finding highest Open Interest of People's in CE based on CE data
def highest_oi_CE(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_oi = 0
    max_oi_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["CE"]["openInterest"] > max_oi:
                    max_oi = item["CE"]["openInterest"]
                    max_oi_strike = item["strikePrice"]
                strike = strike + step
    return max_oi_strike

# Finding highest Open Interest of People's in PE based on PE data
def highest_oi_PE(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_oi = 0
    max_oi_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["PE"]["openInterest"] > max_oi:
                    max_oi = item["PE"]["openInterest"]
                    max_oi_strike = item["strikePrice"]
                strike = strike + step
    return max_oi_strike

set_header()
print('\033c')
print_hr()
print_header("Nifty",nf_ul,nf_nearest)
print_hr()
print_oi(10,50,nf_nearest,url_nf)
print_hr()
print_header("Bank Nifty",bnf_ul,bnf_nearest)
print_hr()
print_oi(10,100,bnf_nearest,url_bnf)
print_hr()

# Finding Highest OI in Call Option In Nifty
nf_highestoi_CE = highest_oi_CE(10,50,nf_nearest,url_nf)

# Finding Highet OI in Put Option In Nifty
nf_highestoi_PE = highest_oi_PE(10,50,nf_nearest,url_nf)

# Finding Highest OI in Call Option In Bank Nifty
bnf_highestoi_CE = highest_oi_CE(10,100,bnf_nearest,url_bnf)

# Finding Highest OI in Put Option In Bank Nifty
bnf_highestoi_PE = highest_oi_PE(10,100,bnf_nearest,url_bnf)


print(strCyan(str("Major Resistance in Nifty:")) + str(nf_highestoi_CE))
print(strCyan(str("Major Support in Nifty:")) + str(nf_highestoi_PE))
print(strPurple(str("Major Resistance in Bank Nifty:")) + str(bnf_highestoi_CE))
print(strPurple(str("Major Support in Bank Nifty:")) + str(bnf_highestoi_PE))

def main():
    #normal oi
    optionchain = dataframe(rawop)
    #print(optionchain['CALL OI'])
    TotalCallOI = optionchain['CALL OI'].sum()
    #print(TotalCallOI)
   # print(optionchain['PUT OI'])
    TotalPutOI = optionchain['PUT OI'].sum()
    #print(TotalPutOI)

    #change in oi
    optionchain = dataframe(rawop)
    #print(optionchain['CALL CHNG OI'])
    TotalChangeCallOI = optionchain['CALL CHNG OI'].sum()
    #print(TotalChangeCallOI)
    #print(optionchain['PUT CHNG OI'])
    TotalChangePutOI = optionchain['PUT CHNG OI'].sum()
    #print(TotalChangePutOI)

    print('newww!!',datetime.time)
    print('Total CALL OI',TotalCallOI)
    print('Total PUT OI',TotalPutOI)

    print('Change in call oi',TotalChangeCallOI)
    print('Change in put oi',TotalChangePutOI)


    print('The PCR =',TotalPutOI/TotalCallOI)
    print('The Change PCR =',TotalChangePutOI/TotalChangeCallOI)
    print('OI Difference =',TotalChangePutOI-TotalChangeCallOI)


while True:
    main()
    time.sleep(60)


