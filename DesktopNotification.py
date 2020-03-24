from plyer import notification
import requests
from bs4 import BeautifulSoup
import time



def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "download.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    #notifyMe("Faiz Elahi", "stay Home Stay safe")
    myhtmldata = getData('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(myhtmldata, 'html.parser')
    # print(soup.prettify())
    mydatastr = ""
    for tablerow in soup.find_all('tbody')[7].find_all('tr'):
        mydatastr += tablerow.get_text()
    mydatastr = mydatastr[1:]

    itemlist = mydatastr.split("\n\n")
    states = ['Delhi','Bihar','Haryana','Kerala','Maharashtra','Uttar Pradesh']

    for item in itemlist[0:23]:
        datalist = item.split("\n")
        if datalist[1] in states:
            ntitle = 'Cases of Covid-19'
            ntext = f"State: {datalist[1]}\nIndian: {datalist[2]} & Foreigner: {datalist[3]}\nCured: {datalist[4]}\nDeaths: {datalist[5]}"
            notifyMe(ntitle, ntext)
            time.sleep(5)

