import requests
import bs4
import csv
from DataModel import DataModel

dataModel = DataModel()


def getData(url):
    pageUrlString = "?pst=2018&pkw=Yazilim%20Muhendisi&cp="
    counter = 0
    pages = 20
    for i in range(pages):
        requestsUrl = ""
        requestUrl = url + str(i) + pageUrlString + str(i)
        r = requests.get(requestUrl)
        soup = bs4.BeautifulSoup(r.content, 'html5lib')
        table = soup.find('div', attrs={'class': 'list-items-wrapper'})

        for row in table.findAll('div', attrs={'class': 'k-ad-card-content'}):
            sponsor = row.find('span', attrs={'class': 'sponsor'})
            if not sponsor:
                job_name = row.h3.text
                comp_name = row.find('span', attrs={'class': 'kad-card-subtitle'}).text
                job_location = row.find('div', attrs={'class': 'kad-card-location'}).text
                job_type = row.find('span', attrs={'class': 'badge badge-primary'}).text
                job_add_date = row.find('span', attrs={'class': 'ad-date'}).text
                dataModel.addNewJobToAllJobs(job_name, comp_name, job_location, job_type, job_add_date)

            counter = counter + 1
    print(dataModel.printAllData())
    print(counter)
    exportToCsv()

    # r = requests.get(url)
    # soup = bs4.BeautifulSoup(r.content, 'html5lib')
    #
    # table = soup.find('div', attrs={'class': 'lister-list'})
    #
    # for row in table.findAll('div', attrs={'class': 'lister-item-content'}):
    #     print(row.h3.a.text)

    # print(soup.prettify())


def print_hi(name):
    url = "https://www.kariyer.net/is-ilanlari/yazilim+muhendisi-"
    getData(url)


def exportToCsv():
    filename = 'jobs.csv'
    with open(filename, 'w', newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        w = csv.DictWriter(f, ['jobName', "compName", "jobLocation", "jobType", "jobAddDate"])
        w.writeheader()
        for job in dataModel.allJobs:
            writer.writerow([job["jobName"], job['compName'], job['jobLocation'], job['jobType'], job['jobAddDate']])


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
