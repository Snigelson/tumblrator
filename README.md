## Tumblrator - download tumblr feeds

This script gets feeds from Feedly and saves it as a json. It also 
extracts URLs pointing to tumblr's CDN (*.media.tumblr.com) and tries to 
download those.


## Requirements

Python3


## Usage

Run `python tumblrator.py <feed name>`. You can supply any number of 
feeds in one go, and they will be downloaded sequentially.

Example: `python tumblrator.py probertson`

A drirectory named "&lt;feed name&gt;" should be created. In that direcory, the feed will be saved as `feed.json` along with any (see below) media files.


## Caveats

1. I have not bug tested this software like at all.

2. Only media stored on tumblr's CDN will be downloaded.
External media will not be downloaded.

3. I have only yet tested this software on Linux.

4. No pretty formatting is done. It would probably be easy for someone
with the know-how to parse the JSON into a nice HTML presentation.

5. I am not sure it extracts all media. If it doesn't, please create
an issue where you supply the name of the feed and the media which
is not downloaded. Thank you!
