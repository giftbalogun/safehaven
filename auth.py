import jwt
import time
import requests

# Paste your private key within the space as it is.
private_key = """
-----BEGIN PRIVATE KEY-----

-----END PRIVATE KEY-----
"""

def generate_and_print_token():
    company_url = "https://royalbv.name.ng" # add your company URL same as what is on SafeHaven
    oauth_client_id = "" # add your client generated id
    safe_haven_environment = "https://api.sandbox.safehavenmfb.com" # use the right url for your safehaven enrironment
    issued_at = int(time.time())  # Current Unix timestamp
    expiry = issued_at + 86400  # Expires in 24 hours (adjust as needed)

    # Create the payload
    payload = {
        "iss": company_url,
        "sub": oauth_client_id,
        "aud": safe_haven_environment,
        "iat": issued_at,
        "exp": expiry
    }

    jwt_token = jwt.encode(payload, private_key, algorithm="RS256")

    return (jwt_token) # return the jwt auth token

def accesstoken():
    url = "https://api.sandbox.safehavenmfb.com/oauth2/token"

    payload = {
        "grant_type": "client_credentials",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_id": "", # Client Kye From SafeHaven Dashboard
        "client_assertion": generate_and_print_token(), # call the token here
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

accesstoken() #this will generate the 