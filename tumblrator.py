import urllib.request
import json
import sys
import os
import re

def get_feed(user):
	url = "http://cloud.feedly.com/v3/streams/contents?streamId=feed/http://"
	url+= user
	url+= ".tumblr.com/rss&ranked=oldest"
	handle = urllib.request.urlopen(url)
	feed = handle.read()
	return feed

def get_media(url, savepath='.'):
	media_basename = url.split("/")[-1]
	print("=== Downloading {}".format(media_basename))
	urllib.request.urlretrieve(url, os.path.join(savepath,media_basename))

if __name__ == "__main__":
	feed_list = sys.argv[1:]

	for f_name in feed_list:
		print("Downloading feed: {}".format(f_name))
		try:
			os.mkdir(f_name)
		except FileExistsError:
			if not os.path.isdir(f_name):
				print("ERROR: Could not create directory {}".format(f_name))
				continue
			else:
				print("Directory {} already exists.".format(f_name))

		feed_json = get_feed(f_name)
		feed = json.loads(feed_json)
		with open(os.path.join(f_name, "feed.json"),"w") as f:
			f.write(json.dumps(feed, indent=4, sort_keys=True))

		print("Downloading media...")

		media = []
		for post in feed["items"]:
			if "visual" in post:
				visual_url = post["visual"]["url"]
				if "media.tumblr.com" in visual_url:
					if not visual_url in media:
						media.append(visual_url)

			for url in re.findall("http://[0-9]+.media.tumblr.com/[^\"]+",post["summary"]["content"]):
				if not url in media:
					media.append(url)

		for url in media:
			get_media(url, savepath=f_name)
