import csv

budget_csv = 'budget_data.csv'

def print_file(statement, file_pointer) :
    print (statement)
    file_pointer.write(str(statement) + "\n")
with open('myfile.txt',"w") as f :
    with open(budget_csv, 'r') as csvfile:
    
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        # Prompt the user for what wrestler they would like to search for
        next(csvreader)
    
        # Loop through the data
        sum_of_profitloss = 0
        num_months        = 0 
        change            = 0 
        max_val =  -999999999999
        min_val =  999999999999
        for row in csvreader:
            sum_of_profitloss = sum_of_profitloss + int(row[1])
            num_months = num_months + 1 
            if num_months == 1 :
                prev_val = int(row[1])
                continue 
            if num_months >= 2 :
                diff = int(row[1]) -  prev_val
                change =  change + diff
                #print (row[0])
                #print ( "nw  :  " + str(row[1]) +  "   prev_Val :" + str(prev_val) + "  change : " + str(change))
                prev_val = int(row[1])
                if max_val < diff :
                    max_val = diff 
                    max_month = row[0]
                    #print ( "Value : " + str(max_val))
                if min_val > diff :
                    min_val = diff
                    min_month = row[0]
    
    
    print_file ('Financial Analysis ',f)
    print_file ('---------------------------',f)
    print_file (str(' Total Months    :  ' + str(num_months)),f)
    print_file (str(' Total amount       : $' + str(sum_of_profitloss)),f)
    roundval =format((float((change)/(num_months-1))) , ".2f" )
    print_file (str(' Average change     : $ ' + str(roundval)),f)
    print_file (str(' Greatest Increase  : ' + str(max_month) + ' : $ '  + str(max_val) ),f)
    print_file (str(' Greatest Decrease  : ' + str(min_month)  + ' : $ '  +str(min_val)),f)
