from calendar import c
from http.client import HTTPResponse
from unicodedata import decimal
from django.shortcuts import render
from django.http import JsonResponse
import chatswap.swapscripts.tokenlist as tokenlist
# import chatswap.swapscripts.zrxrequests as zrxrequests

def index(request):
    tokensRaw = tokenlist.getTokenData("https://tokens.coingecko.com/uniswap/all.json")
    tokens = []
    for i in tokensRaw:
        ticker = i["ticker"]
        contract = i["address"]
        decimals = i["decimals"]
        tokens.append(tokenlist.token(ticker, decimals, contract))
    tokens.append(tokenlist.token("ETH", 18, "ETH"))
    context = {"tokenData": tokens}
    return render(request, "chatswap/index.html", context)

#Temporary view function serving to render the new iteration of the main page of the chat swap app. 
def newIndex(request):
    tokensRaw = tokenlist.getTokenData("https://tokens.coingecko.com/uniswap/all.json")
    tokens = []
    for i in tokensRaw:
        ticker = i["ticker"]
        contract = i["address"]
        decimals = i["decimals"]
        tokens.append(tokenlist.token(ticker, decimals, contract))
    tokens.append(tokenlist.token("ETH", 18, "ETH"))
    context = {"tokenData": tokens}
    return render(request, "chatswap/NewIndex.html", context)
# def pullPrice(request, sellTokenAddress, buyTokenAddress):
#     return JsonResponse({"price": zrxrequests.pullPrice(sellTokenAddress, buyTokenAddress)})