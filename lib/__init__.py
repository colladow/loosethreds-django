import urlparse, urllib2
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

def download_gif(url):
    parsed = urlparse.urlparse(url)

    name = parsed.path.split('/')[-1]

    temp_image = NamedTemporaryFile(delete=True)
    temp_image.write(urllib2.urlopen(parsed.geturl()).read())
    temp_image.flush()

    return name, File(temp_image)
