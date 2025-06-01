# Task Options Documentation

This page details the various command-line options available for tasks.

## General Task Options

### New Name

`-new` (Example command part)

**New Name**: -n

/cmd link -n new name
Note: Doesn't work with torrents

---
### Multi-Link

`-multi` (Example command part)

**Multi links only by replying to first link/file**: -i

/cmd -i 10(number of links/files)

---
### Same Directory

`-same` (Example command part)

**Move file(s)/folder(s) to new folder**: -m

You can use this arg also to move multiple links/torrents contents to the same directory, so all links will be uploaded together as one task

/cmd link -m new folder (only one link inside new folder)
/cmd -i 10(number of links/files) -m folder name (all links contents in one folder)
/cmd -b -m folder name (reply to batch of message/file(each link on new line))

While using bulk you can also use this arg with different folder name along with the links in message or file batch
Example:
link1 -m folder1
link2 -m folder1
link3 -m folder2
link4 -m folder2
link5 -m folder3
link6
so link1 and link2 content will be uploaded from same folder which is folder1
link3 and link4 content will be uploaded from same folder also which is folder2
link5 will uploaded alone inside new folder named folder3
link6 will get uploaded normally alone

---
### Thumbnail

`-thumb` (Example command part)

**Thumbnail for current task**: -t

/cmd link -t tg-message-link (doc or photo) or none (file without thumb)

---
### Split Size

`-split` (Example command part)

**Split size for current task**: -sp

/cmd link -sp (500mb or 2gb or 4000000000)
Note: Only mb and gb are supported or write in bytes without unit!

---
### Upload Destination

`-upload` (Example command part)

**Upload Destination**: -up

/cmd link -up rcl/gdl (rcl: to select rclone config, remote & path | gdl: To select token.pickle, gdrive id) using buttons
You can directly add the upload path: -up remote:dir/subdir or -up Gdrive_id or -up id/username (telegram) or -up id/username|topic_id (telegram)
If DEFAULT_UPLOAD is `rc` then you can pass up: `gd` to upload using gdrive tools to GDRIVE_ID.
If DEFAULT_UPLOAD is `gd` then you can pass up: `rc` to upload to RCLONE_PATH.

If you want to add path or gdrive manually from your config/token (UPLOADED FROM USETTING) add mrcc: for rclone and mtp: before the path/gdrive_id without space.
/cmd link -up mrcc:main:dump or -up mtp:gdrive_id <strong>or you can simply edit upload using owner/user token/config from usetting without adding mtp: or mrcc: before the upload path/id</strong>

To add leech destination:
-up id/@username/pm
-up b:id/@username/pm (b: means leech by bot) (id or username of the chat or write pm means private message so bot will send the files in private to you)
when you should use b:(leech by bot)? When your default settings is leech by user and you want to leech by bot for specific task.
-up u:id/@username(u: means leech by user) This incase OWNER added USER_SESSION_STRING.
-up h:id/@username(hybrid leech) h: to upload files by bot and user based on file size.
-up id/@username|topic_id(leech in specific chat and topic) add | without space and write topic id after chat id or username.

In case you want to specify whether using token.pickle or service accounts you can add tp:gdrive_id (using token.pickle) or sa:gdrive_id (using service accounts) or mtp:gdrive_id (using token.pickle uploaded from usetting).
DEFAULT_UPLOAD doesn't affect on leech cmds.

---
### Rclone Flags

`-rcf` (Example command part)

**Rclone Flags**: -rcf

/cmd link|path|rcl -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
This will override all other flags except --exclude
Check here all [RcloneFlags](https://rclone.org/flags/).

---
### Extract/Zip

`-extract` (Example command part)

**Extract/Zip**: -e -z

/cmd link -e password (extract password protected)
/cmd link -z password (zip password protected)
/cmd link -z password -e (extract and zip password protected)
Note: When both extract and zip added with cmd it will extract first and then zip, so always extract first

---
### Join Splitted Files

`-join` (Example command part)

**Join Splitted Files**: -j

This option will only work before extract and zip, so mostly it will be used with -m argument (samedir)
By Reply:
/cmd -i 3 -j -m folder name
/cmd -b -j -m folder name
if u have link(folder) have splitted files:
/cmd link -j

---
### Sample Video

`-sample` (Example command part)

**Sample Video**: -sv

Create sample video for one video or folder of videos.
/cmd -sv (it will take the default values which 60sec sample duration and part duration is 4sec).
You can control those values. Example: /cmd -sv 70:5(sample-duration:part-duration) or /cmd -sv :5 or /cmd -sv 70.

---
### Screenshots

`-screenshot` (Example command part)

**ScreenShots**: -ss

Create screenshots for one video or folder of videos.
/cmd -ss (it will take the default values which is 10 photos).
You can control this value. Example: /cmd -ss 6.

---
### Bittorrent Seed

`-seed` (Example command part)

**Bittorrent seed**: -d

/cmd link -d ratio:seed_time or by replying to file/link
To specify ratio and seed time add -d ratio:time.
Example: -d 0.7:10 (ratio and time) or -d 0.7 (only ratio) or -d :10 (only time) where time in minutes

---
### Quality Buttons (YT-DLP)

`-qual` (Example command part)

**Quality Buttons**: -s

In case default quality added from yt-dlp options using format option and you need to select quality for specific link or links with multi links feature.
/cmd link -s

---
### Convert Media

`-convert` (Example command part)

**Convert Media**: -ca -cv
/cmd link -ca mp3 -cv mp4 (convert all audios to mp3 and all videos to mp4)
/cmd link -ca mp3 (convert all audios to mp3)
/cmd link -cv mp4 (convert all videos to mp4)
/cmd link -ca mp3 + flac ogg (convert only flac and ogg audios to mp3)
/cmd link -cv mkv - webm flv (convert all videos to mp4 except webm and flv)

---
### Force Start

`-force` (Example command part)

**Force Start**: -f -fd -fu
/cmd link -f (force download and upload)
/cmd link -fd (force download only)
/cmd link -fu (force upload directly after download finish)

---
### Name Substitution

Content not found for `name_sub`.

---
### TG Transmission

`-transmission` (Example command part)

**Tg transmission**: -hl -ut -bt
/cmd link -hl (leech by user and bot session with respect to size) (Hybrid Leech)
/cmd link -bt (leech by bot session)
/cmd link -ut (leech by user)

---
### Thumbnail Layout

`-thumbnail` (Example command part)

Thumbnail Layout: -tl
/cmd link -tl 3x3 (widthxheight) 3 photos in row and 3 photos in column

---
### Leech As Document/Media

`-leech` (Example command part)

**Leech as**: -doc -med
/cmd link -doc (Leech as document)
/cmd link -med (Leech as media)

---
### FFmpeg Commands

`-ffmpeg` (Example command part)

**FFmpeg Commands**: -ff
list of lists of ffmpeg commands. You can set multiple ffmpeg commands for all files before upload. Don't write ffmpeg at beginning, start directly with the arguments.
Notes:
1. Add `-del` to the list(s) which you want from the bot to delete the original files after command run complete!
2. To execute one of pre-added lists in bot like: ({"subtitle": ["-i mltb.mkv -c copy -c:s srt mltb.mkv"]}), you must use -ff subtitle (list key)
Examples: ["-i mltb.mkv -c copy -c:s srt mltb.mkv", "-i mltb.video -c copy -c:s srt mltb", "-i mltb.m4a -c:a libmp3lame -q:a 2 mltb.mp3", "-i mltb.audio -c:a libmp3lame -q:a 2 mltb.mp3", "-i mltb -map 0:a -c copy mltb.mka -map 0:s -c copy mltb.srt", "-i mltb -i tg://openmessage?user_id=5272663208&message_id=322801 -filter_complex 'overlay=W-w-10:H-h-10' -c:a copy mltb"]
Here I will explain how to use mltb.* which is reference to files you want to work on.
1. First cmd: the input is mltb.mkv so this cmd will work only on mkv videos and the output is mltb.mkv also so all outputs is mkv. -del will delete the original media after complete run of the cmd.
2. Second cmd: the input is mltb.video so this cmd will work on all videos and the output is only mltb so the extenstion is same as input files.
3. Third cmd: the input in mltb.m4a so this cmd will work only on m4a audios and the output is mltb.mp3 so the output extension is mp3.
4. Fourth cmd: the input is mltb.audio so this cmd will work on all audios and the output is mltb.mp3 so the output extension is mp3.
5. Fifth cmd: You can add telegram link for small size input like photo to set watermark

---

## YT-DLP Specific Options

### main

**Send link along with command line**:

/cmd link
**By replying to link**:
/cmd -n new name -z password -opt x:y|x1:y1

Check here all supported [SITES](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
Check all yt-dlp api options from this [FILE](https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L212) or use this [script](https://t.me/mltb_official_channel/177) to convert cli arguments to api options.

---
### New Name

**New Name**: -n

/cmd link -n new name
Note: Doesn't work with torrents
Note: Don't add file extension

---
### Zip

**Zip**: -z password

/cmd link -z (zip)
/cmd link -z password (zip password protected)

---
### Quality

**Quality Buttons**: -s

In case default quality added from yt-dlp options using format option and you need to select quality for specific link or links with multi links feature.
/cmd link -s

---
### Options

**Options**: -opt

/cmd link -opt {"format": "bv*+mergeall[vcodec=none]", "nocheckcertificate": True, "playliststart": 10, "fragment_retries": float("inf"), "matchtitle": "S13", "writesubtitles": True, "live_from_start": True, "postprocessor_args": {"ffmpeg": ["-threads", "4"]}, "wait_for_video": (5, 100), "download_ranges": [{"start_time": 0, "end_time": 10}]}
Check all yt-dlp api options from this [FILE](https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184) or use this [script](https://t.me/mltb_official_channel/177) to convert cli arguments to api options.

---
### Multi Link

**Multi links only by replying to first link/file**: -i

/cmd -i 10(number of links/files)

---
### Same Directory

**Move file(s)/folder(s) to new folder**: -m

You can use this arg also to move multiple links/torrents contents to the same directory, so all links will be uploaded together as one task

/cmd link -m new folder (only one link inside new folder)
/cmd -i 10(number of links/files) -m folder name (all links contents in one folder)
/cmd -b -m folder name (reply to batch of message/file(each link on new line))

While using bulk you can also use this arg with different folder name along with the links in message or file batch
Example:
link1 -m folder1
link2 -m folder1
link3 -m folder2
link4 -m folder2
link5 -m folder3
link6
so link1 and link2 content will be uploaded from same folder which is folder1
link3 and link4 content will be uploaded from same folder also which is folder2
link5 will uploaded alone inside new folder named folder3
link6 will get uploaded normally alone

---
### Thumb

**Thumbnail for current task**: -t

/cmd link -t tg-message-link (doc or photo) or none (file without thumb)

---
### Split Size

**Split size for current task**: -sp

/cmd link -sp (500mb or 2gb or 4000000000)
Note: Only mb and gb are supported or write in bytes without unit!

---
### Upload Destination

**Upload Destination**: -up

/cmd link -up rcl/gdl (rcl: to select rclone config, remote & path | gdl: To select token.pickle, gdrive id) using buttons
You can directly add the upload path: -up remote:dir/subdir or -up Gdrive_id or -up id/username (telegram) or -up id/username|topic_id (telegram)
If DEFAULT_UPLOAD is `rc` then you can pass up: `gd` to upload using gdrive tools to GDRIVE_ID.
If DEFAULT_UPLOAD is `gd` then you can pass up: `rc` to upload to RCLONE_PATH.

If you want to add path or gdrive manually from your config/token (UPLOADED FROM USETTING) add mrcc: for rclone and mtp: before the path/gdrive_id without space.
/cmd link -up mrcc:main:dump or -up mtp:gdrive_id <strong>or you can simply edit upload using owner/user token/config from usetting without adding mtp: or mrcc: before the upload path/id</strong>

To add leech destination:
-up id/@username/pm
-up b:id/@username/pm (b: means leech by bot) (id or username of the chat or write pm means private message so bot will send the files in private to you)
when you should use b:(leech by bot)? When your default settings is leech by user and you want to leech by bot for specific task.
-up u:id/@username(u: means leech by user) This incase OWNER added USER_SESSION_STRING.
-up h:id/@username(hybrid leech) h: to upload files by bot and user based on file size.
-up id/@username|topic_id(leech in specific chat and topic) add | without space and write topic id after chat id or username.

In case you want to specify whether using token.pickle or service accounts you can add tp:gdrive_id (using token.pickle) or sa:gdrive_id (using service accounts) or mtp:gdrive_id (using token.pickle uploaded from usetting).
DEFAULT_UPLOAD doesn't affect on leech cmds.

---
### Rclone Flags

**Rclone Flags**: -rcf

/cmd link|path|rcl -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
This will override all other flags except --exclude
Check here all [RcloneFlags](https://rclone.org/flags/).

---
### Bulk

**Bulk Download**: -b

Bulk can be used only by replying to text message or text file contains links separated by new line.
Example:
link1 -n new name -up remote1:path1 -rcf |key:value|key:value
link2 -z -n new name -up remote2:path2
link3 -e -n new name -up remote2:path2
Reply to this example by this cmd -> /cmd -b(bulk)

Note: Any arg along with the cmd will be setted to all links
/cmd -b -up remote: -z -m folder name (all links contents in one zipped folder uploaded to one destination)
so you can't set different upload destinations along with link incase you have added -m along with cmd
You can set start and end of the links from the bulk like seed, with -b start:end or only end by -b :end or only start by -b start.
The default start is from zero(first link) to inf.

---
### Sample Video

**Sample Video**: -sv

Create sample video for one video or folder of videos.
/cmd -sv (it will take the default values which 60sec sample duration and part duration is 4sec).
You can control those values. Example: /cmd -sv 70:5(sample-duration:part-duration) or /cmd -sv :5 or /cmd -sv 70.

---
### Screenshot

**ScreenShots**: -ss

Create screenshots for one video or folder of videos.
/cmd -ss (it will take the default values which is 10 photos).
You can control this value. Example: /cmd -ss 6.

---
### Convert Media

**Convert Media**: -ca -cv
/cmd link -ca mp3 -cv mp4 (convert all audios to mp3 and all videos to mp4)
/cmd link -ca mp3 (convert all audios to mp3)
/cmd link -cv mp4 (convert all videos to mp4)
/cmd link -ca mp3 + flac ogg (convert only flac and ogg audios to mp3)
/cmd link -cv mkv - webm flv (convert all videos to mp4 except webm and flv)

---
### Force Start

**Force Start**: -f -fd -fu
/cmd link -f (force download and upload)
/cmd link -fd (force download only)
/cmd link -fu (force upload directly after download finish)

---
### Name Substitute

Content not found

---
### TG Transmission

**Tg transmission**: -hl -ut -bt
/cmd link -hl (leech by user and bot session with respect to size) (Hybrid Leech)
/cmd link -bt (leech by bot session)
/cmd link -ut (leech by user)

---
### Thumb Layout

Thumbnail Layout: -tl
/cmd link -tl 3x3 (widthxheight) 3 photos in row and 3 photos in column

---
### Leech Type

**Leech as**: -doc -med
/cmd link -doc (Leech as document)
/cmd link -med (Leech as media)

---
### FFmpeg Cmds

**FFmpeg Commands**: -ff
list of lists of ffmpeg commands. You can set multiple ffmpeg commands for all files before upload. Don't write ffmpeg at beginning, start directly with the arguments.
Notes:
1. Add `-del` to the list(s) which you want from the bot to delete the original files after command run complete!
2. To execute one of pre-added lists in bot like: ({"subtitle": ["-i mltb.mkv -c copy -c:s srt mltb.mkv"]}), you must use -ff subtitle (list key)
Examples: ["-i mltb.mkv -c copy -c:s srt mltb.mkv", "-i mltb.video -c copy -c:s srt mltb", "-i mltb.m4a -c:a libmp3lame -q:a 2 mltb.mp3", "-i mltb.audio -c:a libmp3lame -q:a 2 mltb.mp3", "-i mltb -map 0:a -c copy mltb.mka -map 0:s -c copy mltb.srt", "-i mltb -i tg://openmessage?user_id=5272663208&message_id=322801 -filter_complex 'overlay=W-w-10:H-h-10' -c:a copy mltb"]
Here I will explain how to use mltb.* which is reference to files you want to work on.
1. First cmd: the input is mltb.mkv so this cmd will work only on mkv videos and the output is mltb.mkv also so all outputs is mkv. -del will delete the original media after complete run of the cmd.
2. Second cmd: the input is mltb.video so this cmd will work on all videos and the output is only mltb so the extenstion is same as input files.
3. Third cmd: the input in mltb.m4a so this cmd will work only on m4a audios and the output is mltb.mp3 so the output extension is mp3.
4. Fourth cmd: the input is mltb.audio so this cmd will work on all audios and the output is mltb.mp3 so the output extension is mp3.
5. Fifth cmd: You can add telegram link for small size input like photo to set watermark

---

## Mirror Specific Options

### main

**Send link along with command line or **

/cmd link

**By replying to link/file**:

/cmd -n new name -e -up upload destination

**NOTE:**
1. Commands that start with **qb** are ONLY for torrents.

---
### New Name

**New Name**: -n

/cmd link -n new name
Note: Doesn't work with torrents

---
### DL Auth

**Direct link authorization**: -au -ap

/cmd link -au username -ap password

---
### Headers

**Direct link custom headers**: -h

/cmd link -h key:value|key1:value1

---
### Extract/Zip

**Extract/Zip**: -e -z

/cmd link -e password (extract password protected)
/cmd link -z password (zip password protected)
/cmd link -z password -e (extract and zip password protected)
Note: When both extract and zip added with cmd it will extract first and then zip, so always extract first

---
### Select Files

**Bittorrent/JDownloader/Sabnzbd File Selection**: -s

/cmd link -s or by replying to file/link

---
### Torrent Seed

**Bittorrent seed**: -d

/cmd link -d ratio:seed_time or by replying to file/link
To specify ratio and seed time add -d ratio:time.
Example: -d 0.7:10 (ratio and time) or -d 0.7 (only ratio) or -d :10 (only time) where time in minutes

---
### Multi Link

**Multi links only by replying to first link/file**: -i

/cmd -i 10(number of links/files)

---
### Same Directory

**Move file(s)/folder(s) to new folder**: -m

You can use this arg also to move multiple links/torrents contents to the same directory, so all links will be uploaded together as one task

/cmd link -m new folder (only one link inside new folder)
/cmd -i 10(number of links/files) -m folder name (all links contents in one folder)
/cmd -b -m folder name (reply to batch of message/file(each link on new line))

While using bulk you can also use this arg with different folder name along with the links in message or file batch
Example:
link1 -m folder1
link2 -m folder1
link3 -m folder2
link4 -m folder2
link5 -m folder3
link6
so link1 and link2 content will be uploaded from same folder which is folder1
link3 and link4 content will be uploaded from same folder also which is folder2
link5 will uploaded alone inside new folder named folder3
link6 will get uploaded normally alone

---
### Thumb

**Thumbnail for current task**: -t

/cmd link -t tg-message-link (doc or photo) or none (file without thumb)

---
### Split Size

**Split size for current task**: -sp

/cmd link -sp (500mb or 2gb or 4000000000)
Note: Only mb and gb are supported or write in bytes without unit!

---
### Upload Destination

**Upload Destination**: -up

/cmd link -up rcl/gdl (rcl: to select rclone config, remote & path | gdl: To select token.pickle, gdrive id) using buttons
You can directly add the upload path: -up remote:dir/subdir or -up Gdrive_id or -up id/username (telegram) or -up id/username|topic_id (telegram)
If DEFAULT_UPLOAD is `rc` then you can pass up: `gd` to upload using gdrive tools to GDRIVE_ID.
If DEFAULT_UPLOAD is `gd` then you can pass up: `rc` to upload to RCLONE_PATH.

If you want to add path or gdrive manually from your config/token (UPLOADED FROM USETTING) add mrcc: for rclone and mtp: before the path/gdrive_id without space.
/cmd link -up mrcc:main:dump or -up mtp:gdrive_id <strong>or you can simply edit upload using owner/user token/config from usetting without adding mtp: or mrcc: before the upload path/id</strong>

To add leech destination:
-up id/@username/pm
-up b:id/@username/pm (b: means leech by bot) (id or username of the chat or write pm means private message so bot will send the files in private to you)
when you should use b:(leech by bot)? When your default settings is leech by user and you want to leech by bot for specific task.
-up u:id/@username(u: means leech by user) This incase OWNER added USER_SESSION_STRING.
-up h:id/@username(hybrid leech) h: to upload files by bot and user based on file size.
-up id/@username|topic_id(leech in specific chat and topic) add | without space and write topic id after chat id or username.

In case you want to specify whether using token.pickle or service accounts you can add tp:gdrive_id (using token.pickle) or sa:gdrive_id (using service accounts) or mtp:gdrive_id (using token.pickle uploaded from usetting).
DEFAULT_UPLOAD doesn't affect on leech cmds.

---
### Rclone Flags

**Rclone Flags**: -rcf

/cmd link|path|rcl -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
This will override all other flags except --exclude
Check here all [RcloneFlags](https://rclone.org/flags/).

---
### Bulk

**Bulk Download**: -b

Bulk can be used only by replying to text message or text file contains links separated by new line.
Example:
link1 -n new name -up remote1:path1 -rcf |key:value|key:value
link2 -z -n new name -up remote2:path2
link3 -e -n new name -up remote2:path2
Reply to this example by this cmd -> /cmd -b(bulk)

Note: Any arg along with the cmd will be setted to all links
/cmd -b -up remote: -z -m folder name (all links contents in one zipped folder uploaded to one destination)
so you can't set different upload destinations along with link incase you have added -m along with cmd
You can set start and end of the links from the bulk like seed, with -b start:end or only end by -b :end or only start by -b start.
The default start is from zero(first link) to inf.

---
### Join

**Join Splitted Files**: -j

This option will only work before extract and zip, so mostly it will be used with -m argument (samedir)
By Reply:
/cmd -i 3 -j -m folder name
/cmd -b -j -m folder name
if u have link(folder) have splitted files:
/cmd link -j

---
### Rclone DL

**Rclone Download**:

Treat rclone paths exactly like links
/cmd main:dump/ubuntu.iso or rcl(To select config, remote and path)
Users can add their own rclone from user settings
If you want to add path manually from your config add mrcc: before the path without space
/cmd mrcc:main:dump/ubuntu.iso
You can simply edit using owner/user config from usetting without adding mrcc: before the path

---
### Tg Links

**TG Links**:

Treat links like any direct link
Some links need user access so you must add USER_SESSION_STRING for it.
Three types of links:
Public: https://t.me/channel_name/message_id
Private: tg://openmessage?user_id=xxxxxx&message_id=xxxxx
Super: https://t.me/c/channel_id/message_id
Range: https://t.me/channel_name/first_message_id-last_message_id
Range Example: tg://openmessage?user_id=xxxxxx&message_id=555-560 or https://t.me/channel_name/100-150
Note: Range link will work only by replying cmd to it

---
### Sample Video

**Sample Video**: -sv

Create sample video for one video or folder of videos.
/cmd -sv (it will take the default values which 60sec sample duration and part duration is 4sec).
You can control those values. Example: /cmd -sv 70:5(sample-duration:part-duration) or /cmd -sv :5 or /cmd -sv 70.

---
### Screenshot

**ScreenShots**: -ss

Create screenshots for one video or folder of videos.
/cmd -ss (it will take the default values which is 10 photos).
You can control this value. Example: /cmd -ss 6.

---
### Convert Media

**Convert Media**: -ca -cv
/cmd link -ca mp3 -cv mp4 (convert all audios to mp3 and all videos to mp4)
/cmd link -ca mp3 (convert all audios to mp3)
/cmd link -cv mp4 (convert all videos to mp4)
/cmd link -ca mp3 + flac ogg (convert only flac and ogg audios to mp3)
/cmd link -cv mkv - webm flv (convert all videos to mp4 except webm and flv)

---
### Force Start

**Force Start**: -f -fd -fu
/cmd link -f (force download and upload)
/cmd link -fd (force download only)
/cmd link -fu (force upload directly after download finish)

---
### User Download

**User Download**: link

/cmd tp:link to download using owner token.pickle incase service account enabled.
/cmd sa:link to download using service account incase service account disabled.
/cmd tp:gdrive_id to download using token.pickle and file_id incase service account enabled.
/cmd sa:gdrive_id to download using service account and file_id incase service account disabled.
/cmd mtp:gdrive_id or mtp:link to download using user token.pickle uploaded from usetting
/cmd mrcc:remote:path to download using user rclone config uploaded from usetting
you can simply edit upload using owner/user token/config from usetting without adding mtp: or mrcc: before the path/id

---
### Name Substitute

Content not found

---
### TG Transmission

**Tg transmission**: -hl -ut -bt
/cmd link -hl (leech by user and bot session with respect to size) (Hybrid Leech)
/cmd link -bt (leech by bot session)
/cmd link -ut (leech by user)

---
### Thumb Layout

Thumbnail Layout: -tl
/cmd link -tl 3x3 (widthxheight) 3 photos in row and 3 photos in column

---
### Leech Type

**Leech as**: -doc -med
/cmd link -doc (Leech as document)
/cmd link -med (Leech as media)

---
### FFmpeg Cmds

**FFmpeg Commands**: -ff
list of lists of ffmpeg commands. You can set multiple ffmpeg commands for all files before upload. Don't write ffmpeg at beginning, start directly with the arguments.
Notes:
1. Add `-del` to the list(s) which you want from the bot to delete the original files after command run complete!
2. To execute one of pre-added lists in bot like: ({"subtitle": ["-i mltb.mkv -c copy -c:s srt mltb.mkv"]}), you must use -ff subtitle (list key)
Examples: ["-i mltb.mkv -c copy -c:s srt mltb.mkv", "-i mltb.video -c copy -c:s srt mltb", "-i mltb.m4a -c:a libmp3lame -q:a 2 mltb.mp3", "-i mltb.audio -c:a libmp3lame -q:a 2 mltb.mp3", "-i mltb -map 0:a -c copy mltb.mka -map 0:s -c copy mltb.srt", "-i mltb -i tg://openmessage?user_id=5272663208&message_id=322801 -filter_complex 'overlay=W-w-10:H-h-10' -c:a copy mltb"]
Here I will explain how to use mltb.* which is reference to files you want to work on.
1. First cmd: the input is mltb.mkv so this cmd will work only on mkv videos and the output is mltb.mkv also so all outputs is mkv. -del will delete the original media after complete run of the cmd.
2. Second cmd: the input is mltb.video so this cmd will work on all videos and the output is only mltb so the extenstion is same as input files.
3. Third cmd: the input in mltb.m4a so this cmd will work only on m4a audios and the output is mltb.mp3 so the output extension is mp3.
4. Fourth cmd: the input is mltb.audio so this cmd will work on all audios and the output is mltb.mp3 so the output extension is mp3.
5. Fifth cmd: You can add telegram link for small size input like photo to set watermark

---
