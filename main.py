# -*- coding:utf-8 -*-

from selenium import webdriver as wd
import time
import sys
import os


baidu = "https://www.baidu.com"

step = 2
limit = 10
page_step = 10

ff_options = wd.firefox.options.Options()
ff_options.add_argument('--headless')
work = wd.Firefox(options=ff_options)


def main():
    global work,step,limit,page_step
    kw = ' '.join(sys.argv[1:])
    work.get(baidu)
    work.find_element_by_id("kw").send_keys(kw)
    work.find_element_by_id("su").click()
    home = work.current_window_handle
    i = 1
    time.sleep(1)
    while True:
        if i > limit:
            print("Turning to next page...")
            work.find_element_by_xpath("//div[@id='page']/strong/following-sibling::a[1]").click()
            limit += page_step
            time.sleep(1)
        for id in range(i, i+step):
            try:
                print('\033[34m' + str(id) + '\033[0m')
                div = work.find_element_by_id(str(id))
                print('\033[1m' + div.find_element_by_xpath("h3").text+ '\033[0m')
                print(div.find_element_by_xpath("div[1]").text)
            except:
                print('null')
                continue
        i += step
        while True:
            ln = input("^_^>")
            if ln == 'exit':
                work.quit()
                exit()
            try:
                cmd = eval(ln)
                work.find_element_by_id(str(cmd)).find_element_by_class_name("t").find_element_by_tag_name("a").click()
                time.sleep(3)
                work.switch_to.window(work.window_handles[1])
                print('\033[1m' + work.title + '\033[0m')
                print(work.find_element_by_tag_name("html").text)
                work.close()
                work.switch_to.window(home)
            except:
                break


if __name__ == '__main__':
    try:
#        os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
        main()
    except SystemExit:
        pass
    except:
        print("Sorry, something went wrong..")
    work.quit()
    os.system("rm geckodriver.log")
