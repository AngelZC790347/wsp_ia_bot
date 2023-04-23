# wsp_ia_bot
Its a Whatsapp bot with ia 
## Deployment

Using enviroment

You need to activte a cloud service to forwarding your app
A  easy option is ngrok , you install with tihs comand
in linux
``` 
sudo tar xvzf ~/Downloads/ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
```
or macos
```
brew install ngrok/ngrok/ngrok
```
then you can run a forwarding serve app
```
ngrok http 8080
```
- [NGROOK ](https://ngrok.com/download)


set up enviroment variables in .env

```
python3 -m venv myvenv && pip3 install -r requirements.txt
```
or directly in local machine
```
pip3 install -r requirements.txt
```
define de input personality and name os if in config.py
finally run
```
python3 server.py
```

