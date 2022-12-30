import requests
import bs4
import csv
from DataModel import DataModel
import time

# import lxml
dataModel = DataModel()


def getData(url, gBand):
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.content, "html5lib")
    content = soup.findAll('a', attrs={'class': 'position-absolute d-flex align-items-center justify-content-center'})
    counter = 0
    for card in content:
        try:
            pageUrl = "https://www.atasunoptik.com.tr/" + card['href']
            r = requests.get(pageUrl)
            soup2 = bs4.BeautifulSoup(r.content, "html5lib")
            price = soup2.find('div', attrs={'class': 'd-flex align-items-end p-price'}).span.text
            gD1 = soup2.findAll('span', attrs={'class': 'col-4 col-sm col-hg-auto d-flex flex-column align-items-center '
                                                       'justify-content-center'})[0].span.text
            gD2 = soup2.findAll('span', attrs={'class': 'col-4 col-sm col-hg-auto d-flex flex-column align-items-center '
                                                       'justify-content-center'})[1].span.text
            gD3 = soup2.findAll('span', attrs={'class': 'col-4 col-sm col-hg-auto d-flex flex-column align-items-center '
                                                              'justify-content-center'})[2].span.text
        except:
            print("error")
        finally:
            dataModel.addNewGlassesToAllGlasses(gBand, price, gD1, gD2, gD3)
            counter = counter + 1
            print(counter)

    dataModel.printAllData()


def exportToCsv():
    filename = 'glasses.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        w = csv.DictWriter(f, ['Marka', "Fiyat", "Cam genişliği", "Gözlük genişliği", "Gözlük Uzunluğu"])
        w.writeheader()
        for glasses in dataModel.allGlasses:
            writer.writerow([glasses["gBand"], glasses['gPrice'], glasses['gD1'], glasses['gD2'], glasses['gD3']])


if __name__ == '__main__':
    getData("https://www.atasunoptik.com.tr/ray-ban-marka-gunes-gozlugu-modelleri?ps=5000&st=1", 'Ray-Ban')
    getData("https://www.atasunoptik.com.tr/gunes-gozlugu?m=inesta", 'Inesta')
    getData("https://www.atasunoptik.com.tr/gunes-gozlugu?m=prada", 'Prada')
    getData("https://www.atasunoptik.com.tr/gunes-gozlugu?m=emporio-armani", 'Emporio Armani')
    getData("https://www.atasunoptik.com.tr/gunes-gozlugu?m=mustang", 'Mustang')
    getData("https://www.atasunoptik.com.tr/gunes-gozlugu?m=guess", 'Guess')
    getData("https://www.atasunoptik.com.tr/gunes-gozlugu?m=vogue", 'Vogue')
    getData("https://www.atasunoptik.com.tr/gunes-gozlugu?m=unofficial", 'Unofficial')
    exportToCsv()
