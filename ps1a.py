## 6.0001 Pset 1: Part a 
## Name: Autumn Artist
## Time Spent: 1:00
## Collaborators: None

##########################################################################
## Get user input for annual_salary, portion_saved and total_cost below ##
##########################################################################
annual_salary = float(input("Enter yearly salary: "))
portion_saved = float(input("Enter portion of salary to save (decimal form): "))
total_cost = float(input("Enter cost of home: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
#down payment needed
portion_down_payment = 0.20*total_cost
current_savings = 0.0
r = 0.04
#monthly salary to be added to savings
monthly_salary = annual_salary*portion_saved/12
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

#increasing savings as months increase
while current_savings < portion_down_payment : 
    #start of month
    current_savings += current_savings*r/12
    #end of month
    current_savings += monthly_salary
    #counting months
    months += 1
    
print("Number of months:", months)