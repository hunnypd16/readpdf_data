import camelot
file = '/home/hunny/Downloads/itr1.pdf'
tables = camelot.read_pdf(file, pages="all")
tables
tables[0].to_csv('foo.csv')
data = tables[0].df
tables
data
data.iloc[11][2]
name=data.iloc[3][1]
print(name)
pan=data.iloc[4][1]
print(pan)
Dob=data.iloc[5][1]
print(Dob)
block=data.iloc[7][2]
print(block)
nameofpremises=data.iloc[8][2]
print(nameofpremises)
roadstreet=data.iloc[9][2]
print(roadstreet)
area=data.iloc[10][2]
print(area)
town=data.iloc[11][2]
print(town)
state=data.iloc[12][2]
print(state)
country=data.iloc[13][2]
print(country)
pincode=data.iloc[14][2]
print(pincode)
aadharno=data.iloc[15][2]
print(aadharno)
status=data.iloc[16][2]
print(status)
mobileno_1=data.iloc[17][2]
print(mobileno_1)
stdcode="null"
print(stdcode)
landline="null"
print(landline)
import json
thisdict = {
    "name":name,
    "pan":pan,
    "Dob":Dob,
    "block":block,
    "nmaeofpremises":nameofpremises,
    "road":roadstreet,
    "area":area
}
# print(thisdict)
thisdict
y=json.dumps(thisdict,indent=2)
print(y)