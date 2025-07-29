import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/astronomyapi-astronomyapi-default/api/astronomy'

mcp = FastMCP('astronomy')

@mcp.tool()
def get_all_bodies_positions(latitude: Annotated[Union[int, float], Field(description='Default: 33.775867')],
                             longitude: Annotated[Union[int, float], Field(description='Default: -84.39733')],
                             from_date: Annotated[Union[str, datetime], Field(description='Date (yyyy-mm-dd)')],
                             to_date: Annotated[Union[str, datetime], Field(description='Date (yyyy-mm-dd)')],
                             elevation: Annotated[Union[int, float, None], Field(description='Default: 166')] = None,
                             time: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Returns a iterable list of bodies and their properties in tabular format.'''
    url = 'https://astronomy.p.rapidapi.com/api/v2/bodies/positions'
    headers = {'x-rapidapi-host': 'astronomy.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'from_date': from_date,
        'to_date': to_date,
        'elevation': elevation,
        'time': time,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_positions_for_body(latitude: Annotated[Union[int, float], Field(description='Default: 33.775867')],
                           longitude: Annotated[Union[int, float], Field(description='Default: -84.39733')],
                           from_date: Annotated[Union[str, datetime], Field(description='Date (yyyy-mm-dd)')],
                           to_date: Annotated[Union[str, datetime], Field(description='Date (yyyy-mm-dd)')],
                           elevation: Annotated[Union[int, float, None], Field(description='Default: 166')] = None,
                           time: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Returns properties of the given body for the given date range in tabular format. Supported bodies are "sun" ,"moon", "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"'''
    url = 'https://astronomy.p.rapidapi.com/api/v2/bodies/positions/venus'
    headers = {'x-rapidapi-host': 'astronomy.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'from_date': from_date,
        'to_date': to_date,
        'elevation': elevation,
        'time': time,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(exact: Annotated[Union[str, None], Field(description='')] = None,
           match_type: Annotated[Literal['exact', 'fuzzy', None], Field(description='')] = None,
           ra: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           dec: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           limit: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           order_by: Annotated[Literal['name', None], Field(description='')] = None) -> dict: 
    '''Search endpoint can be used to get information for stars and deep space objects.'''
    url = 'https://astronomy.p.rapidapi.com/api/v2/search'
    headers = {'x-rapidapi-host': 'astronomy.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'exact': exact,
        'match_type': match_type,
        'ra': ra,
        'dec': dec,
        'limit': limit,
        'offset': offset,
        'order_by': order_by,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def generate_moon_phase(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Generate an image of the Moon based on the given parameters.'''
    url = 'https://astronomy.p.rapidapi.com/api/v2/studio/moon-phase'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'astronomy.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def generate_star_chart(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Generates a star chart with the given parameters, and returns the url'''
    url = 'https://astronomy.p.rapidapi.com/api/v2/studio/star-chart'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'astronomy.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
