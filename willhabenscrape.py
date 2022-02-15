import requests
import 

page = 1 
rows = 100 #how many results are displayed - 100 is max

response = requests.get(f"https://www.willhaben.at/iad/immobilien/mietwohnungen/mietwohnung-angebote?sfId=172fc0d6-3091-49c9-bd11-1cfc4c87e78e&isNavigation=true&areaId=117223&areaId=117224&areaId=117225&areaId=117226&areaId=117227&areaId=117228&areaId=117229&areaId=117230&areaId=117231&areaId=117237&areaId=117238&areaId=117239&areaId=117240&NO_OF_ROOMS_BUCKET=3X3&NO_OF_ROOMS_BUCKET=4X4&NO_OF_ROOMS_BUCKET=5X5&NO_OF_ROOMS_BUCKET=6X9&NO_OF_ROOMS_BUCKET=10X&NO_OF_ROOMS_BUCKET=0X0&page={page}&rows={rows}&PRICE_TO=1400&ESTATE_SIZE/LIVING_AREA_FROM=80")

print(response.content)