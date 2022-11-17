def mobile_price_bdt (usd_price,  exchange_rate):
    bdt_price = usd_price * exchange_rate
    return bdt_price
samsung_bdt_price = mobile_price_bdt(180,106)
oppo_bdt_price = mobile_price_bdt(500,103)
print(samsung_bdt_price)
print(oppo_bdt_price)


