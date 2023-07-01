import requests
import json
from algoliasearch.search_client import SearchClient


def process_response(response):
    response_dict = json.loads(response)
    print(response_dict)
    required_data_dict = {}
    
    # required_data_dict["temperature"] = response_dict["current"]["temp_c"]
    # required_data_dict["conditions"] = response_dict["current"]["condition"]["text"]
    # required_data_dict["feels_like"] = response_dict["current"]["feelslike_c"]
    # required_data_dict["wind_speed"] = response_dict["current"]["wind_kph"]
    # required_data_dict["humidity"] = response_dict["current"]["humidity"]
    # required_data_dict["visibility"] = response_dict["current"]["vis_km"]
    # required_data_dict["precipitation"] = response_dict["current"]["precip_mm"]
    # required_data_dict["uv_index"] = response_dict["current"]["uv"]

    return required_data_dict

def request_weather_information():

    

    client = SearchClient.create("M8WP0L5M62", "470a772391acc8c49c3e0880cacfea21")
    index = client.init_index("my_first_index")
    res = index.search('coles')
    print(res)
    
    

    # response = requests.request("POST", url, headers=headers, params=querystring)


    # processed_response = process_response(response.text)

    # return processed_response