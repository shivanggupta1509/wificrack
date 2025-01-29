import requests

# URL to send the request
url = "http://192.168.1.1:8090/login.xml"

# Request data (parameters)
payload = {
    "mode": "191",
    "username": "Fgg",
    "password": "ghbzb",
    "a": "1738155857532",
    "producttype": "2"
}

# Sending the POST request
response = requests.post(url, data=payload)

# Print response status and content
print("Status Code:", response.status_code)
print("Response Text:", response.text)
