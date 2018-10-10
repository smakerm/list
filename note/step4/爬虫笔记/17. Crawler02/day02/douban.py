# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:33:56 2018

@author: Administrator
"""
from bs4 import BeautifulSoup
import re
import basicSpider
from multiprocessing import Pool,Manager

def get_html(url):
    """
    获取一页的网页源码信息
    """
    headers = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36")]
    #proxy = {"http":"182.129.243.84:9000"}
    html = basicSpider.downloadHtml(url, headers=headers)
    return html

def get_movie_all(html):
    """
    获取当前页面中所有的电影的列表信息
    """
    soup = BeautifulSoup(html, "html.parser")
    movie_list = soup.find_all('div', class_='bd doulist-subject')
    #print(movie_list)
    return movie_list

def get_movie_one(movie):
    """
    获取一部电影的精细信息，最终拼成一个大的字符串
    """
    result = ""
    soup = BeautifulSoup(str(movie),"html.parser")
    title = soup.find_all('div', class_="title")
    soup_title = BeautifulSoup(str(title[0]), "html.parser")
    for line in soup_title.stripped_strings:
        result += line
    
    try:
        score = soup.find_all('span', class_='rating_nums')
        score_ = BeautifulSoup(str(score[0]), "html.parser")
        for line in score_.stripped_strings:
            result += "|| 评分："
            result += line
    except:
         result += "|| 评分：5.0"
         
    abstract = soup.find_all('div', class_='abstract')
    abstract_info = BeautifulSoup(str(abstract[0]), "html.parser")
    for line in abstract_info.stripped_strings:
        result += "|| "
        result += line    
    
    result += '\n'
    #print(result)
    return result

def save_file(movieInfo, lock):
    """
    写文件的操作,这里使用的追加的方式来写文件
    """
    with open("doubanMovie.txt","ab") as f:
        #lock.acquire()
        f.write(movieInfo.encode("utf-8"))
        #lock.release()

def CrawlMovieInfo(url, q, lock):
    """
    抓取电影一页数据，并写入文件
    """
    html = get_html(url)
    movie_list = get_movie_all(html)
    for it in movie_list:
        save_file(get_movie_one(it), lock)
        
    q.put(url) #已完成的url


if __name__ == "__main__":
    # 创建进程池和进程池队列来完成抓取
    pool = Pool()
    q = Manager().Queue()
    lock = Manager().Lock()
    
    url = "https://www.douban.com/doulist/3516235/?start=225&sort=seq&sub_type="    
    CrawlMovieInfo(url)
    
    html = get_html(url)
    pattern = re.compile('(https://www.douban.com/doulist/3516235/\?start=.*)"')
    itemUrls = re.findall(pattern, html)
#    for i in itemUrls:
#        print(i)
        
    # 两步去重操作
    crawl_queue = []    # 待爬队列
    crawled_queue = []  # 已爬取队列
    for item in itemUrls:
        if item not in crawled_queue: 
            # 第一步去重，确定这些url不在已爬队列中
            crawl_queue.append(item)
    #第二步去重，对待爬队列去重
    crawl_queue = list(set(crawl_queue))
    
    # 模拟广度优先遍历
    while crawl_queue: #去待爬队列中取值，直到待爬队列为空
        url = crawl_queue.pop(0)#取出待爬队列中第一个值
        #CrawlMovieInfo(url)
        pool.apply_async(func=CrawlMovieInfo, args=(url,q,lock))
        # 把已经处理完的url放入已经爬取的队列中
        urlCompeted = q.get()
        crawled_queue.append(urlCompeted)
    
    
    pool.close()
    pool.join()
        
    
    