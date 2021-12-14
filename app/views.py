"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

from bs4 import BeautifulSoup
from selenium import webdriver
import time 

from app.models import Playlist,Channel,Watch

def upload(soup):
    allmusic = soup.findAll('a', class_='yt-simple-endpoint style-scope yt-formatted-string')
    url1="https://music.youtube.com"
    for data in allmusic:
        t1=str(data.contents[0])
        t2=str(data.attrs['href'])
        if t2.find("playlist")!=-1 or t2.find("browse")!=-1:
            temp=Playlist(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Playlist.objects.filter(url__contains=t2))==0:
                temp.save()
        elif t2.find("channel")!=-1:
            temp=Channel(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Channel.objects.filter(url__contains=t2))==0:
                temp.save()
        elif t2.find("watch")!=-1:
            temp=Watch(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Watch.objects.filter(url__contains=t2))==0:
                temp.save()
        else:
            print(t1,t2)
            
    allmusic = soup.findAll('a', class_='yt-simple-endpoint image-wrapper style-scope ytmusic-two-row-item-renderer')
    url1="https://music.youtube.com"

    for data in allmusic:
        t1=str(data.contents[0])
        t2=str(data.attrs['href'])
        if t2.find("playlist")!=-1 or t2.find("browse")!=-1:
            temp=Playlist(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Playlist.objects.filter(url__contains=t2))==0:
                temp.save()
        elif t2.find("channel")!=-1:
            temp=Channel(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Channel.objects.filter(url__contains=t2))==0:
                temp.save()
        elif t2.find("watch")!=-1:
            temp=Watch(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Watch.objects.filter(url__contains=t2))==0:
                temp.save()
        else:
            print(t1,t2)

def upload_deep(soup):
    allmusic = soup.findAll('a', class_='yt-simple-endpoint style-scope yt-formatted-string')
    url1="https://music.youtube.com"
    for data in allmusic:
        t1=str(data.contents[0])
        t2=str(data.attrs['href'])
        if t2.find("playlist")!=-1 or t2.find("browse")!=-1:
            temp=Playlist(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Playlist.objects.filter(url__contains=t2))==0:
                temp.save()
                url=url1+"/"+t2
                driver = webdriver.Firefox()
                driver.get(url)
                time.sleep(2) 
                html = driver.page_source
                if url.find("music.youtube.com")!=-1:
                    soup = BeautifulSoup(html, features='html.parser')
                    upload_deep(soup)
                driver.close()
        elif t2.find("channel")!=-1:
            temp=Channel(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Channel.objects.filter(url__contains=t2))==0:
                temp.save()
        elif t2.find("watch")!=-1:
            temp=Watch(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Watch.objects.filter(url__contains=t2))==0:
                temp.save()
        else:
            print(t1,t2)
            
    allmusic = soup.findAll('a', class_='yt-simple-endpoint image-wrapper style-scope ytmusic-two-row-item-renderer')
    url1="https://music.youtube.com"

    for data in allmusic:
        t1=str(data.contents[0])
        t2=str(data.attrs['href'])
        if t2.find("playlist")!=-1 or t2.find("browse")!=-1:
            temp=Playlist(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Playlist.objects.filter(url__contains=t2))==0:
                temp.save()
        elif t2.find("channel")!=-1:
            temp=Channel(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Channel.objects.filter(url__contains=t2))==0:
                temp.save()
        elif t2.find("watch")!=-1:
            temp=Watch(url=url1+"/"+t2,name=t1,name2=t1.lower())
            if len(Watch.objects.filter(url__contains=t2))==0:
                temp.save()
        else:
            print(t1,t2)



def index(request):
    return render(request, 'app/index.html')


def upload_music(request):
    if request.method == 'POST':

        url=str(request._post['url_'])
        if url.find("music.youtube.com")!=-1:
            driver = webdriver.Firefox()
            driver.get(url)
            time.sleep(2) 
            html = driver.page_source
            soup = BeautifulSoup(html, features='html.parser')
            upload(soup)
    driver.close()
    return render(request, 'app/index.html')


def deep_upload_music(request):
    if request.method == 'POST':
        url=str(request._post['url_'])
        if url.find("music.youtube.com")!=-1:

            driver = webdriver.Firefox()
            driver.get(url)
            time.sleep(2) 
            html = driver.page_source
            soup = BeautifulSoup(html, features='html.parser')
            upload_deep(soup)
    driver.close()
    return render(request, 'app/index.html')

def search(request):
    if request.method == 'POST':
        name=str(request._post['name'])
        playlists = Playlist.objects.filter(name2__contains=name.lower())
        channels = Channel.objects.filter(name2__contains=name.lower())
        watches = Watch.objects.filter(name2__contains=name.lower())
        return render(request, 'app/base.html', {'playlists': playlists,'channels': channels,'watches': watches})
    return render(request, 'app/index.html')
        
def base(request):
    playlists = Playlist.objects.all()
    channels = Channel.objects.all()
    watches = Watch.objects.all()

    return render(request, 'app/base.html', {'playlists': playlists,'channels': channels,'watches': watches})