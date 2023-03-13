import csv

with open("age.csv",'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # next(csv_reader) #skipping to first value
    
    ##creating new file
    with open("new_ages.csv","w") as new_file:
        
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            #writing to new file
            csv_writer.writerow(line)