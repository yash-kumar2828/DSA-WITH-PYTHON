# WAP to provide discounted price as per below conditions:
# 	if shopping price>=10000 then %discount=40%
# 	shopping price>=6000 and <=9999 then %discount=30%
# 	shopping price>=3000 and <=5999 then %discount=20%
# 	shopping price>=1 and <=2999 then %discount=8%


shoppingPrice = float(input("Enter your shopping price : "))

if shoppingPrice>=10000:
    discount = (shoppingPrice*40)/100

elif shoppingPrice>=6000 and shoppingPrice<10000:
    discount = (shoppingPrice*30)/100

elif shoppingPrice>=3000 and shoppingPrice<6000:
    discount = (shoppingPrice*20)/100

elif shoppingPrice>=1 and shoppingPrice<3000:
    discount = (shoppingPrice*8)/100

else:
    discount = 0

print(f"Your shopping price is {shoppingPrice} and your discount is {discount} and your total bill is : {shoppingPrice-discount}")