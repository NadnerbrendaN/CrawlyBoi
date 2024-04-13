from requests_html import HTMLSession

visited_links = []
keyword = 'https://en.wikipedia.org/wiki'

def crawl(url,session):
    r = session.get(url)
    for link in r.html.absolute_links:
        if link not in visited_links and keyword in link:
            visited_links.append(link)
            print(link)
            crawl(link,session)

def main(url):
    session = HTMLSession()
    crawl(url,session)

if __name__=='__main__':
    url = 'https://en.wikipedia.org/wiki/Special:Random'
    main(url)