from flask import Flask, render_template, request
import pandas as pd
from result_collector import final_results
from give_me_q import q_generator
from word_cloud_maker import word_cloud
from word_freq_plot import plot_generator
app=Flask(__name__)

results = []
inner_dic = {}
titles=[]
barplots_filenames=[]
wordcloud_filenames=[]
name_list=[]
headings = ()
df = pd.DataFrame()

@app.route("/",methods=['GET','POST'])
def homepage():
    pd.set_option('display.max_colwidth', None)
    global results
    global inner_dic
    global titles
    global barplots_filenames
    global wordcloud_filenames
    global name_list
    global headings
    global df

    headings = ('Title','Source','Pub_time')
    

    try:
        player_name = request.form['player']
    except:
        name_list=q_generator()
    else:
        name_list = [player_name]
    finally:
        results = final_results(name_list)
        df = pd.DataFrame(columns=['Name','Title','Source','Pub_time'])
        for result in results:
            for i in range(len(result['titles'])):
                inner_dic['Name'] = result['Name']
                inner_dic['Title'] = result['titles'][i]
                inner_dic['Source'] = result['sources'][i]
                inner_dic['Pub_time'] = result['pub_times'][i]
                df=df.append(inner_dic,ignore_index=True)
        barplots_filenames=[]
        wordcloud_filenames=[]
        for name in name_list:
            titles = []
            titles.append(df['Title'][df['Name']==name])
            wordcloud_filenames.append(word_cloud(name,titles))
            barplots_filenames.append(plot_generator(name,titles))
            print(titles)
    try:
        return render_template("results.html",name_list = q_generator(), table_headings = headings, player_names=df['Name'], data=df.drop(columns=['Name']),len_df = len(df), wordcloud_files = wordcloud_filenames, plot_files = barplots_filenames, player_name = player_name)

    except:
        return render_template("results.html",name_list = q_generator(), table_headings = headings, player_names=df['Name'], data=df.drop(columns=['Name']),len_df = len(df), wordcloud_files = wordcloud_filenames, plot_files = barplots_filenames)
        
@app.route("/filter",methods=['GET','POST'])
def filter():
    player_name = request.form['player']
    global df
    filter_df = df[df['Name']==player_name]
    global wordcloud_filenames
    global barplots_filenames
    filter_wordclouds=[]
    filter_barplots = []
    for i in range(len(wordcloud_filenames)):
        if (player_name.replace(' ','_') in wordcloud_filenames[i]):
            filter_wordclouds.append(wordcloud_filenames[i])
            filter_barplots.append(barplots_filenames[i])

    return render_template("results.html",name_list = name_list, table_headings = headings, player_names=filter_df['Name'], data=filter_df.drop(columns=['Name']),len_df = len(filter_df), wordcloud_files = filter_wordclouds, plot_files = filter_barplots, player_name = player_name)

if __name__=="__main__":
    app.run(debug=True)