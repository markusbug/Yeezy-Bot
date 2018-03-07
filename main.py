import time
import urllib
import datetime
import webbrowser
def notify():
    print("\nHEEEEEY")
first = urllib.urlopen("http://yeezysupply.com/").read()
found = False
while(found == False):
    page = urllib.urlopen("http://yeezysupply.com/")
    html = page.read()
    if(first==html):
        print("Checked (%s)" % datetime.datetime.now().strftime('%I:%M:%S'))
        page=""
        time.sleep(4)
    else:
        notify()
        webbrowser.open("http://yeezysupply.com/")
        found = True