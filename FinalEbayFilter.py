'''Imports'''
import json
import requests
import storage as stor


class Ebay():

    def __init__(self, python_file, name_of_text_file):
        self.pythonFile = python_file
        self.nameOfTextFile = name_of_text_file
        self.sortedList = self.sort_shopping()
        print("Sorted List: ")
        print(self.sortedList)
        self.key = python_file.key
        self.urls = self.get_urls()
        self.responses = self.login()

    def show_list(self):
        print(self.sortedList)

    def show_urls(self):
        print(self.urls)

    def get_urls(self):
        urls = []
        for (search, index) in zip(self.sortedList, range(len(self.sortedList))):
            sampleURL = ('http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findItemsByKeywords\
&sortOrder=PricePlusShippingLowest\
&buyerPostalCode=92128&SERVICE-VERSION=1.13.0\
&SECURITY-APPNAME=' + self.key +'&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD\
&itemFilter(0).name=' + 'Condition' + '\
&itemFilter(0).value=' + self.sortedList[index][1] + '\
&itemFilter(1).name=MaxPrice\
&itemFilter(1).value=' + self.sortedList[index][2] + '\
&itemFilter(1).name=MinPrice\
&itemFilter(1).value=' + self.sortedList[index][3] + '\
&itemFilter(1).paramName=Currency\
&itemFilter(1).paramValue=' + 'USD' + '\
&keywords=' + self.sortedList[index][0])
            urls.append(sampleURL)
        return urls

    def login(self, show_url=False):
        print("Logging into Ebay API")
        goodUrls = []
        with requests.Session() as s:
            for url in self.urls:
                response = requests.get(url)
                if response.status_code == 200:
                    print('Success!')
                    goodUrls.append(response)
                    if (show_url):
                        print(url)

                elif response.status_code == 404:
                    print('Not Found.')
                    print(response.status_code)
        return goodUrls

    def sort_shopping(self):
        file = open(self.nameOfTextFile, 'r')
        yourResult = [line.split(',') for line in file.readlines()]
        nestedStrings = []
        for line in yourResult:
            correctLine = []
            for word in line:
                word = word.lstrip()
                word = word.rstrip()
                correctLine.append(word)
            nestedStrings.append(correctLine)
        return nestedStrings

    def show_json(self):
        for (url, index) in zip(self.responses, range(6)):
            print(self.responses[index].json())

    # Parse document
    def parse_doc(self,show_url=True, shows_shipping_type=False):
        for (success, index) in zip(self.responses, range(6)):
            print("Parsing text file")
            parsedoc = self.responses[index].json()
            try:
                for item in (parsedoc["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
                    title = item["title"][0]
                    condition = item["condition"][0]["conditionDisplayName"][0]
                    price = item["sellingStatus"][0]["convertedCurrentPrice"][0]["__value__"]
                    if show_url:
                        url=item["viewItemURL"][0]
                    if shows_shipping_type:
                        try:
                            shipping_type = item['shippingInfo'][0]['shippingType'][0]
                        except:
                            print("can't find shipping")
                    print("Title: " + title)
                    print("Price: " + price)
                    print("Condition: " + condition)
                    if show_url:
                        print("URL: "+url)
                    if shows_shipping_type:
                        try:
                            print("Shipping type: "+shipping_type)
                        except:
                            print()
                    print()
            except KeyError:
                print('An error occurred.')


loginAttempt = Ebay(stor, "Shopping_Search_List.txt")
loginAttempt.show_urls()
loginAttempt.show_json()
loginAttempt.parse_doc()
loginAttempt.parse_doc(shows_shipping_type=True)
loginAttempt.sort_shopping()
