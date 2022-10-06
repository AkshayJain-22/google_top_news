from wordcloud import WordCloud
import matplotlib.pyplot as plt

stopword=["i", "br", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def word_cloud(name,titles):
    comment_words = ''
    stopwords = stopword

    for val in titles: # iterate through the titles

        val = str(val) # typecaste each val to string
        tokens = val.split() # split the value
        
        for i in range(len(tokens)): # Converts each token into lowercase
            tokens[i] = tokens[i].lower()

        comment_words += " ".join(tokens)+" "

    wordcloud = WordCloud(width = 350, height = 350,
                    background_color = 'white',
                    stopwords = stopwords,
                    min_font_size = 10).generate(comment_words)

    filename = f'static/images/{name}.png'.replace(' ','_')
    wordcloud.to_file(filename)
    return(filename)