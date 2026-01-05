file_path="task_5_12_25_insagram\\Instagram_Analytics.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[r for r in reader]

# print(len(data))

# print first 5 row
row=data[:5]
# print(row)

# highest like count media type

media_like=[int(r.get("likes")) for r in data]

max_like=max(media_like)

highest_md_liked=[r.get("media_type") for r in data if max_like==int(r.get("likes"))]

# print(highest_md_liked)

# average share of photo

shares_photo=[int(r.get("shares")) for r in data if r.get("media_type")=="Photo"]

average=sum(shares_photo)/len(shares_photo)

# print(average)

#Find the average likes for each media type.
photo_like=[int(r.get("likes")) for r in data if r.get("media_type")=="Photo"]
reel_like=[int(r.get("likes")) for r in data if r.get("media_type")=="Reel"]
video_like=[int(r.get("likes")) for r in data if r.get("media_type")=="Video"]
Carousel_like=[int(r.get("likes")) for r in data if r.get("media_type")=="Carousel"]

avg_photo=sum(photo_like)/len(photo_like)
avg_reel=sum(reel_like)/len(reel_like)
avg_video=sum(video_like)/len(video_like)
avg_carousel=sum(Carousel_like)/len(Carousel_like)

# print("avg photos",avg_photo)
# print("avg reel",avg_reel)
# print("avg video",avg_video)
# print("avg carosel",avg_carousel)

#How many posts used more than 10 hashtags?

post_hastag=[r.get("media_type") for r in data if int(r.get("hashtags_count"))>10]

# print(post_hastag.count("Photo"))
# print(post_hastag.count("Reel"))
# print(post_hastag.count("Video"))

#Which media type has the highest number of comments?

comments=[int(r.get("comments")) for r in data ]

max_comment=max(comments)

md_hightcomment=[r.get("media_type") for r in data if max_comment==int(r.get("comments"))]

print(md_hightcomment)



