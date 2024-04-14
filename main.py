from requests_html import HTMLSession # Importing a thing that lets me do website interaction stuff
from pynput import keyboard # Importing a thing that lets me detect key presses
import webbrowser # Importing a thing that lets me open websites in a web browser

visited_links = [] # Set up a list that I will add visited links to
keyword = 'https://en.wikipedia.org/wiki/' # Set up a keyword that I will make sure is in each link (to make sure it doesn't leave wikipedia)
doCrawl = True # Set up a variable that I will use to tell the crawler when to stop

def on_press(key): # Set up a function that will run when a key is pressed
    if key == keyboard.Key.esc: # If the key pressed is escape
        global doCrawl # Make sure we have the right variable
        doCrawl = False # Set that variable to false
        return False # End the keyboard listener

def crawl(url,session): # Set up a function that will run on each link
    r = session.get(url) # Get the page from the link
    for link in r.html.absolute_links: # For each link on the page
        if doCrawl is False: # If I have told the crawler to stop
            break # Stop the crawler
        elif link not in visited_links and keyword in link: # If the link is not in the visited links list and the keyword is in the link
            visited_links.append(link) # Add the link to the visited links list
            print(link) # Print the link to the console
            crawl(link,session) # Run this function again on the new found link (this is why it's called recursive)

def main(url): # Set up the main function that will run at the start of the program
    listener = keyboard.Listener(on_press=on_press) # Set up the keyboard listener
    listener.start() # Start the listener
    session = HTMLSession() # Make the website interaction thing work
    crawl(url,session) # Run the crawler on the url defined below
    webbrowser.open(visited_links[-1]) # Once the crawling is done, open the last link in the visited links list in my web browser

url = 'https://en.wikipedia.org/wiki/Special:Random' # Set a variable to the link I want the crawler to start on
main(url) # Run the main function, sending it the link I want the crawler to start on