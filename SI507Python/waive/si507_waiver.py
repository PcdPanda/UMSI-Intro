# encoding: utf-8
#################################
##### Name: Chongdan Pan
##### Uniqname: pandapcd
#################################

from bs4 import BeautifulSoup
import requests
import json
import secrets # file that contains your API key
from typing import Iterable, Dict


try:
    with open("cache.json", "r", encoding="utf-8") as f:
        CACHE = json.loads(f.read())
except Exception:
    CACHE = dict()

class NationalSite:
    '''a national site

    Instance Attributes
    -------------------
    category: string
        the category of a national site (e.g. 'National Park', '')
        some sites have blank category.
    
    name: string
        the name of a national site (e.g. 'Isle Royale')

    address: string
        the city and state of a national site (e.g. 'Houghton, MI')

    zipcode: string
        the zip-code of a national site (e.g. '49931', '82190-0168')

    phone: string
        the phone of a national site (e.g. '(616) 319-7906', '307-344-7381')
    '''
    
    def __init__(self, category: str, name: str, address: str, zipcode: str, phone: str):
        self.category = category
        self.name = name
        self.address = address
        self.zipcode = str(zipcode)
        self.phone = phone

    def info(self):
        return "{name} ({category}): {address} {zip}".format(name=self.name, category=self.category, address=self.address, zip=self.zipcode)


def request(url: str, params: Dict[str, str]=dict()) -> str:
    if url in CACHE.keys():
        print("Using cache")
        return CACHE[url]
    else:
        print("Fetching")
        res = requests.request("get", url).content.decode("utf-8")
        CACHE[url] = res
        with open("cache.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(CACHE))
    return res

def build_state_url_dict():
    ''' Make a dictionary that maps state name to state page url from "https://www.nps.gov"

    Parameters
    ----------
    None

    Returns
    -------
    dict
        key is a state name and value is the url
        e.g. {'michigan':'https://www.nps.gov/state/mi/index.htm', ...}
    '''
    prefix = "https://www.nps.gov"
    response = request(prefix)
    response = response.split("\n")[210].split("href=\"")
    ret = dict()
    for res in response:
        if "</a>" in res:
            val, key = res.split("</a>")[0].split(">")
            ret[key.lower()] = prefix + val[:-1]
    return ret

def get_site_instance(site_url) -> NationalSite:
    '''Make an instances from a national site URL.
    
    Parameters
    ----------
    site_url: string
        The URL for a national site page in nps.gov
    
    Returns
    -------
    instance
        a national site instance
    '''
    response = request(site_url).split("\n")
    for i, res in enumerate(response):
        if "class=\"Hero-title \">" in res:
            name = res.split("<")[1].split(">")[-1]
        elif "class=\"Hero-designation\">" in res:
            category = res.split("<")[1].split(">")[-1]
        elif "<span><span itemprop=\"addressLocality\">" in res:
            res = res.split("</span>")
            address = res[0].split(">")[-1] + ", " + res[1].split(">")[-1]
        elif "class=\"postal-code\"" in res:
            res = res.split("</span>")[0].split(">")[-1].replace(" ", "")
            zip_code = res
        elif "class=\"tel\"" in res:
            res = response[i+1]
            phone = res.split("<")[0]
    return NationalSite(category, name, address, zip_code, phone)


def get_sites_for_state(state_url):
    '''Make a list of national site instances from a state URL.
    
    Parameters
    ----------
    state_url: string
        The URL for a state page in nps.gov
    
    Returns
    -------
    list
        a list of national site instances
    '''
    sites = list()
    prefix = "https://www.nps.gov"
    response = request(state_url).split("\n")

    for res in response:
        if "</a></h3>" in res:
            site_url = prefix + res.split(">")[1][9:-1]
            sites.append(get_site_instance(site_url))
    return sites


def get_nearby_places(site_object: NationalSite) -> Dict[str, str]:
    '''Obtain API data from MapQuest API.
    
    Parameters
    ----------
    site_object: object
        an instance of a national site
    
    Returns
    -------
    dict
        a converted API return from MapQuest API
    '''
    zipcode = str(site_object.zipcode)
    if zipcode not in CACHE.keys():
        print("Fetching")
        params = {"origin": site_object.zipcode, "radius": 10, "maxMatches": 10, "ambiguities": "ignore", "outFormat":"json", "key": secrets.API_KEY}
        url = "http://www.mapquestapi.com/search/v2/radius"
        response = requests.get(url, params=params)
        response = json.loads(response.content)
        CACHE[zipcode] = response
        with open("cache.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(CACHE))
    else:
        print("Using cache")
        response = CACHE[zipcode]
    for place in response["searchResults"]:
        name = place["fields"]["name"]
        address = place["fields"]["address"]
        city = place["fields"]["city"]
        category = place["fields"]["group_sic_code_name"]
        if not city: city = "no city"
        if not address: address = "no address"
        if not category: category = "no category"
        print("- {name} ({category}): {address}, {city}".format(**locals()))
    return response
    
def part3():
    states = build_state_url_dict()
    while 1:
        name = input("Enter a state name (e.g. Michigan, michigan) or \"exit\"\n")
        if name == "exit": exit()
        elif name.lower() in states.keys():
            state_url = states[name.lower()]
            print("------------------------------")
            print("List of national sites in {}".format(states[name.lower()]))
            print("------------------------------")
            sites = get_sites_for_state(state_url)
            for i, site in enumerate(sites):
                print("[{}] {}".format(i + 1, site.info()))
        else:
            print("[Error] Enter proper state name\n")
            continue
        break

def part5():
    states = build_state_url_dict()
    while 1:
        name = input("Enter a state name (e.g. Michigan, michigan) or \"exit\"\n")
        if name == "exit": exit()
        elif name.lower() in states.keys():
            state_url = states[name.lower()]
            print("------------------------------")
            print("List of national sites in {}".format(states[name.lower()]))
            print("------------------------------")
            sites = get_sites_for_state(state_url)
            for i, site in enumerate(sites):
                print("[{}] {}".format(i + 1, site.info()))
            while 1:
                num = input("Choose the number for detail search or \"exit\" or \"back\"\n")
                if num == "exit": exit()
                elif num == "back":
                    break
                else:
                    try:
                        num = int(num) - 1
                        if num < 0: raise Exception
                        site = sites[num]
                        print("Places near {name}".format(name=site.name))
                        response = get_nearby_places(site)
                    except Exception:
                        print("[Error] Invalid Input")
        else:
            print("[Error] Enter proper state name\n")

if __name__ == "__main__":
    part5()
    # for i in range(2):
        # part3()
    # x = NationalSite("National Park", "Isle Royale", "Houghton, MI", 49630, "(906) 482-0984")
    # x = get_nearby_places(x)

