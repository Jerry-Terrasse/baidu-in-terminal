# -*- coding:utf-8 -*-

from selenium import webdriver as wd
import time
import sys


baidu = "https://www.baidu.com"

step = 2
limit = 10
page_step = 10

ff_options = wd.firefox.options.Options()
ff_options.add_argument('--headless')
work = wd.Firefox(options=ff_options)


def main():
    kw = ' '.join(sys.argv[1:])
#    print(kw)
    work.get(baidu)
#    time.sleep(1)
    work.find_element_by_id("kw").send_keys(kw)
    work.find_element_by_id("su").click()
    home = work.current_window_handle
    i = 1
    while True:
        for id in range(i, i+step):
            print('\033[34m' + str(id) + '\033[0m')
#            input("pause")
            print('\033[1m' + work.find_element_by_id(str(id)).find_element_by_class_name("t").text + '\033[0m')
#            input("pause")
#            time.sleep(0.5)
            print(work.find_element_by_id(str(id)).find_element_by_class_name("c-abstract").text)
#            input("pause")
#            time.sleep(0.5)
        i += step
        ln = input(">>>")
        try:
            cmd = eval(ln)
            work.find_element_by_id(str(cmd)).find_element_by_class_name("t").find_element_by_tag_name("a").click()
            handles = work.window_handles
            for handle in handles:
                if handle != home:
                    work.switch_to_window(handle)
                    break
            print('\033[1m' + work.title + '\033[0m')
            print(work.find_element_by_tag_name("html").text)
            exit()
        except:
            continue
        if i > limit:
#            work.get_element_by_id("page").get_element_by_tag_name("strong").find_element_by_xpath("")
            work.find_element_by_xpath("//div[@id='page']/strong/following-sibling::a[1]").click()
            limit += page_step


if __name__ == '__main__':
    try:
        main()
    except:
        print("Sorry, something went wrong..")
    work.quit()
