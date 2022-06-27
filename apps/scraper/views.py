from django.http import HttpResponse
from django.shortcuts import render
from apps.scraper.beautiful_soup import scraper
from apps.scraper.form import ScraperInputForm
from apps.scraper.models import Keyword, Url
from django.contrib import messages

# Create your views here.


def data_handler(datas):
    websites = set()
    data_website = {}
    for data in datas:
        data_website.setdefault(data.url.url, []).append(data.keyword)
        if len(data_website[data.url.url]) >= 3:
            websites.add(data.url)
    return websites


def scrap(request):
    form = ScraperInputForm()
    context = {'form': form}
    if request.method == 'POST':
        try:
            url = Url.objects.get(url=request.POST['url'])
            datas = Keyword.objects.filter(url=url)
            keywords = []
            for data in datas:
                keywords.append(data.keyword)
            context['keywords'] = keywords
            datas = Keyword.objects.filter(
                keyword__in=keywords).exclude(url=url)
            websites = data_handler(datas)
            context['websites'] = websites
        except:
            url = Url.objects.create(url=request.POST['url'])
            try:
                keywords = scraper(request.POST['url'])
                for keyword in keywords:
                    Keyword.objects.create(url=url, keyword=keyword)
                context['keywords'] = keywords
                datas = Keyword.objects.filter(
                    keyword__in=keywords).exclude(url=url)
                websites = data_handler(datas)
                context['websites'] = websites
            except:
                messages.error(request, 'no keywords found')

    return render(request, 'index.html', context)
