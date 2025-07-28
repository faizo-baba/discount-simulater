print ("welcome to khan shopping mall, enjoy 10% off over 1000 buy!")
items = ["1.handbag-500","2.shoes-400","3.shirt-300","4.shorts-400","5.pant-350"]
price = [500,400,300,400,350]
print ("avalible products")
for item in items :
    print (item)

user_choice1 = (int(input("choose your 1st item(1-1): ")))-1
user_choice2 = (int(input("choose your 2nd item(1-5): ")))-1
user_choice3 = (int(input("choose your 3rd item(5-1): ")))-1
 
total = price[user_choice1]+price[user_choice2]+price[user_choice3]

if total >=1000:
    discount = total * 0.10
    print (f"you got discount of Rs: {discount}")
    total-=discount    

print (f"your total bill is:{total}")
print ("thank you for shopping with us, have a good day")



