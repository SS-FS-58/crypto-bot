from api import BinanceAPI
client = BinanceAPI('8SqwIw1lYhaxQZa9LSCUx2wjN1GqguDDAuewtKUCKmUlO4uwXoQ3ylz0Efs','5Phlc0ldADa6rQYJANguTIe1mSekiSTN2SiaowBPcs2gXi3wsgQ2TCQssmo4B')

ping = client.time()
print(ping)