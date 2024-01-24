
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# git clone [url to repo] - klonuje repo z linku i dodaje folder na komputerze

# ls - lista plików w folderze
# cd [nazwa folderu] - komenda za pomoca ktorej wchodzi sie do folderu

# git pull origin main

# git commit -m "wiadomosc" - wpierdalasz zmeiany
# git push - no wprowadzam juz zmiany

np.random.seed(42) # ustawiamy seed, by miec stałe obliczenia

# Zdefiniujemy domyslnie rozmairy czcionek słuzące do generowania ładnych rysunków
plt.rc("font", size=12)
plt.rc("axes", labelsize=14, titlesize=14)
plt.rc("legend", fontsize=12)
plt.rc("xtick", labelsize=10)
plt.rc("ytick", labelsize=10)

# Zdefiniujemy ustawienia biblioteki Pandas
pd.set_option("display.max_columns", None) # Wyśiwetlaj wszystkei kolumny w dataframe
#pd.set_option("display.max_rows", None) # Wyśiwetlaj wszystkei wiersze w dataframe
#pd.set_option("display.max_colwidth", None)  # Maksymalizuje szerokośc kolumn w dataframe
#pd.set_option("display.precision", 2) # Zdefiniuj precyzje wyswitlania liczb w dataframe
#pd.reset_option("display.max_columns") # # Resetujesz wcześniejsze ustawienia na domyślne

datapath = Path() / "uczenie maszynowe" / "lifesat" # definiujemy ścieżkę do bierzącego kataloga
# Wczytujemy zbiory
#oecd_bli = pd.read_csv(datapath / "oecd_bli.csv")
#gdp_per_capita = pd.read_csv(datapath / "gdp_per_capita.csv")

gdp_per_capita = pd.read_csv("C:\\Users\\macie\\Desktop\\Studia\\Wprowadzenie do uczenia maszynowego\\classes\\data\\lifesat\\gdp_per_capita.csv")
oecd_bli = pd.read_csv("C:\\Users\\macie\\Desktop\\Studia\\Wprowadzenie do uczenia maszynowego\\classes\\data\\lifesat\\oecd_bli.csv")

gdp_per_capita_2020 = gdp_per_capita[gdp_per_capita["Year"] == 2020]
gdp_per_capita_2020 = gdp_per_capita_2020.rename(
    columns = {"GDP per capita, PPP (constant 2017 international $)": "GDP per capita (USD)"
               }
)

print(oecd_bli["Indicator"].value_counts())

oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]
oecd_bli = oecd_bli.pivot(
    index="Country",
    columns="Indicator",
    values="Value"
)

oecd_bli = oecd_bli.reset_index()

print(oecd_bli.info())
print(gdp_per_capita_2020.info())

full_country_stat = oecd_bli.merge(
    gdp_per_capita_2020,
    left_on = "Country",
    right_on = "Entity",
    how = "inner"
)

print(full_country_stat.info())

full_country_stat = full_country_stat[["Country", "Life satisfaction", "GDP per capita (USD)"]]
full_country_stat = full_country_stat.sort_values(by = "GDP per capita (USD)")

print(full_country_stat)

full_country_stat.to_csv("C:\\Users\\macie\\Desktop\\Studia\\Wprowadzenie do uczenia maszynowego\\classes\\data\\lifesat\\full_country_stat.csv", index = False)

min_gdp = 23_500
max_gdp = 62_500
country_stats = full_country_stat[(full_country_stat["GDP per capita (USD)"] >= min_gdp)
                                   & (full_country_stat["GDP per capita (USD)"] <= max_gdp)]

country_stats.to_csv("C:\\Users\\macie\\Desktop\\Studia\\Wprowadzenie do uczenia maszynowego\\classes\\data\\lifesat\\country_stats.csv", index=False)
