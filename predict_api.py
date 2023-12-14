import os
import pandas as pd
import requests
import json

os.system("wget https://minio.lab.sspcloud.fr/projet-formation/diffusion/mlops/data/data_to_classify.parquet")


print(pd.read_parquet("data_to_classify.parquet"))

data_to_classify = pd.read_parquet("data_to_classify.parquet")
for index in data_to_classify.index:
    text_to_classify = data_to_classify.loc[index, "text"]
    print(f"text_to_classify = {text_to_classify}")
    text_request = f"description={'%20'.join(text_to_classify.split())}&nb_echoes_max=5"
    response = requests.get(url=f"http://eti-mag-api.lab.sspcloud.fr/predict?{text_request}")

    print(json.loads(response.content))
