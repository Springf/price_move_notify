import json
import boto3
import yfinance as yf
from datetime import datetime

def Handler(event, context):
    monitor_list = {
        'D05.SI': 18,
        'AWX.SI': 3.1,
        '5G3.SI': 0.36,
        'AAPL': 100,
        'VL6.SI': 0.56,
        'OV8.SI': 1.2,
        '1D0.SI': 0.19,
        '1F2.SI': 0.4,
        'BN4.SI': 4.3,
        'S68.SI': 8,
        '558.SI': 0.9,
    }
    monitor_list_name = {
        'D05.SI': 'DBS',
        'AWX.SI': 'AEM',
        '5G3.SI': 'TalkMed',
        'AAPL': 'Apple',
        'VL6.SI': 'Koufu',
        'OV8.SI': 'ShengSiong',
        '1D0.SI': 'Kimly',
        '1F2.SI': 'UnionGas',
        'BN4.SI': 'Keppel',
        'S68.SI': 'SGX',
        '558.SI': 'UEM',
    }
    message = ''
    for p in monitor_list:
        ticker = yf.Ticker(p)
        #name = ticker.info['shortName']
        history = ticker.history('1d');
        price = round(history.Close[0],4)
        date = history.index[0]
        if(price <= monitor_list[p]):
            msg = f'ATTN: {monitor_list_name[p]} closed at {price} on {date.strftime("%Y-%m-%d")} below {monitor_list[p]}'
        else:
            msg = f'{monitor_list_name[p]} closed at {price} on {date.strftime("%Y-%m-%d")}'
        message += msg + '\n'

    print(message)

    sns = boto3.client('sns')
    
    response = sns.publish(
        TopicArn='arn:aws:sns:ap-southeast-1:872764013972:company_annoucement',    
        Message= message,
        Subject = f'Price Monitoring for {datetime.today()}'
        )
    print(f'Sent: {response}')
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
