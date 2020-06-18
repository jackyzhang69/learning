import requests
response = requests.get('GET https://lmi-wages-esdc-edsc-apicast-production.api.canada.ca/clmix-wsx/gcapis/wages/ca?noc=1111')
print(response)