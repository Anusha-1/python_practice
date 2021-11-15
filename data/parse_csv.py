#csv = json ==dict similar formats

# with open will take care of memory leaks

import csv
with open('names.csv','r') as csvfile:
    csv_reader=csv.DictReader(csvfile) #dict

    with open('new_names.csv','w') as newfile:
        fnames=['first_name','last_name']
        csvwriter=csv.DictWriter(newfile,fieldnames=fnames,delimiter=',',lineterminator='\n')
        csvwriter.writeheader()
        for line in csv_reader:
            del line['email']
            csvwriter.writerow(line)
        print("File created successfully")

print("csv export completed")
