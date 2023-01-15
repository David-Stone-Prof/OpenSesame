import os
from datetime import datetime as dt

def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

# folder = r'C:\Users\david\Documents\_Stone\Family_Leave\Stone_Kroger_PayStubs\\'
folder = r'C:\Users\david\Documents\_Stone\Family_Leave\Stone_Kroger_PayStubs\newfolder\\'
print(os.listdir(folder))
count = 1
# count increase by 1 in each iteration
# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name
    if right(file_name,8) == "2020.pdf":
        source = folder + file_name
        print(source)

    source = folder + file_name
    # Adding the count to the new file name and extension
    year = mid(file_name,6,4)
    month = left(file_name,2)
    day = mid(file_name,3,2)
    print("year: ",year,"month: ",month, "day: ",day)
    readname = file_name.replace(file_name, "{}-{}-{}.pdf")
    destination = folder + readname
    print("Destination: ",destination)

    # Renaming the file
    os.rename(source, destination)
    # count += 1
print('All Files Renamed')

print('New Names are')
# verify the result
res = os.listdir(folder)
print(res)