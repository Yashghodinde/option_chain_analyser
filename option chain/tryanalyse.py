
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
    print(response)
    rawdata = pd.DataFrame(response)
    rawop = pd.DataFrame(rawdata['filtered']['data']).fillna(0)
    print('This is length',len(rawop))

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

    def main():
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


        print('Total CALL OI',TotalCallOI)
        print('Total PUT OI',TotalPutOI)

        print('Change in call oi',TotalChangeCallOI)
        print('Change in put oi',TotalChangePutOI)


        print('The PCR =',TotalPutOI/TotalCallOI)
        print('The Change PCR =',TotalChangePutOI/TotalChangeCallOI)
        print('OI Difference',TotalPutOI-TotalCallOI)


while True:
    main()
    time.sleep(10)