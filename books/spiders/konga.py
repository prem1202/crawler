# -*- coding: utf-8 -*-
import requests
response = requests.get(
    "https://www.konga.com/category/laptops-5230",
    proxies={
        "http": "http://:@/",
    },
)
print(response.text)


