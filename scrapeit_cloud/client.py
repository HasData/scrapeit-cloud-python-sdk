from requests import request, Response

from .default_headers import default_headers

class ScrapeitCloudClient:
    api_url = "https://api.hasdata.com/scrape/web"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def scrape(
        self,
        params: dict,
        **kwargs
    ) -> Response:
        headers={
            "x-api-key": self.api_key
        }

        headers.update(default_headers)
        params["source"] = "python_sdk"

        return request("POST", self.api_url, json=params, headers=headers, **kwargs)
