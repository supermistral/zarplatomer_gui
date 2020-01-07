# -*- coding: utf-8 -*-
from design import *
from classes import *
from PyQt5 import QtCore, QtGui, QtWidgets
import requests, bs4, datetime, sys, shelve, threading, time
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

class Parser:                                        
    def __init__(self, text, param, progress1, progress2, progress3, param1, param2):  
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
        self.text = text
        self.info = []    
        self.width = 0.2
        self.indent = 0.3
        self.xticks = (0, self.width/2 + (self.indent - self.width), self.width + (self.indent - self.width))
        self.param = param
        self.param1 = param1
        self.text_param = self.text.replace('+', ' ').lower()
        self.progress1 = progress1
        self.progress2 = progress2
        self.progress3 = progress3
        self.maxzp = param2
        self.currency_values()

    def currency_values(self):
        with shelve.open('temporary') as file:
            #self.valute_usd = float(file.readline().strip('\n'))
            self.valute_usd = file['usd']
            self.valute_eur = file['eur']
            #self.valute_eur = float(file.readline().strip('\n'))

    def parser(self):
        self.k = []
        self.comp_with_salary = 0
        if self.param: text = 'NAME:(' + ' AND '.join(self.text.split('+')) + ')'
        else: text = 'NAME:(' + self.text + ')'
        print(text)
        url = 'https://hh.ru/search/vacancy?search_period=30&clusters=true&area=1&text=%s&enable_snippets=true' %text
        s = requests.get(url, headers = self.headers)
        b = bs4.BeautifulSoup(s.text, 'html.parser')
        vac = b.find_all('div', attrs = {'data-qa': 'vacancy-serp__vacancy vacancy-serp__vacancy_premium'})

        #self.amount_vacancy = int(b.find('h1', attrs = {'data-qa': 'page-title'}).getText()[0:b.find('h1', attrs = {'data-qa': 'page-title'}).getText().find('\xa0') + 1])
        self.maximum_for_progressbar(url, self.progress1, 'h1', 'data-qa', 'page-title')
        self.progress1.setMaximum(self.progress1.maximum()*2)
        #progress['maximum'] = self.amount_vacancy*2
        #temp = 0

        for self.i in vac:
            self.company = self.i.find('a', attrs = {'class': 'bloko-link HH-LinkModifier'}).getText()
            self.handler()
            self.info.append({'company': self.company, 'salary': self.salary, 'link': self.link})
            self.progress1.setValue(self.progress1.value() + 1)
        #page = int(b.find('span', attrs = {'class': 'pager-item-not-in-short-range'}).find('a').get('data-page')) + 1
        #print(page)
        #for i in range(page):
        amount = 0
        while 1:
            url_local = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&search_period=30&text=%s&page=%d' %(text, amount)
            s = requests.get(url_local, headers = self.headers)
            b = bs4.BeautifulSoup(s.text, 'html.parser')
            vac = b.find_all('div', attrs = {'class': 'vacancy-serp-item'})
            if vac == []:
                break
            #print(vac)
            amount += 1
            for self.i in vac:
                self.company = self.i.find('a', attrs = {'class': 'bloko-link HH-LinkModifier'}).getText()
                #print(company)
                self.handler()
                self.info.append({'company': self.company, 'salary': self.salary, 'link': self.link})
                self.progress1.setValue(self.progress1.value() + 1)

        Zarplatomer_schedule.statistics_amount_prof[0][0] = self.progress1.value()
        percent_salary = self.comp_with_salary / len(self.info) * 100
        #print(info)
        #print(amount)
        self.res = sum(self.k) // len(self.k)
        self.res_min = min([x['salary'] for x in self.info if x['salary'] != '-'])
        self.res_max = max([x['salary'] for x in self.info if x['salary'] != '-'])
        #print(self.info)
        print(self.res)
        print('%.1f' %percent_salary)
        return percent_salary, self.res_min, self.res, self.res_max

    def handler(self):
        if self.i.find('div', attrs = {'class': 'vacancy-serp-item__compensation'}):
            self.salary = self.i.find('div', attrs = {'class': 'vacancy-serp-item__compensation'}).getText()
            self.comp_with_salary += 1
            valute = 1
            if 'USD' in self.salary:
                valute = self.valute_usd
            elif 'EUR' in self.salary:
                valute = self.valute_eur
            if 'от' == self.salary[:2] or self.salary[:2] == 'до':
                self.salary = int(self.salary[3:len(self.salary)-4].replace('\xa0', '')) * valute
            elif '-' in self.salary:
                self.salary = self.salary[:len(self.salary)-4]
                temp = self.salary.split('-')
                self.salary = (int(temp[0].replace('\xa0', '')) * valute + int(temp[1].replace('\xa0', '')) * valute) // 2
            else:
                self.salary = int(self.salary[:len(self.salary)-4].replace('\xa0', '')) * valute
            self.k.append(self.salary)
        else:
            self.salary = '-'
        self.link = self.i.find('a', attrs = {'data-qa': 'vacancy-serp__vacancy-title'}).get('href')

    def parser_skills(self):
        skills = []
        for i in self.info:
            url = i['link']
            s = requests.get(url, headers = self.headers)
            b = bs4.BeautifulSoup(s.text, 'html.parser')
            self.progress1.setValue(self.progress1.value() + 1)
            if b.find('span', attrs = {'data-qa': 'skills-element'}):
                for j in b.find_all('span', attrs = {'data-qa': 'skills-element'}):
                    skills.append(j.get('data-tag-id'))

        self.progress1.setValue(self.progress1.maximum())
        counter = {x: skills.count(x) for x in set(skills)}
        print(counter)
        skills1 = [k for k, v in counter.items() if v == max(list(counter.values()))][0] if counter else '-'
        if skills1 != '-': counter.pop(skills1)
        skills2 = [k for k, v in counter.items() if v == max(list(counter.values()))][0] if counter else '-'
        if skills2 != '-': counter.pop(skills2)
        skills3 = [k for k, v in counter.items() if v == max(list(counter.values()))][0] if counter else '-'
        return skills1, skills2, skills3

    def parser_resume(self, age_from, age_to):
        info = []
        temp = 0
        if self.param:
            for_text = 'position'
        else:
            for_text = 'full_text'
        url = 'https://hh.ru/search/resume?L_is_autosearch=false&age_from=%d&age_to=%d&area=1&clusters=true&exp_period=all_time&label=only_with_age&logic=normal&no_magic=false&order_by=relevance&pos=%s&search_period=30&text=%s&page=0' %(age_from, age_to, for_text, self.text)
        #self.amount_vacancy = int(b.find('h1', attrs = {'data-qa': 'page-title'}).getText()[8:].split()[0])
        self.maximum_for_progressbar(url, self.progress1, 'h1', 'data-qa', 'page-title', 1)
        if age_from == 18:
            count = 1
        else:
            count = 2
        #progress_2['maximum'] = self.amount_vacancy
        while 1:
            s = requests.get(url, headers = self.headers)
            b = bs4.BeautifulSoup(s.text, 'html.parser')
            vac = b.find_all('div', attrs = {'data-qa': 'resume-serp__resume'})
            #print(vac)
            if vac == []:
                break
            for i in vac:
                self.progress1.setValue(self.progress1.value() + 1)
                if i.find('div', attrs = {'class': 'resume-search-item__compensation'}).getText():
                    self.salary = i.find('div', attrs = {'class': 'resume-search-item__compensation'}).getText()
                    valute = 1
                    if 'бел.' in self.salary: 
                        valute = 32
                        self.salary = int(self.salary[:len(self.salary)-9].replace('\xa0', '')) * valute
                    else: 
                        if 'USD' in self.salary:
                            valute = self.valute_usd
                        elif 'EUR' in self.salary:
                            valute = self.valute_eur
                        #print(self.salary)
                        self.salary = int(self.salary[:len(self.salary)-4].replace('\xa0', '')) * valute
                    if self.maxzp > self.salary > 10000:
                        info.append(self.salary)
                        #Tkinter.statistics[0][x] += 1
                        Zarplatomer_schedule.statistics_amount_prof[0][count] += 1
                    else:
                        continue
            temp += 1
            url = 'https://hh.ru/search/resume?L_is_autosearch=false&age_from=%d&age_to=%d&area=1&clusters=true&exp_period=all_time&label=only_with_age&logic=normal&no_magic=false&order_by=relevance&pos=%s&search_period=30&text=%s&page=%d' %(age_from, age_to, for_text, self.text, temp)
        print(temp)
        #print(self.info_2)
        self.progress1.setValue(self.progress1.maximum())
        res = sum(info) // len(info)
        res_min = min([x for x in info])
        res_max = max([x for x in info])
        return res_min, res, res_max

    def parser_jobfilter(self, text):
        info = []
        info2 = []
        info3 = []
        page = 0
        self.maximum_for_progressbar('https://moskva.jobfilter.ru/работа/%s?l=moskva&lt=Москва&page=1' %text, self.progress2, 'div', 'id', 'search_summary')
        while 1:
            page += 1
            url = 'https://moskva.jobfilter.ru/работа/%s?l=moskva&lt=Москва&page=%d' %(text, page)
            s = requests.get(url, headers = self.headers)
            b = bs4.BeautifulSoup(s.text, 'html.parser')
            if b.find_all('div', attrs = {'class': 'srm'}) == []:
                break
            for i in b.find_all('div', attrs = {'class': 'srm'}):
                self.progress2.setValue(self.progress2.value() + 1)
                if self.param and not self.search_coinsidence(i.find('span', attrs = {'class': 'title'}).getText().lower()):
                    continue
                if i.find('span', attrs = {'class': 'moneynum'}):
                    salary = i.find('span', attrs = {'class': 'moneynum'}).get_text()
                    if 'от' in salary or 'до' in salary:
                        salary = int(salary[3:])
                    elif '-' in salary:
                        salary = (int(salary[:salary.find('-')-1]) + int(salary[salary.find('-')+1:])) // 2
                    else:
                        salary = int(salary)

                    if self.maxzp < salary or salary < 10000:
                        continue

                    if 'дн' in i.find('span', attrs = {'class': 'time'}).getText():
                        info.append(salary)
                        #Tkinter.statistics[1][0] += 1
                        Zarplatomer_schedule.statistics_amount_prof[1][0] += 1
                    elif 'мес' in i.find('span', attrs = {'class': 'time'}).getText():
                        if 1 <= self.search_digit(i.find('span', attrs = {'class': 'time'}).getText()) <= 2:
                            info.append(salary)
                            #Tkinter.statistics[1][0] += 1
                            Zarplatomer_schedule.statistics_amount_prof[1][0] += 1
                        elif 3 <= self.search_digit(i.find('span', attrs = {'class': 'time'}).getText()) <= 5:
                            info2.append(salary)
                            #Tkinter.statistics[1][1] += 1
                            Zarplatomer_schedule.statistics_amount_prof[1][1] += 1
                        else:
                            info3.append(salary)
                            #Tkinter.statistics[1][2] += 1
                            Zarplatomer_schedule.statistics_amount_prof[1][2] += 1
                else:
                    pass
        #print(info)
        self.progress2.setValue(self.progress2.maximum())
        res = sum(info) // len(info)
        res_min = min([x for x in info])
        res_max = max([x for x in info])
        res2 = sum(info2) // len(info2)
        res_min2 = min([x for x in info2])
        res_max2 = max([x for x in info2])
        res3 = sum(info3) // len(info3)
        res_min3 = min([x for x in info3])
        res_max3 = max([x for x in info3])
        return res_min, res, res_max, res_min2, res2, res_max2, res_min3, res3, res_max3

    def parser_superjob(self, age_from, age_to):
        info = []
        info_temp = ''
        page = 0
        if self.param:
            superjob_filter = 60
        else:
            superjob_filter = 7
        if self.param1:
            period = '&period=30'
        else:
            period = ''
        self.maximum_for_progressbar('https://www.superjob.ru/resume/search_resume.html?old1=%d&old2=%d&keywords[0][keys]=%s&keywords[0][skwc]=and&keywords[0][srws]=%d%s&t[0]=4&page=1' %(age_from, age_to, self.text, superjob_filter, period), self.progress3, 'span', 'class', '_3mfro _1ZlLP _2JVkc _2VHxz')
        print(self.progress3.maximum())
        if age_from == 18:
            count = 0
        elif age_from == 31:
            count = 1
        else:
            count = 2
        while 1:
            page += 1
            url = 'https://www.superjob.ru/resume/search_resume.html?old1=%d&old2=%d&keywords[0][keys]=%s&keywords[0][skwc]=and&keywords[0][srws]=%d%s&t[0]=4&page=%d' %(age_from, age_to, self.text, superjob_filter, period, page)
            s = requests.get(url, headers = self.headers)
            b = bs4.BeautifulSoup(s.text, 'html.parser')
            #print(b.find('div', class_ = '_3zucV'))
            main_div_t = b.find_all('div', class_ = '_3zucV')
            main_div = ''
            #print(url1)
            #print(url)
            for j in main_div_t:
                #print(j["class"])
                if j["class"] == ["_3zucV"]:
                    main_div = j
                    break
            #print(info_temp == main_div)
            if info_temp != main_div:
                info_temp = main_div
            else:
               #print(info_temp, end = '\n\n')
                #print(main_div)
                break
            for i in main_div:
                #print(i)
                self.progress3.setValue(self.progress3.value() + 1)
                #print(self.progress3.value())
                #print(i.find('div', attrs = {'class': '_3mfro PlM3e _2JVkc _3LJqf'}).find_all('span'))

                #if self.param:
                #    if i.find('div', attrs = {'class': '_3mfro PlM3e _2JVkc _3LJqf'}).find_all('span'):
                #        text_prof = []
                #        for prof in i.find('div', attrs = {'class': '_3mfro PlM3e _2JVkc _3LJqf'}).find_all('span'):
                #            text_prof.append(prof.getText().lower())
                #        text_prof = ' '.join(text_prof)
                #        if not self.search_coinsidence(text_prof):
                #            continue
                #    else:
                #        continue

                #if self.param and text_param !
                #print(i.find_all('div', attrs = {'class': '_2g1F-'}))
                #print(i.find('div', attrs = {'class': '_1_bQo _2FJA4'}).find('span', attrs = {'class': '_3mfro _3Q_Pz _1ZlLP _2JVkc'}))
                #print(i.find('div', attrs = {'class': '_1_bQo _2FJA4'}))
                if i.find('span', attrs = {'class': '_3mfro _3Q_Pz _1ZlLP _2JVkc'}):
                    salary = i.find('span', attrs = {'class': '_3mfro _3Q_Pz _1ZlLP _2JVkc'}).find_all('span')[0].getText()
                else: 
                    continue
                if salary == 'По договорённости':
                    continue
                salary = salary.replace('\xa0', '')
                salary = salary[:len(salary)-1]

                if self.maxzp < salary or salary < 10000:
                    continue

                info.append(int(salary))
                Zarplatomer_schedule.statistics_amount_prof[2][count] += 1
        #print(page)
        self.progress3.setValue(self.progress3.maximum())
        #print(info)
        res = sum(info) // len(info)
        res_min = min([x for x in info])
        res_max = max([x for x in info])
        print(res, res_min, res_max)
        return res_min, res, res_max
    
    def search_coinsidence(self, text):
        k = 0
        for word in self.text_param:
            if word in text:
                k += 1
        if k == len(self.text_param):
            return True
        return False
    
    def search_digit(self, text):
        digit = list(filter(str.isdigit, text))
        digit = ''.join(digit)
        return int(digit)

    def create_plt(self, color, label, name, *args):
        fig = plt.figure()
        for i in range(len(args)//3):
            self.bar = plt.bar([x + self.indent*i for x in range(3)], [int(args[i*3]), int(args[i*3+1]), int(args[i*3+2])], width = self.width, color = color[i], label = label[i])
            self.autolabel(self.bar)
        plt.xticks([x + self.xticks[len(args)//3-1] for x in range(3)], ['минимальная', 'средняя', 'максимальная'])
        plt.legend(loc = 'upper right', borderaxespad = 0., bbox_to_anchor = (1.13, 1.16), fontsize = 8)
        plt.title('Заработная плата')
        plt.ylabel('В рублях')
        plt.savefig('images\\%s.jpg' %name)

    def maximum_for_progressbar(self, url, progress, div, key, word, x = 0):
        #print(progress)
        progress.setValue(0)
        s = requests.get(url, headers = self.headers)
        b = bs4.BeautifulSoup(s.text, 'html.parser')
        amount = b.find(div, attrs = {key: word}).getText()
        print(amount)
        num = ''
        temp = 0
        for i in amount:
            if i.isdigit():
                temp = 1
                num += i
            elif temp and (i == ' ' or i == '\xa0'):
                continue
            elif temp:
                break
        if x:
            num = int(num)*0.9
        progress.setMaximum(int(num))
    
    @staticmethod
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            plt.annotate('{}'.format(height), xy = (rect.get_x() + rect.get_width() / 2, height), xytext = (0, 2), textcoords = "offset points", ha = 'center', va = 'bottom', fontsize = 9)



class Zarplatomer(QtWidgets.QMainWindow):
    mysignal = QtCore.pyqtSignal(list, name = "mysignal")
    mysignal2 = QtCore.pyqtSignal(name = "mysignal2")
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_main.clicked.connect(lambda: self.start_thread())
        self.ui.button_main.setAutoDefault(True)
        self.ui.button_valute.clicked.connect(self.parser_valute)
        self.start_valute()
        self.setWindowTitle("Зарплатомер - главная")
#        self.mythread = MyThread(self, self)
#        self.mythread.mysignal.connect()
#        self.mythread.finished.connect(self.after_parser)

    def start_thread(self):
        self.ui.button_main.setDisabled(True)
        self.ui.lineEdit.setDisabled(True)
        self.mysignal.connect(self.start_after_parser, QtCore.Qt.QueuedConnection)
        self.mysignal2.connect(self.error)
        self.thread = MyThread(self)
        self.thread.start()

    def on_click(self):
        self.text = self.ui.lineEdit.text()
        choose1 = self.ui.combobox1.currentText()
        choose2 = self.ui.combobox2.currentText()
        choose3 = self.ui.spinBox.value()
        self.update_maxzp()
        if self.text:
            if self.text.find(' ') == -1:
                self.text_2 = self.text_3 = self.text
            else:
                self.text_2 = '+'.join(self.text.split())
                self.text_3 = '-'.join(self.text.split())
        else:
            self.ui.button_main.setEnabled(True)
            self.ui.lineEdit.setEnabled(True)
            return
        if choose1 == 'строгий поиск': param = 1
        else: param = 0 
        if choose2 == 'полный поиск': param1 = 0
        else: param1 = 1                                                               #ConnectionError !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        try:
            a = Parser(self.text_2, param, self.ui.progressBar, self.ui.progressBar2, self.ui.progressBar3, param1, choose3) 
            percent_salary, *result_1 = a.parser()
            s1, s2, s3 = a.parser_skills()                                              
            result_2 = list(a.parser_resume(18, 30))                         
            result_3 = list(a.parser_resume(31, 51))                                     

            result_hh = result_1 + result_2 + result_3                                               
            result_jobfilter = a.parser_jobfilter(self.text_3)
            result_1 = a.parser_superjob(18, 30)
            result_2 = a.parser_superjob(31, 50)
            result_3 = a.parser_superjob(51, 75)
            result_superjob = result_1 + result_2 + result_3

            Zarplatomer_schedule.statistics = [s1, s2, s3]
            self.mysignal.emit([result_hh, result_jobfilter, result_superjob, a])
        except:
            self.mysignal2.emit()
            
    def start_after_parser(self, data):
        print(data)
        data[3].create_plt(('blue', 'red', 'orange'), ('вакансии', '18-30', '31-50'), 'from_hh', *data[0])
        data[3].create_plt(('#0018CF', '#0D29FF', '#4158FF'), ('3 мес.', '6 мес.', '7+ мес.'), 'from_jobfilter', *data[1])
        data[3].create_plt(('#0018CF', '#0D29FF', '#4158FF'), ('18-30', '31-50', '51+'), 'from_superjob', *data[2])
        self.after_parser()
    
    def after_parser(self):
        global myapp
        myapp.close()
#    del myapp
        myapp = Zarplatomer_schedule()
        myapp.create_plt('images\\from_hh.jpg', 'main_img1')
        myapp.create_plt('images\\from_jobfilter.jpg', 'main_img2')
        myapp.create_plt('images\\from_superjob.jpg', 'main_img3')
        myapp.create_stat('statistics1')
        myapp.show()
#        myapp.close()
#        self.close()
#        print(self.mythread)
#        self.mythread = None
#        global myapp
#        self.close()
#        del self.mythread
#        del myapp
#        myapp = Zarplatomer_schedule()
#        print(myapp)
#        myapp.create_plt('from_hh.jpg', 'main_img1')
#        myapp.create_plt('from_jobfilter.jpg', 'main_img2')
#        myapp.create_plt('from_superjob.jpg', 'main_img3')
#        myapp.create_stat('statistics1')
#        myapp.show()
        #myapp.create_stat('statistics2')
        #myapp.create_stat('statistics3')
    
    def error(self):
        self.ui.progressBar.setValue(0)
        self.ui.progressBar2.setValue(0)
        self.ui.progressBar3.setValue(0)
        self.ui.button_main.setEnabled(True)
        self.ui.lineEdit.setEnabled(True)
        self.create_dialog()


    def parser_valute(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
        url = 'http://www.cbr.ru/'
        s = requests.get(url, headers = headers)
        b = bs4.BeautifulSoup(s.text, 'html.parser')
        usd = b.find('div', attrs = {'id': 'widget_exchange'}).find('div', attrs = {'class': 'content'}).find_all('tr')[1].find('td', attrs = {'class': 'weak'}).getText()[6:].replace(',', '.')
        eur = b.find('div', attrs = {'id': 'widget_exchange'}).find('div', attrs = {'class': 'content'}).find_all('tr')[2].find('td', attrs = {'class': 'weak'}).getText()[6:].replace(',', '.')
        usd = round(float(usd), 2)
        eur = round(float(eur), 2)
        with shelve.open('temporary') as file:
            file['usd'] = usd
            file['eur'] = eur
            file['date'] = datetime.datetime.today().strftime("%d/%m/%Y")
        self.ui.label.setText('Курс Доллара: %.2f\nКурс Евро: %.2f\nОбновлено %s' %(usd, eur, datetime.datetime.today().strftime("%d/%m/%Y")))

    def start_valute(self):
        with shelve.open('temporary') as file:
            try:
                usd = file['usd']    #= float(file.readline().strip('\n'))
                eur = file['eur']    #= float(file.readline().strip('\n'))
                date = file['date']  #= file.readline().strip('\n')
                currentMaxZp = file['maxzp']
                self.ui.spinBox.setValue(currentMaxZp)
                self.ui.horizontalSlider.setValue(currentMaxZp)
                self.ui.label.setText('Курс Доллара: %.2f\nКурс Евро: %.2f\nОбновлено %s' %(usd, eur, date))
            except:
                file['usd'] = 63
                file['eur'] = 70
                file['date'] = datetime.datetime.today().strftime("%d/%m/%Y")
                file['maxzp'] = 200000
                self.ui.spinBox.setValue(200000)
                self.ui.horizontalSlider.setValue(200000)

    def create_dialog(self):
        self.dialog = Dialog(self)
        self.dialog.button.clicked.connect(self.close_dialog)
        self.dialog.show()

    def close_dialog(self):
        self.dialog.close()

    def closeEvent(self, event):
#        print(self.mythread.isFinished())
        self.hide()
        event.accept()

    def test(self):
        self.ui.progressBar.setValue(100)

    def update_maxzp(self):
        with shelve.open('temporary') as file:
            file['maxzp'] = self.ui.spinBox.value()

class Zarplatomer_schedule(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow_shedule()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.return_on_mainwindow)
        self.ui.label_keys.setText('%s    %s    %s' %(self.statistics[0], self.statistics[1], self.statistics[2]))
        self.setWindowTitle("Зарплатомер - результаты")
#        print(self.statistics_amount_prof)

    statistics = []
    statistics_amount_prof = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def create_plt(self, file, label):
        img = Image.open(file)
        img = img.resize((800, 600), Image.ANTIALIAS)
        img.save(file)
        pix = QtGui.QPixmap(file)
        eval('self.ui.%s.setPixmap(pix)' %label)
        eval('self.ui.%s.resize(pix.width(), pix.height())' %label)

    def return_on_mainwindow(self):
        global myapp
        del myapp
        myapp = Zarplatomer()
        myapp.show()

    def create_stat(self, label):
        self.ui.statistics1.setText("Вакансий найдено: %d\nРезюме в возрастной группе 18-30 лет: %d\nРезюме в возрастной группе 31-50 лет: %d"
            %(self.statistics_amount_prof[0][0], self.statistics_amount_prof[0][1], self.statistics_amount_prof[0][2]))
        self.ui.statistics2.setText('Вакансий с датой публикации:\nне более 3 месяцев назад, включая текущий: %d\nот 3 до 6 (включительно) месяцев: %d\nболее 6 месяцев назад: %d'
            %(self.statistics_amount_prof[1][0], self.statistics_amount_prof[1][1], self.statistics_amount_prof[1][2]))
        self.ui.statistics3.setText('Резюме в возрастной группе 18-30 лет: %s\nРезюме в возрастной группе 31-50 лет: %s\nРезюме в возрастной группе 51+ лет: %s' 
            %(self.statistics_amount_prof[2][0], self.statistics_amount_prof[2][1], self.statistics_amount_prof[2][2]))
        #self.ui.statistics3.setText()
    
    def closeEvent(self, event):
        self.hide()
        event.accept()

class MyThreading(threading.Thread):
    singal2 = QtCore.pyqtSignal()
    def __init__(self, mainwindow):
        threading.Thread.__init__(self)
        self.daemon = True
        self.mainwindow = mainwindow

    def run(self):
        self.mainwindow.on_click()    
        self.mainwindow.mysignal.emit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Zarplatomer()
    myapp.show()
#    myapp.zarplatomer_show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())  #app.exec_()
