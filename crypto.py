#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

#eliott.bureau@ynov.com

import os
import cryptocompare

while True:
    choix = input("Appuyer sur (A) pour afficher les cryptomoney ou sur (C) pour entrer le nom d'une cryptomoney : ")
    if choix == 'A':
        for [key,value] in cryptocompare.get_coin_list(format=False).items():
            print(value.get("CoinName"))

    elif choix == 'C':
        os.system('clear')
        selection = input("Veuillez choisir une cryptomoney : ")
        for [key,value] in cryptocompare.get_coin_list(format=False).items():
            if selection.lower() == value.get("CoinName").lower():
                print(value.get("CoinName")+" : "+str(cryptocompare.get_price(key)))


#while 1:
#    selection = int(input("Veuillez choisir une cryptomoney : "))
#    if selection == 'Id':
#        crypto_result = cryptocompare.get_price(cryptocompare.get_coin_Id)
#        print(crypto_result)
#    break

#while 1:
#    select_one = int(input("Choisissez votre cryptomoney \n 1. Bitcoins \n 2. Ethereum \n Votre choix : "))
#    if select_one == 1:
#        crypto_one = cryptocompare.get_price('BTC')
#        print (crypto_one)
#    elif select_one == 2:
#        crypto_two = cryptocompare.get_price('ETH')
#        print (crypto_two)
#    break
