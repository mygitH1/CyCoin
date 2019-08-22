from django.shortcuts import render

def home(request):
    import requests
    import json

    # Multiple Symbols Full Price Data from CrypoCompare
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BCH,LTC,EOS,XRP,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    # Latest News Article Data from CryptoCompare
    newsArticle_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    newsArticle = json.loads(newsArticle_request.content)

    return render(request, 'home.html', {'newsArticle': newsArticle, 'price' : price })

def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    else:
        notfound = "Please enter a crypto currency symbol within the search form above..."
        return render(request, 'prices.html', {'notfound' : notfound})