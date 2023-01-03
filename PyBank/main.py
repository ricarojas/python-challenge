import os

import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
print('hello')
print(csvpath)
with open("output_module3.txt", "w") as my_output_file:
    
    with open(csvpath) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        print(csv_reader.line_num)

        csv_header = next(csv_reader)
        print(f"CSV Header: {csv_header}")

        #row_count = sum(1 for row in csv_reader)
        row_count = 0
        pl_total = 0
        ave_pl = 0
        max_val = 0
        losses = []
        profit = []
        for row in csv_reader:
            row_count += 1
            pl_total += int(row[1])
            if int (row[1])>= 0:
                if max_val < int (row[1]):
                    max_val = int (row[1])
                profit.append(row[1])
            else:
                losses.append(row[1])

        ave_pl += pl_total // (row_count - 1)
        losses.sort()
        my_output_file.write ("Financial Analysis" + " \n")
        my_output_file.write ("----------------------------------------" + "\n")
        my_output_file.write ("Total months: "+ str (row_count)+ " \n")
        my_output_file.write ("Total: "+ str (pl_total)+ " \n")
        my_output_file.write ("Average Change: $"+ str (ave_pl)+ " \n")
        my_output_file.write ("Greatest increase in profits is: "+ str(max_val)+ " \n")
        my_output_file.write ("Greatest decrease in profits is: "+ str(losses[0])+ " \n")
        # headerline = "profit/losses"
        # pl_total = 0
        # for row in csv_reader:
        #     pl_total += int(row[1])
        # ave_pl = pl_total // 86
        #my_output_file.write ("Total : "+ str (pl_total))
        # print(f"Average Change: $", ave_pl)

        # headerline = "profit/losses"
        # profit = []
        # losses = []
        # max_val = 0
        # for row in csv_reader:
        #     if int (row[1])>= 0:
        #          if max_val < int (row[1]):
        #              max_val = int (row[1])
        #          profit.append(row[1])
        #     else:
        #          losses.append(row[1])
        # losses.sort()
        # print(f"The profits are: ", profit)
        # print(f"The losses are: ", losses)
        # print(f"The greatest increase in profits is: ", max_val)
        # print(f"The greatest decrease in profits is: ", losses[0])

        # for row in csv_reader:
        #     if int (row[1])==1141840:
        #         print (f"The greatest increase in profits was: ", row[0], row[1])
        #     if int (row[1])==-1066544:
        #         print (f"The greatest decrease in profits was: ", row[0], row[1])

    my_output_file.close()
    