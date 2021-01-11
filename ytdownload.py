from pytube import YouTube

link = input("Enter the link: ")
yt =YouTube(link)

#Save_Path = r"Pytube_Project"

#showing details
#Title of video
#print("Title: ",yt.title)
#Number of views of video
#print("Number of views: ",yt.views)
#Length of the video
#print("Length of video: ",yt.length,"seconds")
#Description of video
#print("Description: ",yt.description)
#Rating
#print("Ratings: ",yt.rating)

#printing all the available streams
#print(yt.streams)
#printing audio-only streams
#print(yt.streams.filter(only_audio=True))
#printng video-only streams
#print(yt.streams.filter(only_video=True))
#ys = yt.streams.get_by_itag('22')

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

print('Downloading...')
ys.download(r"Pytube_Project")#or Save_Path 
print('Download Completed')



#from pytube import YouTube
#YouTube('https://youtu.be/-dJdMNCzPFQ').streams.get_highest_resolution().download(r'C:\Users\Ujala\Downloads')
