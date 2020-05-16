import requests

def get(email, key):
    return requests.get(
        f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
        headers={"hibp-api-key": key}  
    )
    