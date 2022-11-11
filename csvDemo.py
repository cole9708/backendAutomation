import csv

with open('C:\\Users\\cole9\\PycharmProjects\\BackEndAutomation\\test.csv') as c:
    csvReader =csv.reader(c, delimiter=',')
    my_list = list(csvReader)
    names =[]
    status=[]
    for i in my_list:
        print(i)
        names.append(i[0])
        status.append(i[1])
print(names)
print(status)



with open('C:\\Users\\cole9\\PycharmProjects\\BackEndAutomation\\test.csv', 'a') as wFile:
    csvWriter =csv.writer(wFile)
    csvWriter.writerow(["Bob","Rejected"])
    print(wFile)



