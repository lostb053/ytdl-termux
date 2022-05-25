<h1>A simple script that makes downloading videos from <i>YouTube</i> easier using <i>yt-dlp</i> and <i>spotify_dl</i></h1>

# Requirements
* Android device with Android version 7.0 or above
* [Termux](https://f-droid.org/en/packages/com.termux/)
* Python
* FFMPEG
* yt-dlp (pip package)
* spotify_dl (pip package)

# Installation
* Install [Termux](https://f-droid.org/en/packages/com.termux/) app from F-Droid (Do not use playstore version)
* For a better appeal/look on the app, install [Litmux](https://github.com/AvinashReddy3108/LitMux), simply follow the instructions
* If you opt for Litmux, after running the installation cmd, exit the app by entering exit command, twice if it doesn't closes app after single try. You may later be prompt to setup Litmux, just answer the questions asked
* Run the following command and wait till it's completed
```
bash -c "$(curl -fsSL https://bit.ly/install-ytdl-termux)"
```
<h3>Note: You don't need to go out of your way to install python, ffmpeg, etc on termux. The script installs everything</h3>

# Usage

USAGE:  ytdl [OPTIONS]
```
ytdl        invokes the function, no required options
-u          option to update this program
-h          to print this help message
-q          quiet mode, will show no progress, download quietly
-a link     to download audio, no playlist links
-b link     download best video (with in-built audio) available, no playlist links
-s link     download audio from youtube using metadata from any spotify link
```
This command separately downloads best video and best audio available and merges them
use -b option to download video with in-built audio and avoid merging
-s option supports spotify track, playlist, album and artist urls
Options -a, -b, -s require link

<br>
<a href="https://bit.ly/ytdl-sample-vid">ytdl plugin in action</a>
