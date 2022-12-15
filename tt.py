from socket import if_indextoname
from functions_tt import functions


pesquisar = input("Tipo de pesquisa: ")


while True :

     if pesquisar == '1' :
        functions.tweets_recents()
        
    
     elif pesquisar == '2' :
        functions.search_tweets()
        
    
    

