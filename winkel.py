# Shoping program
persoon = float(input("split the cost in: "))
articles = []

# get input and store in list
while True:
    article = float(input("what does the article cost (done type: '1001'): "))

    if article > 0 and article < 1000:
        articles.append(article)
    else:
        break

# calculate the price of articles
def calc_amout_per_persoon(articles):
    per_peroon = 0
    for article in articles:
        per_peroon += article
        
    return per_peroon / persoon

# output 
print("everybody pays: " + str(calc_amout_per_persoon(articles)))
