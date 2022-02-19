from translate import Translator
import pandas as pd
from pathlib import Path

"""
    This script is responsible for generating Eng_data_with_cluster_f
    which has the name of countrys in english
    the translate api can only translat 56 word per 7h
                                                        """

path = Path.cwd() / "data"
property = ["pays","cluster_km","cluster_km_2","cluster_km_5"]
df = pd.read_csv(path / "data_with_clusters.csv")[property]
translator = Translator(from_lang="french",to_lang="english")

for i in df.index:
    result = translator.translate(df.pays[i])
    df.pays[i] = result
    print(df.pays[i])

df.to_csv(path / 'ENG_data_with_clusters_f.csv')
