'''
import requests
import pandas as pd
from _datetime import datetime
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
#print(rawop)

def dataframe(rawop):
    data =[]

    for i in range(54,75):
        calloi = callcoi= cltp = putoi = putcoi = pltp =0
        stp = rawop['strikePrice'][i]

        if(rawop['CE'][i]==0):
            calloi = callcoi = 0
        else:
            calloi = rawop['CE'][i]['openInterest']
            #print("he",calloi)
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
    print("hi",optionchain)
    return optionchain

optionchain = dataframe(rawop)
print(rawop)



def main():


    #normal oi
    optionchain = dataframe(rawop)
    print(optionchain['CALL OI'])
    TotalCallOI = optionchain['CALL OI'].sum()
    print("heee",TotalCallOI)
    print(optionchain['PUT OI'])
    TotalPutOI = optionchain['PUT OI'].sum()
    print("hee",TotalPutOI)


    #change in oi
    optionchain = dataframe(rawop)
    print(optionchain['CALL CHNG OI'])
    TotalChangeCallOI = optionchain['CALL CHNG OI'].sum()
    print(TotalChangeCallOI)
    print(optionchain['PUT CHNG OI'])
    TotalChangePutOI = optionchain['PUT CHNG OI'].sum()
    print(TotalChangePutOI)


    # time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)

    print('Total call:', TotalCallOI)
    print('Total put :', TotalPutOI)
    print('Total Change in call:',TotalChangeCallOI)
    print('Total Change in put :',TotalChangePutOI)
    print('The PCR =',TotalPutOI/TotalCallOI)
    print('The ChangeOI PCR =',TotalChangePutOI/TotalChangeCallOI)
    print('OI Difference =',TotalChangePutOI-TotalChangeCallOI)



while True:
    main()
    time.sleep(60)
'''



import requests
import pandas as pd
from _datetime import datetime
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
print(rawop)




