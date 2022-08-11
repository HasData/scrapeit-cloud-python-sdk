# Scrapeit Cloud Python SDK
[Scrapeit Cloud](https://scrape-it.cloud/) - Web Scraping API with Proxy Rotation. Get valuable data at scale in HTML format from any website without need for a proxy.

Interface to call [Scrapeit Cloud API](https://scrape-it.cloud/) easily from Python.

## Install

    pip install scrapeit-cloud

## Usage
Signup to Scrapeit Cloud to  [get your API key](https://app.scrape-it.cloud/sign-up)  and some free credits to get started.

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
    '{"status":"ok","scrapingResult":{"content":"<!DOCTYPE html><html><head>\\n    <title>Example Domain</title>\\n\\n    <meta charset=\\"utf-8\\">\\n    <meta http-equiv=\\"Content-type\\" content=\\"text/html; charset=utf-8\\">\\n    <meta name=\\"viewport\\" content=\\"width=device-width, initial-scale=1\\">\\n    <style type=\\"text/css\\">\\n    body {\\n        background-color: #f0f0f2;\\n        margin: 0;\\n        padding: 0;\\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, \\"Segoe UI\\", \\"Open Sans\\", \\"Helvetica Neue\\", Helvetica, Arial, sans-serif;\\n        \\n    }\\n    div {\\n        width: 600px;\\n        margin: 5em auto;\\n        padding: 2em;\\n        background-color: #fdfdff;\\n        border-radius: 0.5em;\\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\\n    }\\n    a:link, a:visited {\\n        color: #38488f;\\n        text-decoration: none;\\n    }\\n    @media (max-width: 700px) {\\n        div {\\n            margin: 0 auto;\\n            width: auto;\\n        }\\n    }\\n    </style>    \\n</head>\\n\\n<body>\\n<div>\\n    <h1>Example Domain</h1>\\n    <p>This domain is for use in illustrative examples in documents. You may use this\\n    domain in literature without prior coordination or asking for permission.</p>\\n    <p><a href=\\"https://www.iana.org/domains/example\\">More information...</a></p>\\n</div>\\n\\n\\n</body></html>","headers":{"accept-ranges":"bytes","age":"477265","cache-control":"max-age=604800","content-encoding":"gzip","content-length":"648","content-type":"text/html; charset=UTF-8","date":"Thu, 11 Aug 2022 11:56:20 GMT","etag":"\\"3147526947\\"","expires":"Thu, 18 Aug 2022 11:56:20 GMT","last-modified":"Thu, 17 Oct 2019 07:18:26 GMT","server":"ECS (nyb/1D17)","vary":"Accept-Encoding","x-cache":"HIT"},"cookies":[]}}'
    >>>

Scrapeit Cloud supports various parameters to execute a custom JavaScript script, use a premium proxy from a specific geolocation and more.

You can find all the supported parameters on [Scrapeit Cloud documentation](https://scrape-it.cloud/docs/).
