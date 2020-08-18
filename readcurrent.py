import requests, bs4 
from time import gmtime, strftime
import time
class Action:
    def __init__(self,name):
        self.name = name
        self.filename = self.name + ".txt"
        self.value = self.value()
        self.file = self.write_file()
        self.list = self.read_file()
        self.last = len(self.list) -1
        self.before_last = self.last -1
        self.prct = (2 * float(self.list[self.before_last]))/100

    def value(self):
        url = 'https://www.boursorama.com/recherche/' + self.name + '?searchId=' 
        r = requests.get(url) 
        soup = bs4.BeautifulSoup(r.text, 'html.parser') 
        result = soup.find(class_='c-ticker__item c-ticker__item--value')
        result = str(result)
        for i in range(0,len(result)):
            if result[i] == ">":
                result = result[i+1:]
                break
        for i in range(0,len(result)):
            if result[i] == '<':
                result =result[:i]
                break
        result = float(result)
        return(result)
    def write_file(self):
        
        f = open(self.filename,'a')
        f.write(str(self.value)+"\t")
        f.close()
        
    def read_file(self):
        try:
            f = open(self.filename,'r')
        except:
            f = open(self.filename,'a')
            f.close()
            f = open(self.filename,'r')
        return(f.read().split())
    def first_analys(self):

        if float(self.list[self.last]) > float(self.list[self.before_last]) + self.prct or float(self.list[self.last]) > float(self.list[self.before_last]) - self.prct :
            return(self.alert())

    def alert(self):
        f = open('alarm.txt','a')
        f.write((strftime("%d %m %Y %H:%M:%S",gmtime()))+" : " + self.name + ":" + self.list[self.before_last] + " ===> "+self.list[self.last]+'\n')
        f.close()
    def letsgo(self):
        self.write_file()
        self.read_file()
        self.first_analys()


list = ["INGA","PROXIMUS","CRESCENT","ABI","ACKB","AED","AGS","APAM","ARGX","BAR","COFB","COLR","GLPG","GBLB","KBC","SOF","SOLB","TNET","UCB","UMI",'WDP',"ACPH"]
while True:
    thetime = int((strftime("%H",gmtime())))
    if thetime >= 5 and thetime <= 16:
        for elem in list:
            elem = Action(elem)
            elem.letsgo()

    time.sleep(30)
    




       





