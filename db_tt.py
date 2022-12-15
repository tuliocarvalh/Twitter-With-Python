
import tweepy as tw
import pandas as pd
import time
import sqlite3

bearer_token = ''
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

cliente = tw.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

con = sqlite3.connect('DB_Itaipava.db')

cur = con.cursor()

start = '2022-07-23T08:00:00Z'
end = '2022-07-23T16:01:00Z'

resposta = cliente.search_recent_tweets(query='itaipava',max_results=100,start_time=start,end_time=end)

#print(resposta)

dados = resposta.data


cur.execute('CREATE TABLE registros (texto TEXT,RT TEXT)')

for i in dados:
    texto = i.text
    if (texto[:2] == 'RT'):
        RT = 'S'
    else:
        RT = 'N'
    
    cur.execute("INSERT INTO registros (texto,RT) VALUES (?,?)",(texto,RT))
    
con.commit()   

con.close()