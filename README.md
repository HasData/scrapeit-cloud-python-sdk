# HasData Python SDK
[HasData](https://hasdata.com/) - Web Scraping API with Proxy Rotation. Get valuable data at scale in HTML format from any website without need for a proxy.

Interface to call [HasData API](https://hasdata.com/) easily from Python.

## Install

    pip install scrapeit-cloud

## Usage
Signup to HasData to  [get your API key](https://app.hasdata.com/sign-up)  and some free credits to get started.

    >>> from scrapeit_cloud import ScrapeitCloudClient
    >>>
    >>> client = ScrapeitCloudClient(api_key='INSERT_YOUR_API_KEY_HERE')
    >>>
    >>> response = client.scrape(
        params={
            "url": "https://example.com"
        }
    )
    >>>
    >>> response.text
    '{"requestMetadata":{"id":"...","status":"ok",...},"content":"<!DOCTYPE html><html lang=\\"en\\"><head>...<title>Example Domain</title>...</html>","headers":{...},"statusCode":200,"cookies":[]}'
    >>>

HasData supports various parameters to execute a custom JavaScript script, use a premium proxy from a specific geolocation and more.

You can find all the supported parameters on [HasData documentation](https://docs.hasdata.com/apis/web-scraping-api/api-params).
