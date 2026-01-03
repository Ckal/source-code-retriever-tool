import requests
from bs4 import BeautifulSoup
from transformers import Tool


class ScrapperTool(Tool):
    name = "source_code_scrapper"
    description = (
        "This is a tool that retrieves the source code of a given webpage. "
        "It takes the URL of the webpage, and returns the source code."
    )

    inputs = ["text"]
    outputs = ["text"]

    def __call__(self, url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.prettify()
