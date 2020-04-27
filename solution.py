import csv

filFile = open("filteredCountry.csv","w+") # Creates FilterCountry file
output = open("output.csv","w+") # Creates output file 

# Reads from main.csv and Filters accoridng to country 'USA'
with open('main.csv' ,newline='') as File:
    reader = csv.DictReader(File)
    fieldname = reader.fieldnames   # reades the headers 
    writer = csv.DictWriter(filFile,fieldname)
    writer.writeheader()    # writes the header
    for row in reader:
        if 'USA'in row['COUNTRY'] :     # checks if country is 'USA'
            writer.writerow(row)  # writes to file FilterCountry..


with open('filteredCountry.csv',newline='') as File:
    fl = ['SKU','FIRST_MINIMUM_PRICE','SECOND_MINIMUM_PRICE'] # Fieldnames
    dwriter = csv.DictWriter(output,fl)
    dwriter.writeheader()   # writes fieldnames in file header
    dreader = csv.DictReader(File)  # Reads FilterCou.. file
    temp = dict() # to Store sku and their prices temprarely
    for row in dreader:
        try :
            price = float(row['PRICE'][1::])  # converts into float
            sku = row['SKU']
            if sku not in temp:
                # adds first minimum price of sku
                temp[sku] = [price]
            elif sku in temp :
                if len(temp[sku]) == 1:
                    # adds second minimum price of sku
                    temp[sku].append(price)
                    temp[sku].sort()
                else:
                    if temp[sku][0] > price :
                        # swaps number if minimum price found
                        temp[sku][1] , temp[sku][0] = temp[sku][0] ,price
        except:   # Because lot of currupted data availible in rows
            pass
    bigl = []
    for key,values in temp.items():
        if len(values) > 1 :
            l = []
            l.append(key)
            l.extend(values)
            bigl.append(l)
    writer = csv.writer(output)
    # writes to output.csv file
    writer.writerows(bigl)
