# importing the reques ts library
import requests

# defining the api-endpoint
API_ENDPOINT =  "http://4533-115-119-250-30.ngrok.io/train"
# data to be sent to api
data = {
    "url": "https://github.com/yashtest11111/yash4demo.git",
    "branch_name": "master",
    "user_name": "yash4@gmail.com"
}
# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=data)
# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s" % pastebin_url)
