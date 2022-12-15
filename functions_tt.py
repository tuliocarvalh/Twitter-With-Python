import tweepy as tw


bearer_token = ''
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


class functions :
    def tweets_recents() :
        cliente = tw.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
        pesquisa = input('pesquisa: ')
        resposta = cliente.search_recent_tweets(query=pesquisa)
        print("Tweets recentes: ")
        print(resposta)

    def search_tweets() :
        cliente = tw.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
        pesquisa = input('pesquisa: ')
        inicio = input("Data de inicio: ")
        final = input("Data final: ")
        resposta = cliente.search_recent_tweets(query=pesquisa,max_results=10,start_time=inicio,end_time=final)
        print(resposta)

