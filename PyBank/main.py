import os
import csv

#Set the csv (read from) and text (write to) file paths using the os module (imported above)
budget_data_csv_path = os.path.join("Resources/budget_data.csv")
#text_path = os.path.join('Analysis/", "budget_analysis.txt')

file_name = 'budget_data.csv'

#Creates variables
total_months = 0
total_profit_loss = 0
greatest_increase = 0
greatest_decrease = 0
average_change = 0
number_months = 0
changing_sum = 0
changing_month = 0
greatest_increase_month = 0
greatest_decrease_month = 0
last_month = 0
total = 0
changes = []
dates = []

#Location of data to pull from
csvpath = "Resources/budget_data.csv"

#Open and read data from csv file using the Delimiter
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')

 #find header line and skip it
    csv_header =  next(csvfile)
    
   

 #Start pulling data from CSV file to manipulate it into the required categories
    for row in csv_reader:
         
        date = row[0]
    
        change = row[1]
       
        dates.append(date)
         
        changes.append(change)

        #Calculate the total months & total
        number_months = number_months + 1
        total_months = total_months + int(row[1])


for changing_month in range (number_months - 1):
    average_change = average_change + float(changes[changing_month + 1]) - float(changes[changing_month])
    changing_sum = (float(changes[changing_month + 1]) - float(changes[changing_month]))

    #determine greatest increase
    if changing_sum > greatest_increase:
        greatest_increase = changing_sum
        greatest_increase_month = changing_month
    else:
        greatest_increase = greatest_increase
         
    #determine greatest decrease
    if changing_sum < greatest_decrease:
        greatest_decrease = changing_sum
        greatest_decrease_month = changing_month
    else:
        greatest_decrease = greatest_decrease

     # before printing format the calculated values after loop
    
    average_change = changing_sum / int(number_months)
    
    # Print Out the results of data pulled to terminal
    print(f"Financial Analysis")
    print (" ")
    print ("-------------------------------")
    print (" ")
    print(f"Total Months: {number_months}")
    print(f'Total:  ${total_months}')
    print(f"Average Change:  {average_change}")
    print(f"Greatest Increase in Profits:")
    print(f"Greatest Decrease in Profits:")

#Declare the output file we want to write the above results to & write to that file
output_file = "output.txt"
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial_Analysis"])
    writer.writerow([])
    writer.writerow(["-------------------------------"])
    writer.writerow(["total_months: " + str(number_months)])
    writer.writerow(["total: $" + str(total_months)])
    writer.writerow(["average_change: $" '{:.2f}' .format(average_change/(number_months - 1),2)])
    writer.writerow(["greatest_increase_in_profits: " + str(greatest_increase_month) + " (" + str(greatest_increase + 1) + ")" ])
    writer.writerow(["greatest_decrease_in_profits: " + str(greatest_decrease_month) + " (" + str(greatest_decrease + 1) + ")" ])
    
