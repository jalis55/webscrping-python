from bs4 import BeautifulSoup
import requests
import csv


csv_file = open('details.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['No', 'Name_of_Company', 'Address', 'Phone', 'Industry'])

def scrap_data(max_page):

    page=1
    while max_page>=page:
        source = requests.get('http://www.kemenperin.go.id/direktori-perusahaan?what=&prov=&hal=%d'%page).text
        soup = BeautifulSoup(source, 'lxml')
        tr_list = soup.findAll("tr", {"valign": "top"})

        for tr in tr_list:
            td_list = tr.findAll("td")
            No = td_list[0].text
            Company = td_list[1].b.text
            Address = td_list[1].contents[2]
            Phone = td_list[1].contents[4]
            Phone = Phone[6:]
            Industry = td_list[2].text  # industry

            csv_writer.writerow([No, Company, Address, Phone, Industry])
            print(No)

            print(Company)
            print(Address)
            print(Phone)
            print(Industry)
            print("=============================================")
        page=page+1

scrap_data(489)
csv_file.close()









