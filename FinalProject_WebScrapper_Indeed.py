#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import time
import requests
import csv
import os


# In[3]:


def run(url, num_of_pages, city_name):
    fw = open('job_ads_'+city_name+'.csv', 'w', encoding='utf8')
    writer = csv.writer(fw, lineterminator='\n')
    page_count = -10
    existing_vjk_ids = []
    for p in range(0, num_of_pages):
        page_count = page_count + 10
        print('page ', p)
        page_html = None
        page_url_link = url + str(page_count)
        for i in range(5):
            time.sleep(5)
            page_response = requests.get(page_url_link)
            if page_response:
                break
        if not page_response:
            print('No Response for page')
        page_html = page_response.text
        page_soup = BeautifulSoup(page_html, features="html.parser")
        vjk_ids = [element['data-jk'] for element in page_soup.findAll('div', {'class':'jobsearch-SerpJobCard unifiedRow row result'})]
        for vjk_id in vjk_ids:
            print(vjk_id)
            if vjk_id in existing_vjk_ids:
                continue
            else:
                existing_vjk_ids.append(vjk_id)
            job_url_link = 'https://www.indeed.com/viewjob?jk=' + vjk_id
            for i in range(5):
                time.sleep(5)
                job_response = requests.get(job_url_link)
                if job_response:
                    break
            if not job_response:
                print('No Response for job')
            job_html = job_response.text
            with open('output' + str(vjk_id) + '.html', 'w', encoding='utf-8') as f:
                f.write(job_html)
            job_title, job_text = 'NA', 'NA'
            job_soup = BeautifulSoup(job_html, features="html.parser")
            job_title = job_soup.find('h1', {'class':'jobsearch-JobInfoHeader-title'})
            job_text = job_soup.find('div', {'class':'jobsearch-jobDescriptionText'})
            try:
                writer.writerow([job_text.text.replace("\n","").strip(),job_title.text])
            except:
                print('caught exception')
    fw.close()


# In[4]:


url = 'https://www.indeed.com/jobs?q=title%3A(data%20engineer)&l=Houston%2C%20TX&radius=50&sort=date&start='


# In[5]:


run(url, 2, 'Houston')


# In[ ]:




