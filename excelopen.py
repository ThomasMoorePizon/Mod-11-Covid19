import pandas
"pandas makes reading excel easy"

data = pandas.read_excel (r'C:\Users\shado\AppData\Local\Programs\Python\Python37\CV19.xlsx')
"read in the full excel spreadsheet downloaded from the CDC"

mydata = pandas.DataFrame(data, columns = ['COUNTYNAME','PUIsTotal','FLandNonFLDeaths'])
mydata['TotalCases'] = data['PUIsTotal'].sum()
mydata['TotalDeaths'] = data['FLandNonFLDeaths'].sum()
print (mydata)