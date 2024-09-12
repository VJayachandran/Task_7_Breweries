import requests

#function to create api requests to link URL with json 
def get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    if response.status_code == 200:
        breweries = response.json()
        return breweries
    else:
        print(f"Failed to fetch data for {state}")
        return []

#function to print the particular breweries state list 
def count_breweries_by_state(states):
    for state in states:
        breweries = get_breweries_by_state(state)
        print(f"\nBreweries in {state}: {len(breweries)}")
        if state == 'Alaska':
            alaska_breweries_with_websites = sum(1 for brewery in breweries if brewery['website_url'])
            print(f"Breweries in {state} with websites: {alaska_breweries_with_websites}")
        elif state == 'Maine':
            maine_breweries_with_websites = sum(1 for brewery in breweries if brewery['website_url'])
            print(f"Breweries in {state} with websites: {maine_breweries_with_websites}")
        elif state == 'New York':
            ny_breweries_with_websites = sum(1 for brewery in breweries if brewery['website_url'])
            print(f"Breweries in {state} with websites: {ny_breweries_with_websites}")

#function to print city list and breweries type
def count_brewery_types_by_city(states):
    for state in states:
        breweries = get_breweries_by_state(state)
        print(f"\nBrewery types by city in {state}:")
        cities = {}
        for brewery in breweries:
            city = brewery['city']
            brewery_type = brewery['brewery_type']
            if city not in cities:
                cities[city] = set()
            cities[city].add(brewery_type)
        for city, types in cities.items():
            print(f"{city}: {len(types)} types")

#this statement checks if the script is being run as main program
if __name__ == "__main__":
    states = ['Alaska', 'Maine', 'New York']
    count_breweries_by_state(states)
    count_brewery_types_by_city(states)