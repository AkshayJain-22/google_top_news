from give_me_q import q_generator
from news_scrapper import scrapper

def final_results(names):
    results = []
    for name in names:
        results.append(scrapper(name))
    return(results)