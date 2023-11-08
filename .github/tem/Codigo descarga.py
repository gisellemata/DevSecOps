import requests
import json
 
url_api = "http://18.218.244.166:8080/api/v2/{method}"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"
 
def get_products ():
    headers = { 
        'accept': 'application/json',
        'Authorization': api_key
    }
    r = requests.get(url_api.format(method = 'products'), headers = headers, verify = False)
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=4))

def create_products ():
    headers = {
        'accept': 'application/json',
        'Content-Tyoe': 'application/json',
        'Authorization': api_key
    }

data_product = {
  
  "name": "Giselle",
  "description": "Cocoro",
  "prod_numeric_grade": 29,
  "business_criticality": "very high",
  "platform": "web service",
  "lifecycle": "construction",
  "origin": "third party library",
  "user_records": 2147483647,
  "revenue": "52967283715.4",
  "external_audience": true,
  "internet_accessible": true,
  "enable_product_tag_inheritance": true,
  "enable_simple_risk_acceptance": true,
  "enable_full_risk_acceptance": true,
  "disable_sla_breach_notifications": true,
  "product_manager": 0,
  "technical_contact": 0,
  "team_manager": 0,
  "prod_type": 0,
  "sla_configuration": 0,
  "regulations": [
    0
  ]
}

r = requests.post(url_api.format(method = 'product/add'), json=data_product, headers = headers, verify = False)
    

print (r.status_code)
print (json.dumps(r.json(), indent=4))
if r.status_code == 201
    print (json.dumps(r.json(), indent=4))  


if __name__ == '__main__':

 def upload():

    

