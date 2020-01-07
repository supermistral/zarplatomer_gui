import requests, bs4, time
import matplotlib.pyplot as plt
from tkinter import *                               #os.path.abspath(os.path.basename(sys.argv[0]))  - путь до запускаемой проги```
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import ttk

class Parser:                                           #Сделать проверку на соответствие 50% слов запроса профессии, jobfilter - сделать деление на 2 полугодия, сделать парсинг курса валют по кнопке
    def __init__(self, text, param):                           #Запуск процесса фоновым потоком для парсинга за весь период на hh, сделать деление на строгий и нестрогий поиск
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
        self.text = text
        self.info = []                                   #Написать на графике запрос и дату
        self.width = 0.2
        self.indent = 0.3
        self.xticks = (0, self.width/2 + (self.indent - self.width), self.width + (self.indent - self.width))
        self.param = param
        self.text_param = self.text.replace('+', ' ').lower()

    def parser(self):
        global progress
        self.k = []
        self.comp_with_salary = 0
        if self.param: text = 'NAME:(' + ' AND '.join(self.text.split('+')) + ')'
        else: text = self.text
        url = 'https://hh.ru/search/vacancy?search_period=30&clusters=true&area=1&text=%s&enable_snippets=true' %text
        s = requests.get(url, headers = self.headers)
        b = bs4.BeautifulSoup(s.text, 'html.parser')
        vac = b.find_all('div', attrs = {'data-qa': 'vacancy-serp__vacancy vacancy-serp__vacancy_premium'})

        #self.amount_vacancy = int(b.find('h1', attrs = {'data-qa': 'page-title'}).getText()[0:b.find('h1', attrs = {'data-qa': 'page-title'}).getText().find('\xa0') + 1])
        self.maximum_for_progressbar(url, progress, 'h1', 'data-qa', 'page-title')
        progress['maximum'] *= 2
        #progress['maximum'] = self.amount_vacancy*2
        #temp = 0

        for self.i in vac:
            self.company = self.i.find('a', attrs = {'class': 'bloko-link HH-LinkModifier'}).getText()
            self.handler()
            self.info.append({'company': self.company, 'salary': self.salary, 'link': self.link})

            progress['value'] += 1
            progress.update()
            time.sleep(0.01)
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

                progress['value'] += 1
                progress.update()
                time.sleep(0.01)

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
                valute = 64
            elif 'EUR' in self.salary:
                valute = 71
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
        global progress
        skills = []
        for i in self.info:
            url = i['link']
            s = requests.get(url, headers = self.headers)
            b = bs4.BeautifulSoup(s.text, 'html.parser')
            if b.find('span', attrs = {'data-qa': 'skills-element'}):
                for j in b.find_all('span', attrs = {'data-qa': 'skills-element'}):
                    skills.append(j.get('data-tag-id'))

            progress['value'] += 1
            progress.update()
            time.sleep(0.01)
            
        counter = {x: skills.count(x) for x in set(skills)}
        print(counter)
        skills1 = [k for k, v in counter.items() if v == max(list(counter.values()))][0] if counter else '-'
        if skills1 != '-': counter.pop(skills1)
        skills2 = [k for k, v in counter.items() if v == max(list(counter.values()))][0] if counter else '-'
        if skills2 != '-': counter.pop(skills2)
        skills3 = [k for k, v in counter.items() if v == max(list(counter.values()))][0] if counter else '-'
        return skills1, skills2, skills3

    def parser_resume(self, age_from, age_to, x):
        global progress_2
        info = []
        temp = 0
        url = 'https://hh.ru/search/resume?L_is_autosearch=false&age_from=%d&age_to=%d&area=1&clusters=true&exp_period=all_time&label=only_with_age&logic=normal&no_magic=false&order_by=relevance&pos=full_text&search_period=30&text=%s&page=0' %(age_from, age_to, self.text)
        #self.amount_vacancy = int(b.find('h1', attrs = {'data-qa': 'page-title'}).getText()[8:].split()[0])
        self.maximum_for_progressbar(url, progress_2, 'h1', 'data-qa', 'page-title', 1)
        print(progress_2['maximum'])
        #progress_2['maximum'] = self.amount_vacancy
        while 1:
            s = requests.get(url, headers = self.headers)
            b = bs4.BeautifulSoup(s.text, 'html.parser')
            vac = b.find_all('div', attrs = {'data-qa': 'resume-serp__resume'})
            #print(vac)
            if vac == []:
                break
            for i in vac:
                progress_2['value'] += 1
                progress_2.update()
                time.sleep(0.01)
                if self.param and i.find('a', attrs = {'data-qa': 'resume-serp__resume-title'}) and not self.search_coinsidence(i.find('a', attrs = {'data-qa': 'resume-serp__resume-title'}).getText().lower()):
                    continue
                if i.find('div', attrs = {'class': 'resume-search-item__compensation'}).getText():
                    self.salary = i.find('div', attrs = {'class': 'resume-search-item__compensation'}).getText()
                    valute = 1
                    if 'бел.' in self.salary: 
                        valute = 32
                        self.salary = int(self.salary[:len(self.salary)-9].replace('\xa0', '')) * valute
                    else: 
                        if 'USD' in self.salary:
                            valute = 65
                        elif 'EUR' in self.salary:
                            valute = 71 
                        #print(self.salary)
                        self.salary = int(self.salary[:len(self.salary)-4].replace('\xa0', '')) * valute
                    if 1000000 > self.salary > 10000:
                        info.append(self.salary)
                        Tkinter.statistics[0][x] += 1
                    else:
                        continue
            temp += 1
            url = 'https://hh.ru/search/resume?L_is_autosearch=false&age_from=%d&age_to=%d&area=1&clusters=true&exp_period=all_time&label=only_with_age&logic=normal&no_magic=false&order_by=relevance&pos=full_text&search_period=30&text=%s&page=%d' %(age_from, age_to, self.text, temp)
        print(temp)
        #print(self.info_2)
        print(progress_2['value'])
        res = sum(info) // len(info)
        res_min = min([x for x in info if x > 10000])
        res_max = max([x for x in info if x > 10000])
        return res_min, res, res_max

    def parser_jobfilter(self, text):
        global progress_3
        info = []
        info2 = []
        info3 = []
        page = 0
        self.maximum_for_progressbar('https://moskva.jobfilter.ru/работа/%s?l=moskva&lt=Москва&page=1' %text, progress_3, 'div', 'id', 'search_summary')
        while 1:
            page += 1
            url = 'https://moskva.jobfilter.ru/работа/%s?l=moskva&lt=Москва&page=%d' %(text, page)
            s = requests.get(url, headers = self.headers)
            b = bs4.BeautifulSoup(s.text, 'html.parser')
            if b.find_all('div', attrs = {'class': 'srm'}) == []:
                break
            for i in b.find_all('div', attrs = {'class': 'srm'}):
                progress_3['value'] += 1
                progress_3.update()
                time.sleep(0.01)
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
                    if 'дн' in i.find('span', attrs = {'class': 'time'}).getText():
                        info.append(salary)
                        Tkinter.statistics[1][0] += 1
                    elif 'мес' in i.find('span', attrs = {'class': 'time'}).getText():
                        if 1 <= self.search_digit(i.find('span', attrs = {'class': 'time'}).getText()) <= 2:
                            info.append(salary)
                            Tkinter.statistics[1][0] += 1
                        elif 3 <= self.search_digit(i.find('span', attrs = {'class': 'time'}).getText()) <= 5:
                            info2.append(salary)
                            Tkinter.statistics[1][1] += 1
                        else:
                            info3.append(salary)
                            Tkinter.statistics[1][2] += 1
                else:
                    pass
        #print(info)
        res = sum(info) // len(info)
        res_min = min([x for x in info if x > 10000])
        res_max = max([x for x in info if x > 10000])
        res2 = sum(info2) // len(info2)
        res_min2 = min([x for x in info2 if x > 10000])
        res_max2 = max([x for x in info2 if x > 10000])
        res3 = sum(info3) // len(info3)
        res_min3 = min([x for x in info3 if x > 10000])
        res_max3 = max([x for x in info3 if x > 10000])
        return res_min, res, res_max, res_min2, res2, res_max2, res_min3, res3, res_max3

    def parser_superjob(self, age_from, age_to):
        info = []
        info_temp = ''
        page = 0
        while 1:
            page += 1
            url = 'https://www.superjob.ru/resume/search_resume.html?old1=%d&old2=%d&keywords[0][keys]=%s&keywords[0][skwc]=and&keywords[0][srws]=7&period=30&t[0]=4&page=%d' %(age_from, age_to, self.text, page)
            s = requests.get(url, headers = self.headers)
            b = bs4.BeautifulSoup(s.text, 'html.parser')
            #print(b.find('div', class_ = '_3zucV'))
            main_div_t = b.find_all('div', class_ = '_3zucV')
            main_div = ''
            for j in main_div_t:
                #print(j["class"])
                if j["class"] == ["_3zucV"]:
                    main_div = j
                    break
            if info_temp != main_div:
                info_temp = main_div
            else:
                break
            for i in main_div:
                #print(i.find('div', attrs = {'class': '_3mfro PlM3e _2JVkc _3LJqf'}).find_all('span'))
                if self.param:
                    if i.find('div', attrs = {'class': '_3mfro PlM3e _2JVkc _3LJqf'}).find_all('span'):
                        text_prof = []
                        for prof in i.find('div', attrs = {'class': '_3mfro PlM3e _2JVkc _3LJqf'}).find_all('span'):
                            text_prof.append(prof.getText().lower())
                        text_prof = ' '.join(text_prof)
                        if not self.search_coinsidence(text_prof):
                            continue
                    else:
                        continue
                #if self.param and text_param !
                #print(i.find_all('div', attrs = {'class': '_2g1F-'}))
                #print(i.find('div', attrs = {'class': '_1_bQo _2FJA4'}).find('span', attrs = {'class': '_3mfro _3Q_Pz _1ZlLP _2JVkc'}))
                #print(i.find('div', attrs = {'class': '_1_bQo _2FJA4'}))
                if i.find('div', attrs = {'class': '_1_bQo _2FJA4'}):
                    salary = i.find('div', attrs = {'class': '_1_bQo _2FJA4'}).find('span', attrs = {'class': '_3mfro _3Q_Pz _1ZlLP _2JVkc'}).find_all('span')[0].getText()
                else: 
                    continue
                #print(salary)
                #print(salary)
                if salary == 'По договорённости':
                    continue
                salary = salary.replace('\xa0', '')
                salary = salary[:len(salary)-1]
                info.append(int(salary))
        #print(info)
        res = sum(info) // len(info)
        res_min = min([x for x in info if x > 10000])
        res_max = max([x for x in info if x > 10000])
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
            self.bar = plt.bar([x + self.indent*i for x in range(3)], [args[i*3], args[i*3+1], args[i*3+2]], width = self.width, color = color[i], label = label[i])
            self.autolabel(self.bar)
        plt.xticks([x + self.xticks[len(args)//3-1] for x in range(3)], ['минимальная', 'средняя', 'максимальная'])
        plt.legend(loc = 'upper right', borderaxespad = 0., bbox_to_anchor = (1.13, 1.16), fontsize = 8)
        plt.title('Заработная плата')
        plt.ylabel('В рублях')
        plt.savefig('d:\\forwork\\hh\\%s.jpg' %name)

    def maximum_for_progressbar(self, url, progress, div, key, word, x = 0):
        progress['value'] = 0
        #print(progress)
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
            elif temp:
                break
        if x:
            num = int(num)*0.9
        progress['maximum'] = int(num)
    
    @staticmethod
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            plt.annotate('{}'.format(height), xy = (rect.get_x() + rect.get_width() / 2, height), xytext = (0, 5), textcoords = "offset points", ha = 'center', va = 'bottom', fontsize = 9)

class Tkinter:
    def __init__(self):
        #self.frame1 = Frame(root)
        #self.frame1.pack(expand = 1, fill = BOTH)
        self.frame2 = Frame(root, bg = color)
        self.frame2.pack(side = RIGHT, anchor = 'e')
        self.frame = Frame(root, bg = color, relief = FLAT)
        self.frame.pack(side = TOP)
        img = ImageTk.PhotoImage(Image.open(r'D:\forwork\hh\button2.jpg'))
        self.button_new_request = Button(self.frame2, image = img, relief = GROOVE, command = self.click_on_request_button)
        self.button_new_request.image = img
        self.button_new_request.bind("<Button-1>")
        self.button_new_request.pack_forget()
        self.label = Label(self.frame, text = 'Введите профессию', font = 'Arial 50', width = 20, height = 2, bg = color)
        self.label.grid(row = 0, column = 0, sticky = "n", columnspan = 2)
        self.text_pole = Entry(self.frame, font = 'Arial 17 bold', width = 32, borderwidth = 5, relief = 'groove', bd = 2)
        self.text_pole.grid(row = 2, column = 0, sticky = "e", padx = 10)
        self.text_pole.focus()
        self.text_pole.bind('<Return>', lambda event: self.command_for_nextbutton())
        self.button = Button(self.frame, text = 'Хочу результат', bg = '#FFC795', command = self.command_for_nextbutton, font = 'Arial 15', relief = 'flat', overrelief = 'groove', bd = 3, activebackground = '#FFCA8B')
        self.button.bind('<Button-1>')
        self.button.grid(row = 3, column = 0, sticky = "n", pady = 10, columnspan = 2)
        self.label_error = None
        global progress, progress_2, progress_3
        progress = ttk.Progressbar(self.frame, orient = 'horizontal', length = 300, style = 'green1.Horizontal.TProgressbar')
        progress.grid(row = 4, column = 0, sticky = 'n', pady = 5, columnspan = 2)
        progress_2 = ttk.Progressbar(self.frame, orient = 'horizontal', length = 300, style = 'green2.Horizontal.TProgressbar')
        progress_2.grid(row = 5, column = 0, sticky = 'n', pady = 5, columnspan = 2)
        progress_3 = ttk.Progressbar(self.frame, orient = 'horizontal', length = 300, style = 'green3.Horizontal.TProgressbar')
        progress_3.grid(row = 6, column = 0, sticky = 'n', pady = 5, columnspan = 2)
        #self.quit_button = Button(self.frame, text = 'ВЫЙТИ', bg = 'red', fg = 'white', font = 'Arial 10 bold', width = 10, height = 5, command = self.quit_command)
        #self.quit_button.bind('<Button-1>')
        #self.quit_button.place(x = 800, y = 0)
        self.var = StringVar(self.frame)
        self.optionmenu = OptionMenu(self.frame, self.var, 'строгий поиск', 'нестрогий поиск')
        self.var.set('строгий поиск')
        self.optionmenu.config(font = 'Arial 11 bold', width = 12, bg = 'white', relief = "groove", borderwidth = 1, activebackground = 'black', activeforeground = 'white')
        self.optionmenu.grid(row = 2, column = 1, sticky = 'w', ipadx = 20)
        '''self.listbox = Listbox(self.frame, height = 5, width = 15, selectmode = SINGLE)
        listbox_data = ['строгий поиск', 'нестрогий поиск']
        for i in listbox_data:
            self.listbox.insert(END, i)
        self.listbox.bind('<<ListboxSelect>>', lambda event: self.select_item())
        self.listbox.grid(row = 2, column = 1)'''
        #print(progress, progress_2, progress_3)
    
    statistics = [[0, 0, 0], [0, 0, 0]]

    def command_for_nextbutton(self):
        if self.text_pole.get():
            if self.text_pole.get().find(' ') == -1:
                self.text_2 = self.text_3 = self.text_pole
            else:
                self.text_2 = '+'.join(self.text_pole.get().split())
                self.text_3 = '-'.join(self.text_pole.get().split())
        else:
            return
        if self.var.get() == 'строгий поиск': param = 1
        else: param = 0
        a = Parser(self.text_2, param)
        try:                                                                #ConnectionError !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            self.button.config(state = 'disabled')
            percent_salary, *result_1 = a.parser()

        except:
            self.label_error = Label(self.frame, text = "Некорректный ввод", bg = color, font = 'Arial 15')
            self.label_error.grid(row = 1, column = 0, pady = 10)    
            self.text_pole.delete(0, END)
            #self.text = StringVar()
            self.button.config(state = 'normal')
            self.text_pole.config(highlightcolor = 'red', highlightthickness = 2)
            return
        s1, s2, s3 = a.parser_skills()
        stat_progress2 = []
        result_1 = a.parser_resume(18, 30, 0)
        stat_progress2.append(progress_2['value'])
        result_2 = a.parser_resume(31, 51, 1)
        stat_progress2.append(progress_2['value'])
        #mini, avg, maxi = a.parser()
        #result_4 = a.parser_resume(51, 75)
        #stat_progress.append(progress_2['value'])
        #result = result_1 + result_2 + result_3
        #a.create_plt(('blue', 'red', 'orange'), ('вакансии', '18-30', '31-50'), 'from_hh', *result)
        result = a.parser_jobfilter(self.text_3)
        a.create_plt(('#0018CF', '#0D29FF', '#4158FF'), ('3 мес.', '6 мес.', '7+ мес.'), 'from_jobfilter', *result)

        stat_progress1 = progress['value']
        stat_progress3 = progress_3['value']
        self.destroy_widget(self.button, self.label, self.text_pole, progress, progress_2, progress_3, self.optionmenu)
        if self.label_error: self.label_error.destroy()   


        '''self.frame2 = Frame(root)
        self.frame2.pack(expand = 1, anchor = E, fill = BOTH)'''

        #button_temp = Button(self.frame3, text = 'лол')
        #button_temp.pack_forget()
        #self.frame.pack(side = LEFT, anchor = N)

        self.button_new_request.pack(pady = 20)

        self.tab_control = ttk.Notebook(self.frame, padding = 0)  
        self.tab1 = Frame(self.tab_control, borderwidth = 0, relief = FLAT, bg = color)  
        self.tab2 = Frame(self.tab_control, borderwidth = 0, relief = FLAT, bg = color)
        self.tab3 = Frame(self.tab_control, borderwidth = 0, relief = FLAT, bg = color)
        self.tab_control.add(self.tab1, text = 'headhunter.ru')  
        self.tab_control.add(self.tab2, text = 'jobfilter.ru')  
        self.tab_control.add(self.tab3, text = 'superjob.ru')  
        self.tab_control.pack(expand = 1, fill = 'both')
        img = self.create_img(r'd:\forwork\hh\from_hh.jpg')
        self.panel = Label(self.tab1, image = img, compound = "center", bg = color)
        self.panel.image = img
        self.panel.grid(row = 0, column = 0)
        self.label_keys = Label(self.tab1, text = 'КЛЮЧЕВЫЕ НАВЫКИ', font = 'Arial 20 bold', width = 20, height = 2, bg = '#FFE7FD')
        self.label_keys.grid(row = 2, column = 0)
        self.label_keys_words = Label(self.tab1, text = '%s    %s    %s' %(s1, s2, s3), font = 'Arial 15', bd = 4, bg = color)
        self.label_keys_words.grid(row = 3, column = 0)
        self.label_keys_words.configure(highlightthickness = 4, highlightbackground = '#000000', highlightcolor = '#000000')
        self.label_statistics = Label(self.tab1, text = 'Вакансий найдено: %d\nРезюме в возрастной группе 18-30 лет: %d\nРезюме в возрастной группе 31-50 лет: %d' %(stat_progress1, self.statistics[0][0], self.statistics[0][1]), font = 'Arial 15', bg = color)
        self.label_statistics.grid(row = 4, column = 0)

        img = self.create_img(r'd:\forwork\hh\from_jobfilter.jpg')
        self.panel2 = Label(self.tab2, image = img, compound = "center", bg = color)
        self.panel2.image = img
        self.panel2.grid(row = 0, column = 0)
        self.label_statistics_2 = Label(
            self.tab2, text = 'Вакансий с датой публикации:\nне более 3 месяцев назад, включая текущий: %d\nне более 6 месяцев назад, включая текущий: %d\nболее 6 месяцев назад: %d' %(self.statistics[1][0], self.statistics[1][1], self.statistics[1][2]), 
            font = 'Arial 15', bg = color)
        self.label_statistics_2.grid(row = 1, column = 0)

        result_1 = a.parser_superjob(18, 30)
        result_2 = a.parser_superjob(31, 50)
        result_3 = a.parser_superjob(51, 75)
        result = result_1 + result_2 + result_3
        a.create_plt(('#0018CF', '#0D29FF', '#4158FF'), ('18-30', '31-50', '51+'), 'from_superjob', *result)
        img = self.create_img(r'd:\forwork\hh\from_superjob.jpg')
        self.panel3 = Label(self.tab3, image = img, compound = "center", bg = color)
        self.panel3.image = img
        self.panel3.grid(row = 0, column = 0)


    def create_img(self, file):
        img = Image.open(file)
        img = img.resize((800, 600), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        return img
        
    def click_on_request_button(self):
        self.destroy_widget(self.label_keys, self.label_keys_words, self.tab_control, self.button_new_request, self.frame, self.frame2)
        self.__init__()
    
    def destroy_widget(self, *args):
        for i in args:
            i.destroy()

    def quit_command(self):
        root.quit()

color = '#FFF6FE'                                                       #ДОБАВИТЬ ПОЛНЫЙ/НЕПОЛНЫЙ ПОИСК для superjob
root = Tk()
root.geometry("1000x1000")
root.title("Зарплатомер")
root.config(bg = color)

color_nonactive = "#FFFFFF"
color_active = "#FF9121"

style = ttk.Style()

style.theme_create("style", parent = "alt", settings = {
            "TNotebook": {
                "configure": {"background": color, "borderwidth": 0, "relief": GROOVE}
            },
            "TNotebook.Tab": {
                "configure": {"background": color_active, 'bordercolor': '#000000', 'font': ('Arial','15'), "padding": [80, 10], "borderwidth": 2, "activerelief": FLAT, "inactiverelief": FLAT},   #"padding": [5, 1]
                "map":       {"background": [("selected", color_nonactive)], 'fieldbackground': [('active', 'red')]}}
                         # "expand": [("selected", [1, 1, 1, 0])] } },
            } )
        #style.configure('TNotebook.Tab', font = ('URW Gothic L','11','bold'))
style.theme_use("style")
style.configure("green1.Horizontal.TProgressbar", background = '#F86C1B')                                       #!!!!!!!!!!!!!!!!!!!!!!!!!!!
style.configure("green2.Horizontal.TProgressbar", background = '#F86C1B')
style.configure("green3.Horizontal.TProgressbar", background = '#F86C1B')
style.layout(
            "Tab", [('Notebook.tab', {'sticky': 'nswe', 'children':
                [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
        #[('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                    [('Notebook.label', {'side': 'top', 'sticky': ''})],
        #})],
                    })],
                })]
            )
root.protocol("WM_DELETE_WINDOW", lambda: root.quit())
glob = Tkinter()
root.mainloop()
#plt.show()