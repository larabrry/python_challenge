#Dependencies
import csv

#files to load and output
file_to_load = "C:\\Users\\larab\\OneDrive\\Documents\\GitHub\\vba_challenge\\budget_data.csv"
file_to_output = "C:\\Users\\larab\\OneDrive\\Documents\\GitHub\\pybank_analysis.txt"

#track various revenue parameters
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0] 
greatest_decrease = ["", 999999999999999999]
total_revenue = 0
PL_changes_average=0

#read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)    
    for row in reader:
        
        total_months = total_months + 1  #calculate the number of rows and tell us the total months          
        total_revenue = total_revenue + int(row["Profit/Losses"]) #add the value of revenue for each row, specify the value as integer
        if total_months>1:
            revenue_change_list.append(int(row["Profit/Losses"])-prev_revenue) #calculate the changes in profit/losses
            month_of_change.append(row['Date']) #add the date that corresponds with the P/L changes
        prev_revenue= int(row["Profit/Losses"]) #update the prev_revenue to equal the current P/L value
    
    PL_changes_average= round(sum(revenue_change_list)/(total_months-1))  #calculate the average pf the P/L changes
  
    for i  in range( len(revenue_change_list)):
        if revenue_change_list[i]>0:                                #calculate the greatest increase in profit 
            if greatest_increase[1] <=  revenue_change_list[i]:     #amount
                greatest_increase[1]=revenue_change_list[i]
                greatest_increase[0]=month_of_change[i]             #date
 
        elif revenue_change_list[i]<0:                              #calculate the greatest decrease in profit
            if greatest_decrease[1] >=  revenue_change_list[i]:     #amount 
                greatest_decrease[1]=revenue_change_list[i]         
                greatest_decrease[0]=month_of_change[i]             #date
 
 #format the results
    result=f'''                                                    
Financial Analysis
----------------------------

Total Months: {total_months}
Total: ${total_revenue}
Average Change: ${PL_changes_average}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
'''
    
    print(result)                                                   #print the results to the terminal

    with open('pybank_analysis.txt','w') as f:                      #export a txt file with the results  
        f.write(result)
    
 