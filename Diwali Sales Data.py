#!/usr/bin/env python
# coding: utf-8

# In[30]:


df.head()


# In[31]:


df.info()


# In[37]:


#drop unrelated/blank columns
df.drop(['status','unnamed1'], axis=1, inplace=True)


# In[38]:


pd.isnull(df)


# In[36]:


#check for null values
pd.isnull(df).sum()


# In[17]:


df.shape


# In[18]:


#drop null values
df.dropna(inplace=True)


# In[19]:


df.shape


# In[20]:


#initialize List of Lists
data_test = [['madhav',11], ['Gopi',15],['Keshav',],['Lalita',16]]

#Create the pandas DataFrame using List
df_test = pd.DataFrame(data_test,columns=['Name','Age'])
df_test


# In[23]:


df_test.dropna()


# In[22]:


df_test


# In[24]:


df.shape


# In[27]:


#drop null values
df.dropna(inplace=True)


# both are same thing
# df_test.dropna(inplace=True)
# df_test = df_test.dropna()

# In[28]:


# change data type
df['Amount'] = df['Amount'].astype('int')


# In[29]:


df['Amount'].dtypes


# In[30]:


df.columns


# In[71]:


#rename column
df.rename(columns= {'Marital_Status':'jeewansathi'})


# In[20]:


# describe() method returns description of the data in the DataFrame (i.e count, mean, std, etc)
df.describe()


# In[12]:


# use describe() for specific columns


# # Exploratory Data Analysis
# 
# 
# Gender

# In[21]:


ax = sns.countplot(x = 'Gender',data =df)


# In[22]:


ax = sns.countplot(x = 'Gender',data =df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[23]:


sales_gen =df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# In[40]:


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[24]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x ='Gender',y= 'Amount' ,data = sales_gen)


# from above graphs we can see that most of the buyer are females and even the purchasing power of females are greater than men
# 
# 
# Age

# In[48]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[25]:


df.columns


# In[26]:


sns.countplot(data = df, x = 'Age Group', hue = 'Gender')


# In[27]:


df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[28]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# From above graphs we can see that most of the buyer are of age group between 26-35 yrs female.

# # State

# In[39]:


# total number of orders from top 15 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(15)


sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[30]:


df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)


# In[38]:


# total number of Amount/sales from top 15 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(15)


sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# In[40]:


df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(15)


# From above graphs we can see that most of the order& total sales/amount are from uttar pradehs,maharashtra and karnataka resoectively

# # Marital Status

# In[45]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[46]:


sales_state = df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# From above graphs we can see that most of the buyers are merried (woman) and they have high purchasing power.

# # Occupation

# In[50]:


sns.set(rc={'figure.figsize':(15,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[51]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Aviation and Healthcare sector.

# In[52]:


df.columns


# # Product Category

# In[61]:


sns.set(rc={'figure.figsize':(25,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[60]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From above graphs we can see that most of the sold products are from Food & Clothing and Electronics category.

# # Product_ID

# In[69]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[70]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:
#     
#     
#     Married woman age group 26-35 yrs from UP, Maharashtra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food Clothing and Electronics category.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




