#import packages
import os
import csv

#python dict of abbreviated US States
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#create file path for csv file
csvpath = os.path.join('Resources/employee_data.csv')

#open and read csv file
with open(csvpath) as csvfile:

    employee_data = csv.reader(csvfile, delimiter=',')

    csv_header = next(employee_data)

    #create empty lists
    emp_id = []
    fname = []
    lname = []
    dob = []
    ssn = []
    state = []
    
    # Read each row of data after the header
    for row in employee_data:
        emp_id.append(row[0])
        fname.append(row[1].split(" ")[0])
        lname.append(row[1].split(" ")[1])
        dob.append(row[2].split("-")[1] + "/" + row[2].split("-")[2] +  "/" + row[2].split("-")[0])
        ssn.append('***-**-' + row[3].split("-")[2])
        
        for k,v in us_state_abbrev.items():
            if row[4] == k:
                state.append(v)

#zip lists together
zipped_data = zip(emp_id, fname, lname, dob, ssn, state)

# save the output file path
output_file = os.path.join("output","formatted_employee_data.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Emp_ID", "First_Name", "Last_Name", "DOB", "SSN", "State"])

    writer.writerows(zipped_data)

