import json
import boto3
import yfinance as yf
from datetime import datetime

def Handler(event, context):
    monitor_list = event['monitor_list']
    monitor_list_name = event['monitor_list_name']
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
