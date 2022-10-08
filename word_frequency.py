from tkinter.font import names
import pandas as pd

def frequency_generator(titles):
    
    all_titles = ' '.join(titles)

    # break the string into list of words
    words_list = all_titles.split()
 
    # gives set of unique words
    unique_words = set(words_list)
    frequency_df = pd.DataFrame(columns=['Word','Frequency'])
    ctr=0
    for word in unique_words :
        frequency_df['Word'].iloc[ctr] = word
        frequency_df['Frequency'].iloc[ctr] = words_list.count(word)
        ctr+=1

    return(frequency_df)