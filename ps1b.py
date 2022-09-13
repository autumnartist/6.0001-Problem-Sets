## 6.0001 Pset 1: Part b
## Name: Autumn Artist
## Time Spent: 1:30
## Collaborators: None

##########################################################################################
## Get user input for annual_salary, portion_saved, total_cost, semi_annual_raise below ##
##########################################################################################
annual_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter portion of salary to save (decimal form): "))
total_cost = float(input("Enter cost of home: "))
semi_annual_raise = float(input("Enter the semi-annual raise (decimal form):" ))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.2*total_cost
current_savings = 0.0
r = 0.04
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while current_savings < portion_down_payment : 
    #start of month
    current_savings += current_savings*r/12
    #end of month
    months += 1
    #increase by factors of 6 (semi-annual)
    if months%6 == 0:
        annual_salary += annual_salary*semi_annual_raise     
    monthly_salary = annual_salary*portion_saved/12
    current_savings += monthly_salary
    
    
print("Number of months:", months)