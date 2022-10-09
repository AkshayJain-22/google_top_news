from word_frequency import frequency_generator
from matplotlib import pyplot as plt
import pandas as pd


def plot_generator(name,titles):
    frequency_df = frequency_generator(titles)
    frequency_df = frequency_df.sort_values(by=['Frequency'],ascending=False)
    frequency_df.iloc[0:20].plot(x='Words',y='Frequency',kind ='bar',figsize=(3,3))
    plt.xticks(rotation=90,)
    plt.xlabel('xlabel', fontsize=12)
    plots_filename = f'static/images/{name}_plot.png'.replace(' ','_')
    plt.savefig(plots_filename)
    return(plots_filename)