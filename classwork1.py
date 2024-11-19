import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# MY FILE NAME IS nepse_last_90_days.csv SO I USE IT.
# YOU CAN CHANGE THAT NAME TO MATCH YOUR FILES TO SEE THE RESULT.


# TO SHOW ALL DATA
data=pd.read_csv("nepse_last_90_days.csv")
df=pd.DataFrame()
xpoints=np.array(data["Date"])
ypoints=np.array(data["NEPSE Index"])

plt.plot(xpoints, ypoints, "o")
plt.plot(xpoints, ypoints, linestyle="dotted")
plt.show()



# TO SHOW THE LAST SEVEN(7) DATA
df=pd.read_csv("nepse_last_90_days.csv")
data3=df.tail(7)
xpoints=np.array(data3["Date"])
ypoints=np.array(data3["NEPSE Index"])
plt.plot(xpoints, ypoints, "o")
plt.plot(xpoints, ypoints, linestyle="dotted")
plt.show()



# TO SHOW DATA ABOVE 2490
df=pd.read_csv("nepse_last_90_days.csv")
ninetydays=df.tail(90)
selected_df=ninetydays[ninetydays["NEPSE Index"]>2490]
xpoints=np.array(selected_df["Date"])
ypoints=np.array(selected_df["NEPSE Index"])
plt.plot(xpoints, ypoints, "o")
plt.plot(xpoints, ypoints, linestyle="dotted")
plt.show()


# TO FIND THE AVERAGE VALUE
ninetydays=df.tail(90)
average=ninetydays["NEPSE Index"].mean()
print(average)



# TO SHOW THE MAXIMUM VALUE
ninetydays=df.tail(90)
maximum=ninetydays["NEPSE Index"].max()
print(maximum)