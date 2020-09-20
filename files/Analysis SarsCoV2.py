#!/usr/bin/env python
# coding: utf-8

# # SARS-CoV-2 virus spread analysis using Python
# ----------------------

# ## Dataset Resources
# 
# - [Novel Coronavirus (COVID-19) Cases Data](https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases) compiled by the Johns Hopkins University Center for Systems Science and Engineering ([JHU CCSE](https://data.humdata.org/organization/jhucsse))
#   - time_series_covid19_confirmed_global.csv
#   - time_series_covid19_deaths_global.csv
#   - time_series_covid19_recovered_global.csv
# 
# 
# - [GDP (Gross Domestic Product) per capita](https://ourworldindata.org/grapher/gdp-per-capita-worldbank) published by World Bank – World Development Indicators
#   - gdp-per-capita-worldbank.csv

# ## Modules
# 
# - [pandas](https://pandas.pydata.org/) (data analysis and manipulation)
# 
# - [numpy](https://numpy.org/) (scientific computing)
# 
# - [seaborn](https://seaborn.pydata.org/) (statistical data visualization)
# 
# - [matplotlib](https://matplotlib.org/) (visualizations)

# ## Note
# - The latest datasets can be used (from the sources I mentioned above), as long as the files' structure hasn't been changed.
# - Adjust the values in `.sort_values` method to the latest date in the datasets.
# - Change the `name_country` in `.loc[country_name]` method to see the data of what country you want.
# - `.head(1000)` lists all the rows in dataset. Change `1000` to the number of rows you want to list. `.head()` will list 5 rows by default.
# - Use `dataset_name.shape` to see the number of rows and columns of the dataset.

# ## Table of content
# - [Import modules](#Import-modules)
# - **[Dataset: Confirmed cases](#Dataset:-Confirmed-cases)**
#   - [Import file](#Dataset:-Confirmed-cases)
#   - [Confirmed cases in specific countries](#Confirmed-cases-in-specific-countries)
#   - [Countries with the highest confirmed cases](#Countries-with-the-highest-confirmed-cases)
#   - [Countries with the lowest confirmed cases](#Countries-with-the-lowest-confirmed-cases)
#   - [Look at the data in some specific countries about confirmed cases](#Look-at-the-data-in-some-specific-countries-about-confirmed-cases)
#   - [Calculate the max_infection_rate of all countries and add to dataset_cases](#Calculate-the-max_infection_rate-of-all-countries-and-add-to-dataset_cases)
# - **[Dataset: Deaths by COVID-19](#Dataset:-Deaths-by-COVID-19)**
#   - [Import file](#Dataset:-Deaths-by-COVID-19)
#   - [Deaths by COVID-19 in specific countries](#Deaths-by-COVID-19-in-specific-countries)
#   - [Countries with the highest deaths by COVID-19](#Countries-with-the-highest-deaths-by-COVID-19)
#   - [Look at data in some specific countries about deaths by COVID-19](#Look-at-data-in-some-specific-countries-about-deaths-by-COVID-19)
#   - [Calculate the max_death_rate of all countries and add to dataset_deaths](#Calculate-the-max_death_rate-of-all-countries-and-add-to-dataset_deaths)
# - **[Dataset: Recovered](#Dataset:-Recovered)**
#   - [Import file](#Dataset:-Recovered)
#   - [Recovered in specific countries](#Recovered-in-specific-countries)
#   - [Countries with the highest recovered](#Countries-with-the-highest-recovered)
#   - [Look at data in some specific countries about recovered](#Look-at-data-in-some-specific-countries-about-recovered)
#   - [Calculate the max_recovery_rate of all countries and add to dataset_recovered](#Calculate-the-max_recovery_rate-of-all-countries-and-add-to-dataset_recovered)
# - **[Dataset: GDP per capita](#Dataset:-GDP-per-capita)**
#   - [Import file](#Dataset:-GDP-per-capita)
# - **[Join all dataset into one](#Join-all-dataset-into-one)**
# - **[Correlation Matrix](#Correlation-Matrix)**
# - **[Visualization from data](#Visualization-from-data)**
#   - [Recovery Rate](#Recovery-Rate)
#   - [Graph: max_infection_rate and max_death_rate](#Graph:-max_infection_rate-and-max_death_rate)
#   - [Graph: max_infection_rate and max_recovery_rate](#Graph:-max_infection_rate-and-max_recovery_rate)
#   - [Graph: gdp_per_capita and max_infection_rate](#Graph:-gdp_per_capita-and-max_infection_rate)
#   - [Graph: gdp_per_capita and max_recovery_rate](#Graph:-gdp_per_capita-and-max_recovery_rate)

# ## Import modules

# In[1]:


get_ipython().system('pip3 install seaborn')
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('All modules are imported successfully!')


# ## Dataset: Confirmed cases
# 
# ### Import file
# 
# Import `time_series_covid19_confirmed_global.csv`

# In[2]:


# Importing data
dataset_cases = pd.read_csv("time_series_covid19_confirmed_global.csv")

# Filter
# dataset = dataset[dataset.date.eq("2020-09-18")]

# Delete useless column
dataset_cases.drop(["Lat", "Long", "Province/State"],axis=1, inplace=True)

# Set index
# dataset.set_index("Country/Region", inplace=True)
dataset_cases = dataset_cases.groupby("Country/Region").sum()

dataset_cases.head(1000)


# In[3]:


# This dataset_cases_filtered will be used later
dataset_cases_filtered = pd.DataFrame(dataset_cases["9/18/20"])
# Rename
dataset_cases_filtered = dataset_cases_filtered.rename(columns={'9/18/20': 'confirmed_cases'})


# ### Confirmed cases in specific countries

# In[4]:


dataset_cases.loc["Vietnam"].plot(figsize=(14, 6), legend = True, title = 'Confirmed cases in Vietnam, Singapore, Japan and China')
dataset_cases.loc["Singapore"].plot()
dataset_cases.loc["Japan"].plot()
dataset_cases.loc["China"].plot()
# Identify which line belong to which country
plt.legend()


# *Confirmed cases in Vietnam, Singapore, Japan and China*

# ### Countries with the highest confirmed cases

# Sort the `dataset_cases` descending by the value in the newest column.

# In[5]:


# Sort the dataset descending
dataset_cases = dataset_cases.sort_values(by=['9/18/20'], ascending=False)
dataset_cases.head(1000)


# In[6]:


# Cast the index of dataframe (name of countries) into list
countries = list(dataset_cases.index)

# List 10 countries with the highest confirmed cases
count = 0
for country in countries:
    dataset_cases.loc[country].plot(figsize=(14, 6), legend = True, title = 'Countries with the highest confirmed cases')
    count += 1
    if count == 10:
        break

plt.legend()


# *Countries with the highest confirmed cases*

# ### Countries with the lowest confirmed cases

# In[7]:


# Sort the dataset ascending
dataset_cases = dataset_cases.sort_values(by=['9/18/20'])
dataset_cases.head(1000)


# In[8]:


# Cast the index of dataframe (name of countries) into list
countries = list(dataset_cases.index)

# List 10 countries with the lowest confirmed cases
count = 0
for country in countries:
    dataset_cases.loc[country].plot(figsize=(14, 6), legend = True, title = 'Countries with the lowest confirmed cases')
    count += 1
    if count == 10:
        break

plt.legend()


# *Countries with the lowest confirmed cases*

# ### Look at the data in some specific countries about confirmed cases
# Calculate the first derivative to see the spread rate

# #### Infection rate in Vietnam

# In[9]:


# Calculate the first derivative of the curve
dataset_cases.loc["Vietnam"].diff().plot(figsize=(14, 6), legend = True, title = 'Infection rate in Vietnam')


# In[10]:


# Find the max_infection_rate for Vietnam
dataset_cases.loc["Vietnam"].diff().max()


# The `max_infection_rate` in Vietnam is **50.0**

# #### Compare the Infection rate in some countries: Vietnam, United State, Italy, Japan and China

# In[11]:


# Calculate the first derivative of the curve

dataset_cases.loc["US"].diff().plot(figsize=(14, 6), legend = True, color = 'orange', title = 'Compare the Infection rate in some countries: Vietnam, United State, Italy, Japan and China')
dataset_cases.loc["Italy"].diff().plot(legend = True, color = 'purple')
dataset_cases.loc["China"].diff().plot(legend = True, color = 'brown')
dataset_cases.loc["Japan"].diff().plot(legend = True, color = 'green')
dataset_cases.loc["Vietnam"].diff().plot(legend = True)


# In[12]:


# Find the max_infection_rate for US
dataset_cases.loc["US"].diff().max()


# The `max_infection_rate` in US is **77255.0**

# ### Calculate the `max_infection_rate` of all countries and add to `dataset_cases`

# In[13]:


# Cast the index of dataframe (name of countries) into list
countries = list(dataset_cases.index)

#Calculate max_infection_rate of all countries
max_infection_rate = []
for country in countries:
    max_infection_rate.append(dataset_cases.loc[country].diff().max())

#Add new column
dataset_cases["max_infection_rate"] = max_infection_rate

dataset_cases.head(1000)


# In[14]:


# Keep needed column
dataset_cases = pd.DataFrame(dataset_cases["max_infection_rate"])

dataset_cases.head(1000)


# ## Dataset: Deaths by COVID-19
# 
# ### Import file
# 
# Import `time_series_covid19_deaths_global.csv`

# In[15]:


# Importing data
dataset_deaths = pd.read_csv("time_series_covid19_deaths_global.csv")

# Delete useless column
dataset_deaths.drop(["Lat", "Long", "Province/State"],axis=1, inplace=True)

# Set index
# dataset.set_index("Country/Region", inplace=True)
dataset_deaths = dataset_deaths.groupby("Country/Region").sum()

dataset_deaths.head(1000)


# Sort the `dataset_deaths` descending by the value in the newest column.

# In[16]:


dataset_deaths = dataset_deaths.sort_values(by=['9/18/20'], ascending=False)
dataset_deaths.head(1000)


# ### Deaths by COVID-19 in specific countries

# In[17]:


dataset_deaths.loc["Vietnam"].plot(figsize=(14, 6), legend = True, title = 'Deaths by COVID-19 in Vietnam, Singapore, Japan and China')
dataset_deaths.loc["Singapore"].plot()
dataset_deaths.loc["Japan"].plot()
dataset_deaths.loc["China"].plot()
# Identify which line belong to which country
plt.legend()


# *Deaths by COVID-19 in Vietnam, Singapore, Japan and China*

# ### Countries with the highest deaths by COVID-19

# In[18]:


# Cast the index of dataframe (name of countries) into list
countries = list(dataset_deaths.index)

# List 10 countries with the highest deaths by COVID-19
count = 0
for country in countries:
    dataset_deaths.loc[country].plot(figsize=(14, 6), legend = True, title = 'Countries with the highest deaths by COVID-19')
    count += 1
    if count == 10:
        break

plt.legend()


# *Countries with the highest deaths by COVID-19*

# ### Look at data in some specific countries about deaths by COVID-19

# #### Death by COVID-19 rate in Vietnam

# In[19]:


# Calculate the first derivative of the curve
dataset_deaths.loc["Vietnam"].diff().plot(figsize=(14, 6), legend = True, title = 'Death by COVID-19 rate in Vietnam')


# In[20]:


dataset_deaths.loc["Vietnam"].diff().max()


# The `max_death_rate` in Vietnam is **3.0**

# #### Compare the deaths rate in some countries: Vietnam, United State, Italy, Japan and China

# In[21]:


# Calculate the first derivative of the curve
dataset_deaths.loc["US"].diff().plot(figsize=(14, 6), legend = True, color = 'orange', title = 'Compare the deaths rate in some countries: Vietnam, United State, Italy, Japan and China')
dataset_deaths.loc["Italy"].diff().plot(legend = True, color = 'purple')
dataset_deaths.loc["China"].diff().plot(legend = True, color = 'brown')
dataset_deaths.loc["Japan"].diff().plot(legend = True, color = 'green')
dataset_deaths.loc["Vietnam"].diff().plot(legend = True)


# In[22]:


dataset_deaths.loc["US"].diff().max()


# The `max_death_rate` in US is **2609.0**

# ### Calculate the `max_death_rate` of all countries and add to `dataset_deaths`

# In[23]:


# Cast the index of dataframe (name of countries) into list
countries = list(dataset_deaths.index)

# Calculate the max_death_rate of all countries
max_death_rate = []
for country in countries:
    max_death_rate.append(dataset_deaths.loc[country].diff().max())

#Add new column
dataset_deaths["max_death_rate"] = max_death_rate

dataset_deaths.head(1000)


# In[24]:


# Keep needed column
dataset_deaths = pd.DataFrame(dataset_deaths["max_death_rate"])

dataset_deaths.head(1000)


# ## Dataset: Recovered
# 
# ### Import file
# 
# Import `time_series_covid19_recovered_global.csv`

# In[25]:


# Importing data
dataset_recovered = pd.read_csv("time_series_covid19_recovered_global.csv")

# Delete useless column
dataset_recovered.drop(["Lat", "Long", "Province/State"],axis=1, inplace=True)

# Set index
# dataset.set_index("Country/Region", inplace=True)
dataset_recovered = dataset_recovered.groupby("Country/Region").sum()

dataset_recovered.head(1000)


# In[26]:


# This dataset_recovered_filtered will be used with dataset_cases_filtered we created in Confirmed Cases Import file
dataset_recovered_filtered = pd.DataFrame(dataset_recovered["9/18/20"])
# Rename
dataset_recovered_filtered = dataset_recovered_filtered.rename(columns={'9/18/20': 'recovered'})


# Sort the `dataset_recovered` descending by the value in the newest column.

# In[27]:


dataset_recovered = dataset_recovered.sort_values(by=['9/18/20'], ascending=False)
dataset_recovered.head(1000)


# ### Recovered in specific countries

# In[28]:


dataset_recovered.loc["Vietnam"].plot(figsize=(14, 6), legend = True, title = 'Recovered in Vietnam, Singapore, Japan and China')
dataset_recovered.loc["Singapore"].plot()
dataset_recovered.loc["Japan"].plot()
dataset_recovered.loc["China"].plot()
# Identify which line belong to which country
plt.legend()


# *Recovered in Vietnam, Singapore, Japan and China*

# ### Countries with the highest recovered

# In[29]:


# Cast the index of dataframe (name of countries) into list
countries = list(dataset_recovered.index)

# List 10 countries with the highest recovered
count = 0
for country in countries:
    dataset_recovered.loc[country].plot(figsize=(14, 6), legend = True, title = 'Countries with the highest recovered')
    count += 1
    if count == 10:
        break

plt.legend()


# *Countries with the highest recovered*

# ### Look at data in some specific countries about recovered

# #### Recovery rate in Vietnam

# In[30]:


# Calculate the first derivative of the curve
dataset_recovered.loc["Vietnam"].diff().plot(figsize=(14, 6), legend = True, title = 'Recovered rate in Vietnam')


# In[31]:


dataset_recovered.loc["Vietnam"].diff().max()


# The `max_recovery_rate` in Vietnam is **59.0**

# #### Recovery rate in United State

# In[32]:


# Calculate the first derivative of the curve
dataset_recovered.loc["US"].diff().plot(figsize=(14, 6), legend = True, color = 'orange', title = 'Recovery rate in United State')


# In[33]:


dataset_recovered.loc["US"].diff().max()


# The `max_recovery_rate` in US is **103921.0**

# ### Calculate the `max_recovery_rate` of all countries and add to `dataset_recovered`

# In[34]:


# Cast the index of dataframe (name of countries) into list
countries = list(dataset_recovered.index)

# Calculate the max_recovery_rate
max_recovery_rate = []
for country in countries:
    max_recovery_rate.append(dataset_recovered.loc[country].diff().max())

#Add new column
dataset_recovered["max_recovery_rate"] = max_recovery_rate

dataset_recovered.head(1000)


# In[35]:


# Keep needed column
dataset_recovered = pd.DataFrame(dataset_recovered["max_recovery_rate"])

dataset_recovered.head(1000)


# ## Dataset: GDP per capita
# 
# ### Import file
# 
# Import `gdp-per-capita-worldbank.csv`

# In[36]:


# Importing data
dataset_country = pd.read_csv("gdp-per-capita-worldbank.csv")

# Filter
dataset_country = dataset_country[dataset_country.Year.eq(2017)]

# Delete useless column
dataset_country.drop(["Code", "Year"],axis=1, inplace=True)

# Rename
dataset_country = dataset_country.rename(columns={'GDP per capita, PPP (constant 2011 international $)': 'gdp_per_capita'})

# Set index
dataset_country.set_index("Entity", inplace=True)

dataset_country.head(1000)


# ## Join all dataset into one

# In[37]:


data = dataset_cases
data = data.join(dataset_deaths, how="inner")
data = data.join(dataset_recovered, how="inner")
data.head(1000)


# In[38]:


data = data.join(dataset_country, how="inner")
data.head(1000)


# In[39]:


# Remove the rows don't have data
data = data[data.gdp_per_capita.notnull()]
data = data[data.gdp_per_capita != 0]
data.head(1000)


# ## Correlation Matrix
# 
# Correlation coefficients between `max_infection_rate`, `max_death_rate`, `max_recovery_rate` and `gdp_per_capita`

# In[40]:


# Correlation Matrix
data.corr()


# # Visualization from data
# ________________________

# ### Recovery Rate

# Join the `dataset_cases_filtered` and `dataset_recovered_filtered` into `data_filtered`

# In[41]:


# Join the dataset_cases_filtered and dataset_recovered_filtered into data_filtered
data_filtered = dataset_cases_filtered
data_filtered = data_filtered.join(dataset_recovered_filtered, how="inner")
data_filtered.head(1000)


# Calculate the `recovery_rate` column by dividing the `recovered` by the `confirmed_cases`

# In[42]:


temp_data_filtered = data_filtered.sort_values(by=['confirmed_cases'], ascending=False)
temp_data_filtered["confirmed_cases"].plot(kind = 'bar', figsize=(42, 6), legend = True, title = 'Confirmed cases of all countries')


# *Confirmed cases of all countries*

# In[43]:


# Calculate the recovery_rate column by dividing the recovered by the confirmed_cases
# recovery_rate <= 1
data_filtered["recovery_rate"] = data_filtered["recovered"] / data_filtered["confirmed_cases"]

# Sort the data_filtered by the value of recovery_rate
data_filtered = data_filtered.sort_values(by=['recovery_rate'], ascending=False)

data_filtered.head(1000)


# In[44]:


data_filtered["recovery_rate"].plot(kind = 'bar', figsize=(42, 6), legend = True, title = 'Recovery rate of all countries')


# *Recovery rate of all countries*

# ### Graph: `max_infection_rate` and `max_death_rate`

# In[45]:


x = data["max_infection_rate"]
y = data["max_death_rate"]
# sns.scatterplot(x,y)
# np.log(y) make the graph easier to read, larger scale
sns.scatterplot(x, y)


# In[46]:


sns.regplot(x, y)


# ### Graph: `max_infection_rate` and `max_recovery_rate`

# In[47]:


x = data["max_infection_rate"]
y = data["max_recovery_rate"]
# sns.scatterplot(x,y)
# np.log(y) make the graph easier to read, larger scale
sns.scatterplot(x, y)


# In[48]:


sns.regplot(x, y)


# ### Graph: `gdp_per_capita` and `max_infection_rate`

# In[49]:


x = data["gdp_per_capita"]
y = data["max_infection_rate"]
# sns.scatterplot(x,y)
# np.log(y) make the graph easier to read, larger scale
sns.scatterplot(x, np.log(y))


# In[50]:


sns.regplot(x, np.log(y))


# > ##### The result shows that people who are living developed country (higher GDP per capita) are more prone to get infection of SarsCoV2 virus

# ### Graph: `gdp_per_capita` and `max_recovery_rate`

# In[51]:


x = data["gdp_per_capita"]
y = data["max_recovery_rate"]
# sns.scatterplot(x,y)
# np.log(y) make the graph easier to read, larger scale
sns.scatterplot(x, y)


# In[52]:


sns.regplot(x, y)


# > ##### The result shows that the maximum recovery rate of a country is not affected by its GDP per capita (its development). The recovery rate in developed countries is not higher than in developing countries.
