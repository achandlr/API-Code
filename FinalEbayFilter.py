'''Imports'''
import json
import requests
import storage as stor



# print(shopping_list.readline())
# txt=shopping_list.read()
# print(len(txt))

#
# shopping_list = open(r"Shopping_Search_List.txt")
# final=[]
# nestedList = []
# for line in shopping_list:
#     toSort=shopping_list.readline()
#     # for string in toSort:
#     Search = line.split(',')[0]
#     Condition = line.split(',')[1]
#     MaxPrice = line.split(',')[2]
#     MinPrice = line.split(',')[3]
#     nestedList.append(["poop", Search, Condition, MaxPrice, MinPrice])
#     # final.append(nestedList)
#     # print(nestedList)
#     # sorted.append(nestedList)
#     # print(sorted)
# print(nestedList)
#


# print(type(shopping_list))
# searches = txt.readlines()

class Ebay():

    def __init__(self, pythonFile, nameOfTextFile):
        self.pythonFile=pythonFile
        self.nameOfTextFile=nameOfTextFile
        self.sortedList=self.sortShopping()
        print(self.sortedList)
        self.key=pythonFile.key
        # urls=pythonFile.urlList
        # print(len(self.sortedList))
        self.urls=self.getUrls()
        self.responses=self.login()
        # print("LENGTH")
        # print(range(len(self.sortedList)))
        # print(type(self.sortedList[5][3]))

    def showList(self):
        print(self.sortedList)

    def showUrls(self):
        print(self.urls)
    #command to return name of variable
    def namestr(obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    def getUrls(self):
        urls=[]
        for (search, index) in zip(self.sortedList, range(len(self.sortedList))):
            sampleURL = ('http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findItemsByKeywords\
&sortOrder=PricePlusShippingLowest\
&buyerPostalCode=92128&SERVICE-VERSION=1.13.0\
&SECURITY-APPNAME=' + self.key +
'&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD\
&itemFilter(0).name='+'Condition'+'\
&itemFilter(0).value='+self.sortedList[index][1]+'\
&itemFilter(1).name=MaxPrice\
&itemFilter(1).value='+self.sortedList[index][2]+'\
&itemFilter(1).name=MinPrice\
&itemFilter(1).value='+self.sortedList[index][3]+'\
&itemFilter(1).paramName=Currency\
&itemFilter(1).paramValue='+'USD'+'\
&keywords=' + self.sortedList[index][0])
            urls.append(sampleURL)
        return urls




    # login
    #showUrl=Fals
    def login(self,showUrl=False):
        print("Logging into Ebay API")
        goodUrls=[]
        with requests.Session() as s:
            for url in self.urls:
                response = requests.get(url)
                if response.status_code == 200:
                    print('Success!')
                    goodUrls.append(response)
                    if(showUrl):
                        print(url)
                    # shows correct name of variable


                elif response.status_code == 404:
                    print('Not Found.')
                    print(response.status_code)
        return goodUrls
    def sortShopping(self):
        file = open(self.nameOfTextFile, 'r')
        yourResult = [line.split(',') for line in file.readlines()]
        nestedStrings=[]
        for line in yourResult:
            correctLine = []
            for word in line:
                word=word.lstrip()
                word=word.rstrip()
                correctLine.append(word)
            nestedStrings.append(correctLine)
        print("start here")
        print(nestedStrings)
        return nestedStrings
        # shopping_list = open(self.nameOfTextFile)
        # print("length shopping list")
        # print(len(shopping_list))
        # nestedList = []
        # for line in shopping_list:
        #     toSort = shopping_list.readline()
        #     # for string in toSort:
        #     Search = line.split(',')[0]
        #     Condition = line.split(',')[1]
        #     MaxPrice = line.split(',')[2]
        #     MinPrice = line.split(',')[3]
        #     nestedList.append([ Search, Condition, MaxPrice, MinPrice])
            # final.append(nestedList)
            # print(nestedList)
            # sorted.append(nestedList)
            # print(sorted)
        return(nestedList)

    def showContent(self):
        # content = self.responses.content
        for (url,index) in zip(self.responses,range(6)):
            print(self.responses[index].json())
        # print(self.responses.json)
        # print(type(self.responses))

    #parsedoc
    def parseDoc(self):
        for (success, index)in zip(self.responses, range(6)):
            print(success)
            # print(self.response)
            parsedoc=self.responses[index].json()
            print(parsedoc)
            print(parsedoc)
            print(parsedoc)
            for item in (parsedoc["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
                title=item["title"][0]
                condition=item["condition"][0]["conditionDisplayName"][0]
                price=item["sellingStatus"][0]["convertedCurrentPrice"][0]["__value__"]
                print("Title: "+title)
                print("Price: "+price)
                print("Condition: "+condition)
                print()

#
loginAttempt = Ebay(stor,"Shopping_Search_List.txt")
loginAttempt.showUrls()
loginAttempt.showContent()
loginAttempt.parseDoc()
loginAttempt.sortShopping()

# # loginAttempt.dummyMethod()
# content = loginAttempt.login(stor.urlList)
# loginAttempt.login(stor.urlList,True)
# # loginAttempt.dummyMethod(correctUrl)
# loginAttempt.showContent(content)
# # parsedDoc=loginAttempt.parsedoc(content)

# ebayAttempt=Ebay(stor,"Shopping_Search_List.txt")
# ebayAttempt.sortShopping()
#
# response=ebayAttempt.login(ebayAttempt.urls)
# content=ebayAttempt.showContent(response)
# # parsedDoc=ebayAttempt.parseDoc(response)
# #
# #
# # #STOPPPING 12Q3WRTHUIK0YCFREWEARUIOPIRWESDTYUIJOJYDRESTDRJKOKPGYTRHGUIOPITSDZFTY-OYTDFGHIOGFDSDUIO[-0TDSFTU90IUGDFYUI90IOGHGHYUIOPIUGXFY8908THDFTRY789YDTY88YFG STOPPING
# # #NEED TO FIX SORTED TO MAKE IT AN ARRAY OF ARRAYS AND THEN FEED THE DATA CORRECTLY THROUGH PARSE DOC IN SOME FOR OR NESTED FOR LOOP FORMAT
# #THEN EITHER CREATE A EMAIL FILTER OR ROBOT FRAMEWORK