from word_frequency import frequency_generator
from matplotlib import pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")


def plot_generator(name,titles):
    frequency_df = frequency_generator(titles)
    frequency_df = frequency_df.sort_values(by=['Frequency'],ascending=False)
    frequency_df.iloc[0:20].plot(x='Words',y='Frequency',kind ='bar',figsize=(5,5))
    plt.xticks(rotation=90,)
    plt.xlabel('xlabel', fontsize=1)
    plots_filename = f'static/images/{name}_plot.png'.replace(' ','_')
    plt.savefig(plots_filename,dpi=100, bbox_inches='tight')
    return(plots_filename)