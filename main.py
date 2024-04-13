from requests_html import HTMLSession
from pynput import keyboard
import webbrowser

visited_links = []
keyword = 'https://en.wikipedia.org/wiki'
doCrawl = True

def on_press(key):
    if key == keyboard.Key.esc:
        global doCrawl 
        doCrawl = False
        return False

def crawl(url,session):
    r = session.get(url)
    for link in r.html.absolute_links:
        if doCrawl is False:
            break
        elif link not in visited_links and keyword in link:
            visited_links.append(link)
            print(link)
            crawl(link,session)

def main(url):
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    #listener.join()
    session = HTMLSession()
    crawl(url,session)
    webbrowser.open(visited_links[-1])

if __name__=='__main__':
    url = 'https://en.wikipedia.org/wiki/Special:Random'
    main(url)