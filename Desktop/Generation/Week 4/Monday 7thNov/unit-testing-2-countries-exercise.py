# Write unit-tests for
# 1. get_country_code

def get_country_code(countries: list, country_name: str):
    for country in countries:
        if country['name'] == country_name:
            return country['alpha3Code']
    return None


#  2.get_country_currency

def get_country_currency(countries: list, country_name: str):
    for country in countries:
        if country['name'] == country_name:
            return country['currencies'][0]['code']
    return None

# 3. transform

# def transform(name: str):
#     countries = get_countries()
#     code = get_country_code(countries, name)
#     currency = get_country_currency(countries, name)

#     return {"name": name, "country_code": code, "currency_code": currency}

# 4.show_country_info

# def show_country_info():
#     countries = display_countries()
    
#     selected_country_idx = int(input("Please choose a country: "))
    
#     name = countries[selected_country_idx]['name']
#     result = transform(name)
#     print(result)
    
# show_country_info()
