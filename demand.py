import pandas as pd
import os
from dfply import *
from scipy.optimize import curve_fit
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


#set working directory
#os.chdir("C:\Users\Eric\Documents\ENSTA\IN104")

#1) import consumption data from DE.csv into a pandas DataFrame and rename Date (CET) column to Date

data = pd.read_csv (r'C:\Users\Eric\Documents\ENSTA\IN104\DE.csv', sep = ";") 

df=pd.DataFrame(data, columns= ['Date (CET)','LDZ','Actual','Normal'])  

    # The LDZ represents gas consumption in GWh, Actual is the Actual temperature and Normal is the normal temperature
    
    # Try to use dfply pipes to rename
    
df=df.rename(columns={'Date (CET)':'Date'})
#print(df.head)

    
    # Plot using Matplotlib all three series on 3 sub plots to see them varying together
    # Do not forget to add a legend and a title to the plot

df.plot(x="Date",y="LDZ")
plt.xlabel("Date")
plt.ylabel("Gas Consumption (GWh)")
plt.title("Gas consumption = f(time)")

df.plot(x="Date",y="Actual",color="blue")
plt.xlabel("Date")
plt.ylabel("Actual temperature")
df.plot(x="Date",y=["Normal","Actual"])
plt.xlabel("Date")
plt.ylabel("Normal temperature")

plt.grid()
plt.show()

#     
#     # Comment on their variation and their relationships

#The normal temperature varies like a sinus function, and the actual one contains way more noise, which looks like it could be filtered. The gas function varies the same way as the temperature, which is key here.
# 
# 
#     
#     # use dfply to transform Date column to DateTime type
# 
#     
# 
# #2) work on consumption data (non-linear regression)
# #2)1. Plot with a scatter plot the consumption as a function of temperature



#2)2. define the consumption function (I give it to you since it is hard to know it without experience)

#This function takes temperature and 4 other curve shape parameters and returns a value of consumption
def h(t, a, b, c, d):
    return(d+a/(1+(b/(t-40))**c))

#These are random initial values of a, b, c, d
guess_values= [798.433, -37.135, 5.6265, 101.1644]

def h_test(t):
    return h(t,guess_values[0],guess_values[1],guess_values[2],guess_values[3])

#2)3. Fill out this h_hat array with values from the function h

# You will take the 'Actual' column from the DE.csv file as being the input temperature so its length should be the number of rows in the DataFrame imported

# For each value of temperature of this column you will calculate the consumption using the h function above
# DO NOT use a for loop, vectorize
# Use the array guess_values for the curve parameters a, b, c, d that is to say a = guess_values[0], b = guess_values[1], c = guess_values[2], d = guess_values[3]

# Plot on a graph the real consumption (LDZ column) as a function of Actual temperature use blue dots
# On this same graph add the h_hat values as a function of Actual temperature use a red line for this
# Do not forget to add a legend and a title to the plot
# Play around with the parameters in guess_values until you feel like your curve is more or less correct

new_df=df.assign(h_hat=df['Actual'])
new_df['h_hat']=new_df['h_hat'].apply(h_test)

new_df.plot(x='Actual',y=['h_hat','LDZ'],style='o')
plt.show()

new_df=new_df.dropna()
t=new_df['Actual'].values
z=new_df['LDZ'].values
c,cov=curve_fit(h,t,z,guess_values)
print(c)


#2)4. optimize the parameters

    # Your goal right now is to find the optimal values of a, b, c, d using SciPy
    # Inspire yourselves from the following video
    # https://www.youtube.com/watch?v=4vryPwLtjIY

#2)5. check the new fit

#Repeat what we did in 2)3. but with the new optimized coefficients a, b, c, d


#calculate goodness of fit parameters: correlation, root mean square error (RMSE), Average normalised RMSE, normalized RMSE
#averaged normalized RMSE is RMSE/(average value of real consumption)
#normalized RMSE is RMSE/(max value of real consumption - min value of real consumption)
#Any other metric we could use ?

# corr, _ = pearsonr(model, real_conso)
# rmse = np.sqrt(mean_squared_error(model,real_conso))
# nrmse = rmse/(np.max(real_conso) - np.min(real_conso))
# anrmse = rmse/np.mean(real_conso)