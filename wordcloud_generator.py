# Lets build a wordcloud from a CSV file (other formats can be used)
# Word Clouds (WC) are a nice way to visualize word frecuencies
# I like to wave some "print" checkpoints so if I Find a TRACEBACK i can know where exactly to look for 
# Feel free to edit to your taste
# E.



# First well start by importing some required libraries

import pandas as pd
!pip install wordcloud
from wordcloud import WordCloud

print("libraries loaded ... ... ...")
      
# next well create a data frame to work (since well be importing a CSV file )

df = pd.read_csv("YOUR FILE PATH AND FILE NAME.csv")

# -----  OPTIONAL ------
#  Its important to know if this step is correct, so well checkit out by printing the head
df.head()


# Lets Prepare a clean the data, first well change all the letters to lower
df_string = df.to_string().lower()

# -----  OPTIONAL ------
# Some specific words to erase, other option would be to use a STOPWORDS list
df_string = df_string.replace("UNWANTED_WORD", "")


# In this case my file had the cells with more than one word per cell so
# well like to split them to be unique words per item in the list 

words0 = df_string.split()

# Remove numbers
words0 = [word for word in words0 if not any(c.isnumeric() for c in word)]


# -----  OPTIONAL ------
# CHECKPOINT : lets print the first 10 items of our list to see that everithing is OK 
print("This is the cleaned data list: ")
print(words0[:10])


# Building a Dictionary to calculate frecuencies :
name_counts = {}


for name in words0 :
     if name not in name_counts:
        name_counts[name] = 1
     else:
        name_counts[name] += 1
        

# Finally ! Well Build the Word Cloud
# IMPORTANT: WC parameters can be customizables to taste!

stopwords = []
wordcloud = WordCloud(background_color='white', max_words=100, stopwords=stopwords,
                      width=800, height=400)
wordcloud.generate_from_frequencies(name_counts)
wordcloud.to_image()

# Lets turn our result to a JPG file
wordcloud.to_file('wordcloud.jpg')
print("Your Word Cloud was generated succesfully")
