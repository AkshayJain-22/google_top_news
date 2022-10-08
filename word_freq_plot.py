from word_frequency import frequency_generator
from matplotlib import pyplot as plt
import pandas as pd


def plot_generator(name,titles):
    frequency_df = frequency_generator(titles)
    frequency_df = frequency_df.sort_values(by=['Frequency'],ascending=False)
    frequency_df.plot(x='Words',y='Frequency',kind ='bar',figsize=(8,8))
    plt.xticks(rotation=90,)
    plt.xlabel('xlabel', fontsize=24)
    plots_filename = f'{name}_plot.png'
    plt.savefig(plots_filename)
    return(plots_filename)