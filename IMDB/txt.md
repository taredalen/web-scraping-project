import requests
wjdata = requests.get('url').json()
print wjdata['data']['current_condition'][0]['temp_C']

----

pip show ipympl




start = time.time()
print('starting')


def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

print("{}".format(convert(time.time() - start)))





        box_office = soup.find_all('span', {'class': 'ipc-metadata-list-item__list-content-item'})
        box_title = soup.find_all('span', {'class': 'ipc-metadata-list-item__label'})

        for box in box_office:
            number = ''.join(re.findall(r'\b\d+\b', box_office.text))
            list_boxes.append(box_office.text)


        box_office = soup.find('section', {'cel_widget_id': 'StaticFeature_BoxOffice'}).find_all('li')

        for box in box_office:
            box_name = box.find('span').text
            print(box_name)
            print('-----')
