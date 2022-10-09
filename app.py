from flask import Flask, render_template 
import pandas as pd
from result_collector import final_results
from give_me_q import q_generator
from word_cloud_maker import word_cloud
from word_freq_plot import plot_generator
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def homepage():
    results = final_results()
    inner_dic = {}
    titles=[]
    barplots_filenames=[]
    wordcloud_filenames=[]
    name_list=q_generator()
    df = pd.DataFrame(columns=['Name','Title','Source','Pub_time'])
    for result in results:
        for i in range(len(result['titles'])):
            inner_dic['Name'] = result['Name']
            inner_dic['Title'] = result['titles'][i]
            inner_dic['Source'] = result['sources'][i]
            inner_dic['Pub_time'] = result['pub_times'][i]
            df=df.append(inner_dic,ignore_index=True)
    for name in name_list:
        titles = []
        titles.append(df['Title'][df['Name']==name])
        wordcloud_filenames.append(word_cloud(name,titles))
        barplots_filenames.append(plot_generator(name,titles))
    headings = ('Title','Source','Pub_time')
    return render_template("results.html", table_headings = headings, player_names=df['Name'], data=df.drop(columns=['Name']),len_df = len(df), wordcloud_files = wordcloud_filenames, plot_files = barplots_filenames)

if __name__=="__main__":
    app.run(debug=True)