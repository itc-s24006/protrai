#s24006
#消費税１０％を計算するプログラム


def postTaxPrice(price):
    ans = int(price * 1.1)
    return ans

print(postTaxPrice(120),"円")
print(postTaxPrice(128),"円")
print(postTaxPrice(980),"円")
