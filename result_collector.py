from give_me_q import q_generator
from news_scrapper import scrapper

def final_results():
    results = []
    names = q_generator()

    for name in names:
        results.append(scrapper(name))
    print(len(results))
    return(results)