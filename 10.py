import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pylab as pl
# from numpy import mean
from collections import defaultdict

df = pd.read_csv("housePrice2.csv")
ddf = df

# print(ddf)

# pl.scatter(ddf.Area,ddf.Price,color='blue')
# pl.xlabel("Area")
# pl.ylabel("Price")
# pl.show()

ddf["Address"].replace('Abazar','Abuzar',inplace=True)
ddf["Address"].replace('Firoozkooh Kuhsar','Firoozkooh',inplace=True)
ddf["Address"].replace('Islamshahr Elahieh','Islamshahr',inplace=True)
ddf["Address"].replace('Mehrabad River River','Mehrabad',inplace=True)
ddf["Address"].replace('Shahrake Quds','Shahrake Qods',inplace=True)

ddf['pricePerArea'] = ddf['Price']/ddf['Area']

ddf['RoomParkingElevator'] = ddf['Room'] + ddf['Parking'] + ddf['Elevator']

ddf.sort_values('pricePerArea',inplace=True,ascending=False)

temp = defaultdict(lambda: len(temp))
ddf['AddressId'] = [temp[ele] for ele in ddf['Address']]

pl.scatter(ddf.RoomParkingElevator,ddf.pricePerArea,color='blue')
pl.xlabel("RoomParkingElevator")
pl.ylabel("pricePerArea")
pl.show()

