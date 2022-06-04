from django.shortcuts import render
from pytube import YouTube
from youtubesearchpython import VideosSearch
from youtube_downloader.settings import SITE_NAME
import datetime

# Create your views here.
def download(request):
    
    # Youtube Download Videos
    if request.method == "GET":

        q = request.GET.get('q')
        try:
            yt = YouTube(q) # check if video is not valid url
            valid_video_url = True
        except:
            valid_video_url = False
        
        
        if valid_video_url:
            title = yt.title
            thumbnail_url = yt.thumbnail_url
            channel_name =  yt.author
            video_length_seconds = yt.length

            def video_length(seconds):
                convert = str(datetime.timedelta(seconds = seconds))
                return convert
            
            length = video_length(video_length_seconds)
            

            streams = yt.streams
            video_1080p = streams.filter(file_extension="mp4", res="1080p").first()
            video_720p = streams.filter(file_extension="mp4", progressive="True", res="720p").first()
            video_480p = streams.filter(file_extension="mp4", progressive="True", res="480p").first()
            video_360p = streams.filter(file_extension="mp4", progressive="True", res="360p").first()
            video_240p = streams.filter(file_extension="mp4", progressive="True", res="240p").first()
            video_144p = streams.filter(file_extension="mp4", progressive="True", res="144p").first()
            mp3 = streams.filter(type="audio").first()
            
            res = {
                
                # MP4
                "mp4_1080p_res": video_1080p,
                "mp4_720p_mp4_res": video_720p,
                "mp4_480p_mp4_res": video_480p,
                "mp4_360p_mp4_res": video_360p,
                "mp4_240p_mp4_res": video_240p,
                "mp4_144p_mp4_res": video_144p,
                # MP3
                "mp3_res": mp3,
            }


            res_filterd = {}
            
            for x in res:
                if res[x] is not None:
                    res[x] = res[x].url
                    res_filterd[x] = res[x]
                else:
                    res[x] = None
                    res_filterd[x] = res[x]
                    
            
            context = {
                'title':title,
                'thumbnail_url': thumbnail_url,
                'channel_name': channel_name,
                'video_length': length,
                'res_filterd': res_filterd,
                "site_name":SITE_NAME,


            }

            return render(request, 'download_url.html', context)
        
        # Youtube Search Videos
        else:
            q = request.GET.get('q')
            videosSearch = VideosSearch(q).result()['result']
            search_results = []
            for i in videosSearch:
                title = i['title']
                link  = i['link']
                image = i['thumbnails'][-1]['url']
                
                list = {'title': title, 'link': link, 'image': image}
                
                search_results.append(list)

            context = {
                'search_results': search_results,
                'q':q,
                "site_name":SITE_NAME,
            }
            return render(request, 'download_search.html', context)
        
        
def home(request):
    return render(request, 'home.html', {"site_name":SITE_NAME,})

def ContactUs(request):
    return render(request, 'contact_us.html', {"site_name":SITE_NAME,})

def PrivayPolicy(request):
    return render(request, 'privacy-policy.html', {"site_name":SITE_NAME,})

def TermsOfService(request):
    return render(request, 'terms-of-service.html', {"site_name":SITE_NAME,}) 