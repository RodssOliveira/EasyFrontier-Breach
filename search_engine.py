from googleapiclient.discovery import build
from credentials import cred
from tqdm import tqdm


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

def pastebin(email):
    site_list = []
    pbar = tqdm(total=2)
    pbar.set_description('Realizando busca no Pastebin')

    my_api_key = cred['api_key']
    my_cse_id = cred['search_key']

    pbar.update(1)
    results = google_search(
        'site:pastebin.com intext:"{}:"'.format(email), my_api_key, my_cse_id, num=10)
    
    try:
        for site in results['items']:
            site_list.append(site['link'])
    except:
        pass

    pbar.set_description('Retornando resultados')
    pbar.update(1)

    return results['searchInformation']['totalResults'], site_list

def google(email):
    site_list = []
    pbar = tqdm(total=2)
    pbar.set_description('Realizando Busca no Google')

    my_api_key = cred['api_key']
    my_cse_id = cred['search_key']

    pbar.update(1)

    #email = email.split('@')
    #email = '"' + email[0] + '"@' + email[1]
    #print(email)

    results = google_search(email, my_api_key, my_cse_id, num=10)

    #print(results)

    try:
        for site in results['items']:
            site_list.append(site['link'])
    except:
        pass

    pbar.set_description('Retornando resultados')
    pbar.update(1)

    return results['searchInformation']['totalResults'], site_list


if __name__ == '__main__':
    email = 'joanne_reduta@hotmail.com'
    pastebin(email)