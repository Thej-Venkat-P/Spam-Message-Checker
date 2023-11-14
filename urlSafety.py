from bs4 import BeautifulSoup as bs
import requests
import re

def checkLink(link):
    if "https" not in link and "http" in link:
        return "Dangerous Website"
    link=re.sub(r"https?://","",link)
    link=re.sub(r"^www\.", "", link)
    response = requests.get("https://www.urlvoid.com/scan/" + link)
    if response.ok:
        soup = bs(response.text, 'html.parser')
        danger=soup.select(".label-danger")
        if len(danger)>0:
            return "Dangerous Website"
        safe=soup.select(".label-success")
        if len(safe)>0:
            return "Mostly Safe Website"
        return "Unable to Verify Website safety"
    else:
        return "Unable to Verify Website safety"


if __name__=="__main__":
    url="Youtube.com"
    print(url,checkLink(url))
    url="y0utube.com"
    print(url,checkLink(url))
