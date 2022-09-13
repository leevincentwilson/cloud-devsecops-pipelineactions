import requests
import sys
import json
from datetime import datetime

def login(url, client_id, client_secret):
    try:
        url = f"https://{url}/oauth/token"
        payload = f"scope=api-tenant&grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code != 200:
            print("[ERROR] token generation failed.")
        else: 
            response = response.json()
            print("[INFO] Token generated successfully.")
            return response["access_token"]
    except Exception as e:
        print(e)
        print("[EXCEPTION] Error in generating the token. (Reference: login method)")
        sys.exit(1)

def get_scan(url, token, release_id):
    """
    Getting scan details saved in the given release.
    :return: response.
    """
    try:
        url = f"https://{url}/api/v3/releases/{release_id}/dynamic-scans/scan-setup"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        }

        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            print("[INFO] Dynamic Scan Details fetched successfully.")
            return response.json()

        elif response.status_code == 404:
            print("[ERROR] NotFound to fetch the dynamic scan details..")
            sys.exit(1)

        elif response.status_code == 401:
            print("[ERROR] Unauthorized to fetch the dynamic scan details..")
            sys.exit(1)

        elif response.status_code == TooManyRequests:
            print("[ERROR] TooManyRequests to fetch the dynamic scan details..")
            sys.exit(1)

        elif response.status_code == 500:
            print("[ERROR] InternalServerError to fetch the dynamic scan details..")
            sys.exit(1)

    except Exception as e:
        print("[EXCEPTION] Error in fetching the dynamic scan details. (Reference: get_scan method)")
        sys.exit(1)

def start_scan(url, token, release_id, assessmenttype_id, entitlement_id):
    """
    Starting Dynamic scan in the given release.
    :return: response.
    """
    try:
        url = f"https://{url}/api/v3/releases/{release_id}/dynamic-scans/start-scan"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%Y-%m-%dT%H:%M:%S.%f")

        payload = json.dumps({
                "startDate": timestampStr,
                "assessmentTypeId": assessmenttype_id,
                "entitlementId": entitlement_id,
                "entitlementFrequencyType": "SingleScan",
                "isRemediationScan": False,
                "isBundledAssessment": False,
                "parentAssessmentTypeId": 0,
                "applyPreviousScanSettings": False,
                "scanMethodType": "IDE",
                "scanTool": "string",
                "scanToolVersion": "string"
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            print("[INFO] Dynamic scan started successfully.")
            return response.json()
    
        elif response.status_code == 500:
            print("[ERROR] InternalServerError to start dynamic scan.")
            sys.exit(1)

        elif response.status_code == 400:
            print("[ERROR] BadRequest to start dynamic scan.")
            sys.exit(1)
        
        elif response.status_code == 422:
            print("[ERROR] UnprocessableEntity to start dynamic scan.")
            sys.exit(1)

        elif response.status_code == 429:
            print("[ERROR] TooManyRequests to start dynamic scan.")
            sys.exit(1)
          
    except Exception as e:
        print("[EXCEPTION] Error in starting the dynamic scan. (Reference: start_scan method)")
        sys.exit(1)

def main(client_id, client_secret, release_id):
    url = "api.sandbox.fortify.com"
    token = login(url, client_id, client_secret)
    scan_details = get_scan(url, token, release_id)
    assessmenttype_id = scan_details["assessmentTypeId"]
    entitlement_id = scan_details["entitlementId"]
    response = start_scan(url, token, release_id, assessmenttype_id, entitlement_id)
    print(response)

main(str(sys.argv[1]).strip(),str(sys.argv[2]).strip(),sys.argv[3].strip())
