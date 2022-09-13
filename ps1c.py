## 6.0001 Pset 1: Part c
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
total_cost = 800000
portion_down_payment = 0.2
down_payment = total_cost*portion_down_payment
months = 36
high = 1.0
low = 0.0
r = (high+low)/2
current_savings = initial_deposit*(1+r/12)**months
steps = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
while (current_savings <= down_payment-100) or (current_savings > down_payment+100):
    if current_savings > down_payment:
        high = r
    else:
        low = r
    r = (high+low)/2
    current_savings = initial_deposit*(1+r/12)**months
    if initial_deposit >= down_payment-100:
        r = 0
        break
    if initial_deposit*(1+1/12)**months< down_payment:
        r = None
        break
    steps += 1


print("Best savings rate:", r)
print("Steps in bisection search:", steps)

