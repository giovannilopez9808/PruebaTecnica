from pandas import read_csv, DataFrame, concat
from numpy import nan


def get_distribution(
    data,
    header,
    dictionary,
):
    results = DataFrame()
    for key in dictionary:
        data_ = data[data[header] == key]
        data_ = data_["Rango_score"]
        results_ = data_.value_counts()
        results_ = 100*results_/results_.sum()
        results_ = DataFrame(results_)
        results = concat([
            results,
            results_
        ],
            axis=1
        )
    keys = [
        key.replace(",", "") for key in dictionary
    ]
    keys = [
        key.replace("$", "") for key in keys
    ]
    results = results.round(3)
    results.columns = keys
    results = results.sort_index()
    print(results)
    return results


def map_values(
    data,
    column,
    dictionary,
):
    return data[column].map(
        lambda values:
        dictionary[values]
    )


filename = "Muestra_Abandono.txt"
data = read_csv(
    filename,
    encoding='latin-1',
    delimiter="\t",
    low_memory=False,
)
scores = {
    "0% a 10%": 0,
    "10.1% a 20%": 1,
    "20.1% a 30%": 2,
    "30.1% a 40%": 3,
    "40.1% a 50%": 4,
    "50.1% a 60%": 5,
    "60.1% a 70%": 6,
    "70.1% a 80%": 7,
    "80.1% a 90%": 8,
    "90.1% a 100%": 9,
}
secures = {
    "Otros": 0,
    "AA": 1,
    "BB": 2
}
secure_type = {
    "Tpre": 0,
    "Pre": 1,
    "TPL": 2,
    "PL": 3,
    "EL": 4,
    "PE": 5,
}

antiquity = {
    "6 o menos": 0,
    "7 a 12": 1,
    "13 a 24": 2,
    "25 a 60": 3,
    "61 a 120": 4,
    "121 o más": 5,
}

disponibility = {
    "Sin dispersión": 0,
    "$0.1 a $99.9": 1,
    "$100 a $4,999.9": 2,
    "$5,000 a $9,999.9": 3,
    "$10,000 a $19,999.9": 4,
    "$20,000 a $39,999.9": 5,
    "$40,000 a $59,999.9": 6,
    "$60,000 o más": 7,
}

udir = {
    "-$1,000.1 a -$500": 0,
    "-$500.1 a $0": 1,
    "Menor igual a -$1,000": 2,
    "Sin Utilidad": 3,
    "$0.1 a $500": 4,
    "$500.1 a $1,000": 5,
    "$1,000.1 a $5,000": 6,
    "$5,000.1 a más": 7,
}

products_num = {
    "0": 0,
    "1": 1,
    "2": 2,
    "Más de 2": 3
}


sdo_capta = {
    "Sin Captación": 0,
    "$0 a $100": 1,
    "$100.01 a $1,000": 2,
    "$1,000.01 a $5,000": 3,
    "$5,000.01 a $10,000": 4,
    "$10,000.01 a $50,000": 5,
    "$50,000.01 o más": 6,
}
data["udir_anual"] = data["udir_anual"].map(
    lambda value:
    nan if value == "#¡VALOR!" else value

)
data = data.dropna()
data["udir_anual"] = data["udir_anual"].astype(float)
results = get_distribution(
    data,
    "seg",
    secures
)
results.to_csv(
    "seg_distribution.csv"
)
results = get_distribution(
    data,
    "Rango_disp_prom",
    disponibility
)
results.to_csv(
    "disp_distribution.csv"
)
results = get_distribution(
    data,
    "Rango_Num_Productos",
    products_num
)
results.to_csv(
    "products_num_distribution.csv"
)
results = get_distribution(
    data,
    "Rango_Ant",
    antiquity
)
results.to_csv(
    "Rango_Ant_distribution.csv"
)
