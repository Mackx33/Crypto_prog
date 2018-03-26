#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

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
