# from hello_ani import ani

# ani("anuj")

D,deposit= input("enter the deposit amount").split()
deposit = int(deposit)
print(D,deposit)
print(type(D), type(int(deposit) ))
# deposit_sum=0
# print(type(deposit_sum))
# for i in deposit:
#     if deposit !="enter":
#         deposit_sum = deposit
W,withdraw_amount =input("enter the withdraw amount").split()
withdraw_amount =int(withdraw_amount)
print(W,withdraw_amount)
print(type(W),type(int(withdraw_amount)))
remainig_amount = deposit-withdraw_amount
print("Balace amount in Account:", remainig_amount)