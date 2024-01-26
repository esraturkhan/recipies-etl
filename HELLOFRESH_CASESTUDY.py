#!/usr/bin/env python
# coding: utf-8

# # PYTHON PANDAS

# ##### 1) Download the following dataset of Open Recipes.
# 

# In[15]:


# the data set is downloaded to the file named recipies-etl.


# ##### 2) Write a script in Python that reads the recipes and extracts every recipe that has “Chilies” as one of the ingredients. Your code should allow for misspelling of the word for example Chiles as well as the singular form of the word.

# In[16]:


import pandas as pd

# read the .json file named as recipes and then assing it to "df"
df = pd.read_json('recipes.json', lines=True)

# show the dataframe

df.head()



# In[17]:


# Regular expression pattern 
pattern = r'\bchil(?:ies|es|is|e)\b'

# Filter the DataFrame 
recipes_with_chilies = df[df['ingredients'].str.contains(pattern, case=False, regex=True)]

# Display the filtered recipes
print(recipes_with_chilies)



# In[18]:


# You can also see more structered and easy to read way
recipes_with_chilies.head()


# ##### 3) Add an extra field to each of the extracted recipes with the name difficulty. The difficulty field would have a value of "Hard" if the sum of prepTime and cookTime is greater than 1 hour, "Medium" if the total is between 30 minutes and 1 hour, "Easy" if the total is less than 30 minutes, and "Unknown" otherwise.

# In[19]:


# Convert the time format in the data table to numeric values as minutes
for i in ['cookTime', 'prepTime']:
    # Find the hours and convert it to minutes
    hours = recipes_with_chilies[i].str.extract(r'(\d+)H').fillna(0).astype(int) * 60
    # Find minutes
    minutes = recipes_with_chilies[i].str.extract(r'(\d+)M').fillna(0).astype(int)
    # Create new columns for the prepTime and cookTime as a minutes
    recipes_with_chilies[i + '_minutes'] = hours + minutes

# Calculate the totalTime and record in a new column
recipes_with_chilies['totalTime'] = recipes_with_chilies['cookTime_minutes'] + recipes_with_chilies['prepTime_minutes']

print(recipes_with_chilies)

# The question aske me to add only difficulty column as a new column. However, before calculate the difficulty column i add 
#some extra columns above in purpose of preparation. It might be not good since I change the original table more than asked
#However, it makes more readable and easy to understand process step by step.




# Find the difficulty levels using lambda function

recipes_with_chilies['difficulty'] = recipes_with_chilies['totalTime'].apply(
    lambda i: 'Hard' if i > 60 else 
                           'Medium' if 30 < i <= 60 else 
                           'Easy' if i <= 30 else 'Unknown'
)

print(recipes_with_chilies)


# ##### 4) The resulting dataset should be saved as a *.csv file.

# In[20]:


recipes_with_chilies.to_csv('recipes_with_chilies.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:




