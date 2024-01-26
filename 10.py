import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pylab as pl
# from numpy import mean

df = pd.read_csv("housePrice.csv")
ddf = df

def handle_non_numerical_data(df):
    columns = df.columns.values
    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1

            df[column] = list(map(convert_to_int, df[column]))

    return df

# print(ddf)

# pl.scatter(ddf.Area,ddf.Price,color='blue')
# pl.xlabel("Area")
# pl.ylabel("Price")
# pl.show()

# cddf = handle_non_numerical_data(df)

# print(df["Address"].drop_duplicates().sort_values().to_markdown())

ddf["Address"].replace('Abazar','Abuzar',inplace=True)
ddf["Address"].replace('Firoozkooh Kuhsar','Firoozkooh',inplace=True)
ddf["Address"].replace('Islamshahr Elahieh','Islamshahr',inplace=True)
ddf["Address"].replace('Mehrabad River River','Mehrabad',inplace=True)
ddf["Address"].replace('Shahrake Quds','Shahrake Qods',inplace=True)

print(ddf["Address"].drop_duplicates().sort_values().to_markdown())
print(len(ddf["Address"].drop_duplicates()))

ddf.add()

ddf.groupby("Address").agg(lambda x:np.mean(x))