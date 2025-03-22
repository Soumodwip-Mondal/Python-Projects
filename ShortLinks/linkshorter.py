import pyshorteners
url='https://github.com/Soumodwip-Mondal?tab=repositories'
#Short your URL
def short_url(url):
    s=pyshorteners.Shortener()
    short_url=s.tinyurl.short(url)
    return short_url
#Get original url form shorted url
def get_url(url):
    s=pyshorteners.Shortener()
    original_url=s.tinyurl.expand(url)
    return original_url
print(short_url(url))
print(get_url(short_url(url)))