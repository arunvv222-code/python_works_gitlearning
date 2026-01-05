prooduct={"code":123,"title":"shirt","colour":"blue","size":"m","prize":1500,"offer":240}

#add offer of 100 rs if offer not exist else update offer as current offerr +50

if "offer" in prooduct:
    prooduct["offer"]+=50
else:
    prooduct["offer"]=100
print(prooduct)