import csv, datetime
def findSubTimes(fileName):
    fh = open(fileName, "r") 
    csvFile = csv.DictReader(fh)
    subTimes = [] # to store submission times 
    for row in csvFile:
        dt = datetime.datetime.strptime(row["submission_submit_time"], "%H:%M:%S").time()
        sub = (dt.hour - 9) * 3600 + (dt.minute - 20) * 60 + dt.second
        subTimes.append(sub)
    fh.close() 
    return subTimes

import matplotlib.pyplot as py
subTimes = findSubTimes("submission_complete.csv")
# print(subTimes) # just testing
py.hist(subTimes) 
py.show()