import requests

url = "https://paste.c-net.org/"

def upload(content: str):
    headers = {"Content-Type": "text/plain"}
    response = requests.post(url, data=content, headers=headers)

    if response.status_code == 200:
      paste_url = response.text.strip()
      if paste_url.startswith("https://"):
        return paste_url
      else:
        raise Exception("Upload succeeded but no Location header returned")
    else:
        raise Exception(f"Upload failed with status {response.status_code}")