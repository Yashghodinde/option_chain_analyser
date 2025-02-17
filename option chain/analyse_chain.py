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

    for i in range(45,52):
        calloi = callcoi= cltp = putoi = putcoi = pltp =0
        stp = rawop['strikePrice'][i]
        if(rawop['CE'][i]==0):
            calloi = callcoi = 0
        else:
            calloi = rawop['CE'][i]['openInterest']
            callcoi = rawop['CE'][i]['changeinOpenInterest']
            cltp = rawop['CE'][i]['lastPrice']
            cltp = rawop['CE'][i]['lastPrice']
            cvols = rawop['CE'][i]['totalTradedVolume']

        if (rawop['PE'][i] == 0):
            putoi = putcoi = 0
        else:
            putoi = rawop['PE'][i]['openInterest']
            putcoi= rawop['PE'][i]['changeinOpenInterest']
            pltp = rawop['PE'][i]['lastPrice']
            pvols = rawop['PE'][i]['totalTradedVolume']

        opdata = {
            'STRIKE PRICE': stp ,'COI': calloi ,'POI': putoi ,  'CALL CHNG OI': callcoi ,'PUT CHNG OI': putcoi , 'CALL LTP': cltp ,
             'PUT LTP': pltp,'CALL VOL' : cvols ,'PUT VOL' : pvols 
        }

        data.append(opdata)
    optionchain =pd.DataFrame(data)



    return optionchain



def main():

    #normal oi
    optionchain = dataframe(rawop)
    #print(optionchain['COI'])
    TotalCOI = optionchain['COI'].sum()
    #print(TotalCOI)
    #print(optionchain['POI'])
    TotalPOI = optionchain['POI'].sum()
    #print(TotalPOI)

    #change in oi
    optionchain = dataframe(rawop)
    #print(optionchain['CALL CHNG OI'])
    TotalChangeCallOI = optionchain['CALL CHNG OI'].sum()
    #print(TotalChangeCallOI)
    #print(optionchain['PUT CHNG OI'])
    TotalChangePutOI = optionchain['PUT CHNG OI'].sum()
    #print(TotalChangePutOI)
    print(optionchain)

    # write to the file
    now = datetime.now()
    dt_s = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('full_option_table_data.txt', 'a') as f:
        print(dt_s, file=f)
        print(optionchain, file=f)


    # time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    '''
    print(dt_string)

    
    print('Total call:',TotalCOI)
    print('Total put :',TotalPOI)
   
    print('Total Change in call:',TotalChangeCallOI)
    print('Total Change in put :',TotalChangePutOI)
    '''

    pcr = TotalPOI / TotalCOI
    chpcr = TotalChangePutOI / TotalChangeCallOI
    oid = TotalPOI - TotalCOI
    now = datetime.now()
    dt_s = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('CHpcr.txt','a') as f:
        print(dt_s,"CHPCR = ",chpcr, file=f)


    # writing a particular final data to a file
    org=[]
    orgdata = {
        'DATE/TIME': dt_string, 'COI': TotalCOI, 'POI': TotalPOI,
        'CALL CHNG OI': TotalChangeCallOI, 'PUT CHNG OI': TotalChangePutOI,'PCR':pcr ,'CHPCR':chpcr,'OI Difference':oid
    }
    org.append(orgdata)
    ratio = pd.DataFrame(org)
    print(ratio)
    with open('option_data.txt','a') as f:
        print(orgdata,file=f)


main()
