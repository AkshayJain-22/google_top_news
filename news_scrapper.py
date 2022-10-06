from bs4 import BeautifulSoup as bs
import requests, lxml

def scrapper(q):
    headers = {
        'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    params = {
    'q': q,
    'gl': 'us',
    }

    html = requests.get('https://www.google.com/search?q=', headers=headers, params=params)
    soup = bs(html.text, 'lxml')

    all_news = soup.select('.BVG0Nb')
    result = {
                'Name': q,
                'titles':[],
                'sources':[],
                'pub_times':[]
             }
    for news in all_news:
        try:
            title = news.select_one('span').text.replace('\n','')
            source = news.find('div', attrs={'class':'BNeawe tAd8D AP7Wnd'}).text.split('\n')[0]
            pub_time = news.find('div', attrs={'class':'BNeawe tAd8D AP7Wnd'}).text.split('\n')[1]
        except:
            pass
        else:
            result['Name'] = q
            result['titles'].append(title)
            result['sources'].append(source)
            result['pub_times'].append(pub_time)
    return(result)