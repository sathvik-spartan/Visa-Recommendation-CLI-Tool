import requests
import argparse

API_BASE = 'https://api.henleypassportindex.com/api/passports'  # Open Source API Key

def get_country_codes():
    res = requests.get(API_BASE)
    data = res.json()
    return {item['name']: item['code'] for item in data if item.get('code')}

def get_visa_info(passport_code):
    res = requests.get(f"{API_BASE}/{passport_code}/countries")
    return res.json()['default']

def recommend_destinations(origin_country):
    country_codes = get_country_codes()
    normalized_country_codes = {k.lower(): v for k, v in country_codes.items()}

    if origin_country.lower() not in normalized_country_codes:
        print(f" Country '{origin_country}' not found.")
        print("🔍 Try one of these:")
        print(", ".join(sorted(country_codes.keys())))
        return

    print(f"\n Fetching destinations for passport: {origin_country}...\n")
    code = normalized_country_codes[origin_country.lower()]
    destinations = get_visa_info(code)

    visa_categories = {
        'Visa Free': [],
        'Visa on Arrival': [],
        'eVisa': [],
        'Visa Required': [],
        'Other': []
    }

    for dest in destinations:
        name = dest['name']
        if name.lower() == origin_country.lower():
            continue  # Skip own country (The country user typed - default passport)
        pivot = dest.get('pivot', {})
        is_visa_free = pivot.get('is_visa_free') == 1
        visa_category_raw = pivot.get('visa_category', '').lower()

        if is_visa_free:
            visa_categories['Visa Free'].append(name)
        elif 'arrival' in visa_category_raw:
            visa_categories['Visa on Arrival'].append(name)
        elif 'evisa' in visa_category_raw or 'electronic' in visa_category_raw:
            visa_categories['eVisa'].append(name)
        elif 'required' in visa_category_raw:
            visa_categories['Visa Required'].append(name)
        else:
            visa_categories['Visa Required'].append(name)  # Default to required if unknown

    # Display results
    for category, countries in visa_categories.items():
        print(f" {category} ({len(countries)} countries):")
        if countries:
            print(", ".join(sorted(countries)))
        else:
            print("None")
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visa Recommendation CLI using Henley Passport Index")
    parser.add_argument("country", nargs='?', help="Country of passport (e.g., India)")
    args = parser.parse_args()

    if args.country:
        country = args.country.strip()
    else:
        country = input("Enter your country of passport: ").strip()

    recommend_destinations(country)
