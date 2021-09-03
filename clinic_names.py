import requests
from bs4 import BeautifulSoup
import pandas as pd

# return clinic name by passing clinic id
def get_clinic_name(clinic_id):
    url = f"https://{clinic_id}.portal.athenahealth.com/"
    respone = requests.get(url)
    html = respone.text
    soup = BeautifulSoup(html,"html.parser")
    clinic_name = soup.find_all("h1")[-1].text.strip()
    return clinic_name

# Set Start clinic id and End clinic id
start = 12690
end = 12800
clinic_names = []

# Loop throw every clinic id and extract clinic name
for clinic_id in range(start, end + 1):
    data_dict = {}
    data_dict['clinic_id'] = clinic_id
    data_dict['clinic_name'] = get_clinic_name(clinic_id)
    if data_dict['clinic_name'] != "Sorry, we can't find that practice. Make sure you typed the right address." and data_dict['clinic_name'] != "Payment Confirmation" and  len(data_dict['clinic_name']) != 0 :
        clinic_names.append(data_dict)
        print (data_dict['clinic_name'])

# Store date as data frame
df = pd.DataFrame(clinic_names)

# Save data to excel file
df.to_excel ('clinic_names.xlsx', index = False, sheet_name='clinic names')

print ("Done!")
  