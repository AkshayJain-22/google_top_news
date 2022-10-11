import re
import pandas as pd

stopwords=["i", "br", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def frequency_generator(titles):
    all_titles = ''
    for title in titles:
        title = str(title)
        all_titles += title
        all_titles +=' '
    
    all_titles = all_titles.lower()
    all_titles = re.sub('[%s]' % re.escape('@!"#$%&\'()+,-./:;<=>?@[\\]^_`{|}~'), '', all_titles)
    
    words_list = [word for word in all_titles.split() if not word in stopwords]
    print(words_list)
    # gives set of unique words
    unique_words = set(words_list)
    frequency_df = pd.DataFrame(columns=['Words','Frequency'],index=range(500))
    ctr=0
    for word in unique_words :
        frequency_df.loc[ctr].Words = word
        frequency_df.loc[ctr].Frequency = words_list.count(word)
        ctr+=1
    return(frequency_df)