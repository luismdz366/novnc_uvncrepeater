"""Execute a request to the given url to check the response"""
import requests
import traceback


def exec_request(url, params=None, timeout=5):
    try:
        response = requests.get(url, params=params, timeout=timeout)
        return response
    except requests.RequestException:
        return None


def lookup(self, token):
    """Get the host and port for a given token. Return None if the token is invalid."""

    # Implement a context manager over the connection manager to ensure proper resource handling
    # the context manager

    # Make a request to the Asset Digitization Program to validate the token and get the host and port
    # The token is sent as a query parameter in the URL
    # Get the response from the Asset Digitization Program
    # If the response status is 200, it means the request was successful
    # url = f"http://{ADAPP_SERVER}:{ADAPP_PORT}{ADAPP_TOKENVALIDATION_URL}"
    # response = requests.get(url, params={"adp": token}, timeout=5)
    # logger.info("LOOKUP CALLED token=%s", token)

    try:
        s_id = None
        response = requests.get(url, params={"adp": token}, timeout=5)
        if response.status_code == 200:
            # Read the response data and serialize to python object (dict)
            data = response.json()
            print("Response data:", data)
            if data.get("validation") == '1':
                print("Token is valid")
                return (repeater[0], repeater[1], str(data.get("id")))
            else:
                print("Token is invalid")
                return None
        else:
            print("Request failed with status code:",
                  response.status_code, "Response text:", response.text)

            return None
    except requests.RequestException:
        print("Request exception occurred")
        traceback.print_exc()
        return None


if __name__ == "__main__":
    local_url = "http://localhost:8088/system/webdev/uvnc_Dev/dev/token_validation"
    # the reponse should have a JSON object with "validation" and "id" fields
    # response = exec_request(local_url, params={"adp": "1234"})
    # if response:
    #     print(response.status_code, response.text)
    # else:
    #     print("Request failed")

    # test the lookup function
    # define a global variables for the function
    global adpapp, repeater, url, ADAPP_SERVER, ADAPP_PORT, ADAPP_TOKENVALIDATION_URL
    adpapp = ('192.168.10.115', 80)
    repeater = ('192.168.10.115', 5900)
    # url = "/ahm/cms_validation.json"
    url = local_url
    ADAPP_SERVER = "localhost"
    # ADAPP_PORT = 5000
    # ADAPP_TOKENVALIDATION_URL = "/ahm/cms_validation.json"
    ADAPP_PORT = 8088
    ADAPP_TOKENVALIDATION_URL = local_url

    result = lookup(None, "1234")
    print("Lookup result:", result)
