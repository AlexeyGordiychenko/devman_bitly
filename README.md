# Bitly URL shortener


Shorten the given URL or count clicks if the given URL is a short URL

```
usage: main.py [-h] link

positional arguments:
  link        link
```
If the given URL is a biltly link then the program will display the number of clicks for it.

If it's not a bitly link then the program will try to shorten it with bitly API. After that the program will display the short link for you to use.

Example:
```
python main.py https://github.com
```
### How to install

#### Create your token

In order to get a token you need to create an account at [bitly](https://app.bitly.com/). Then you need to create your token. More info at [article](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-)

Example of a token:
```
17c09e20ad155405123ac1977542fecf00231da7
```
To use the token for the program, you need to add it as environment variable 'BITLY_TOKEN':
>   1. Add file '.env' to the root directory
>   2. Add line
>   ```
>   BITLY_TOKEN=[your token]
>   ```
>   For example:
>   ```
>   BITLY_TOKEN=17c09e20ad155405123ac1977542fecf00231da7
>   ```

#### Install dependencies

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
