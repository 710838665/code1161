TODO: Reflect on what you learned this week and what is still unclear.
I know how to get information from the website by the vscode.
but I don't know how to do the wordy_pyramid.
And i also understand how to use the url.
 base = "http://api.wunderground.com/api/"
    api_key = "856182ae539f6718"
    country = "AU"
    city = "Sydney"
    template = "{base}/{key}/conditions/q/{country}/{city}.json"
    url = template.format(base=base, key=api_key, country=country, city=city)
    r = requests.get(url)
    the_json = json.loads(r.text)
    obs = the_json['current_observation']
    state = obs["display_location"]["state"]

    latitude = obs["display_location"]["latitude"]

    longitude = obs["display_location"]["longitude"]

    local_tz_offset = obs["local_tz_offset"]

    return {"state":           state,
            "latitude":        latitude,
            "longitude":       longitude,
            "local_tz_offset": local_tz_offset}


