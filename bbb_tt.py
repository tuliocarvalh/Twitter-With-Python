import tweepy as tw
import pandas as pd
# Obtenha as chaves necessarias da API do Twitter
bearer_token = ''
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Conexao
cliente = tw.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)


start = '2022-02-01T19:39:01Z'
end = '2022-02-01T19:40:01Z'

resposta = cliente.search_recent_tweets(query='BBB',max_results=100,start_time=start,end_time=end)

dados = resposta.data

base = []

for i in dados:
    
    linha = [0 for j in range(22)]
    
    linha[0] = i.text
    
    texto = i.text
    
    if('RT' in texto):
        posicao = texto.find(':')
        texto = texto[posicao+2:]
        linha[21] = 1
        
    linha[1] = 1 if ('laís caldas' in texto.lower() or 'lais caldas' in texto.lower() or 'laís' in texto.lower() or 'lais' in texto.lower()) else 0
    linha[2] = 1 if ('luciano estavan' in texto.lower() or 'luciano' in texto.lower()) else 0
    linha[3] = 1 if ('jessilane alves' in texto.lower() or 'jessilane' in texto.lower()) else 0
    linha[4] = 1 if ('eliezer' in texto.lower()) else 0
    linha[5] = 1 if ('eslovênia marques' in texto.lower() or 'eslovênia' in texto.lower() or 'eslovenia marques' in texto.lower() or 'eslovenia' in texto.lower()) else 0
    linha[6] = 1 if ('lucas bissoli' in texto.lower() or 'lucas' in texto.lower()) else 0
    linha[7] = 1 if ('bárbara heck' in texto.lower() or 'bárbara' in texto.lower() or 'barbara heck' in texto.lower() or 'barbara' in texto.lower()) else 0
    linha[8] = 1 if ('arthur aguiar' in texto.lower() or 'arthur' in texto.lower()) else 0
    linha[9] = 1 if ('rodrigo' in texto.lower()) else 0
    linha[10] = 1 if ('natália' in texto.lower() or 'natalia' in texto.lower()) else 0
    linha[11] = 1 if ('vinícius' in texto.lower() or 'vinicius' in texto.lower() or 'vyni' in texto.lower()) else 0
    linha[12] = 1 if ('pedro scooby' in texto.lower() or 'pedro' in texto.lower()) else 0
    linha[13] = 1 if ('brunna gonçalves' in texto.lower() or 'brunna' in texto.lower() or 'brunna goncalves' in texto.lower()) else 0
    linha[14] = 1 if ('paulo andré' in texto.lower() or 'paulo' in texto.lower() or 'paulo andre' in texto.lower()) else 0
    linha[15] = 1 if ('maria' in texto.lower()) else 0
    linha[16] = 1 if ('jade picon' in texto.lower() or 'jade' in texto.lower()) else 0
    linha[17] = 1 if ('douglas silva' in texto.lower() or 'douglas' in texto.lower()) else 0
    linha[18] = 1 if ('linn da quebrada' in texto.lower() or 'linn' in texto.lower()) else 0
    linha[19] = 1 if ('tiago abravanel' in texto.lower() or 'tiago' in texto.lower()) else 0
    linha[20] = 1 if ('naiara azevedo' in texto.lower() or 'naiara' in texto.lower()) else 0  
    
    base.append(linha)

    baseBBB = pd.DataFrame(base)
    baseBBB.columns = ['texto','lais','luciano','jessilane','eliezer','eslovênia','lucas','bárbara','arthur','rodrigo','natália','vinícius','scooby','brunna','paulo','maria','jade','douglas','lina','tiago','naiara','RT']
    print(baseBBB)

