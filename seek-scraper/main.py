import json
import os
import time
from datetime import datetime

import requests
from tqdm import tqdm

# Proxyman Code Generator (1.0.0): Python + Request
# GET https://www.seek.com.au/api/chalice-search/v4/search


def send_request(page=1):
    try:
        response = requests.get(
            url="https://www.seek.com.au/api/chalice-search/v4/search",
            params={
                "siteKey": "AU-Main",
                "sourcesystem": "houston",
                "userqueryid": "c31a6aa8cb75b382dd1a4c6bddabdabb-4418696",
                "userid": "6daccc9a4463e494a55744b16b4c689b",
                "usersessionid": "6daccc9a4463e494a55744b16b4c689b",
                "eventCaptureSessionId": "65501bc6-3bec-480c-818b-6873d2a382e8",
                "where": "All Australia",
                "page": str(page),
                "seekSelectAllPages": "true",
                "keywords": "azure data",
                "hadPremiumListings": "true",
                "include": "seodata",
                "seekerId": "44839513",
                "solId": "c493d04a-1819-4153-b477-b98688bf1cf4",
            },
            headers={
                "Host": "www.seek.com.au",
                "X-Seek-Site": "Chalice",
                "Accept-Encoding": "gzip, deflate, br",
                "Cookie": "_fbp=fb.2.1677283651971.1642895202; main=V%7C2~P%7Cjobsearch~K%7Cazure%20data~WID%7C3000~N%7C22~L%7C3000~OSF%7Cquick&set=1677284418749/V%7C2~P%7Cjobsearch~K%7Csnowflake~WID%7C3000~N%7C8~L%7C3000~OSF%7Cquick&set=1677283946048; sol_id=c493d04a-1819-4153-b477-b98688bf1cf4; da_anz_candi_sid=1677283649551; da_cdt=visid_018685e5680f00168144f45105bb01075001806d00b35-sesid_1677283649551; utag_main=v_id:018685e5680f00168144f45105bb01075001806d00b35$_sn:1$_se:104$_ss:0$_st:1677286217359$ses_id:1677283649551%3Bexp-session$_pn:5%3Bexp-session$dc_visit:1$dc_event:104%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session; _dd_s=rum=0&expire=1677285317742; _ga_JYC9JXRYWC=GS1.1.1677283651.1.1.1677284415.35.0.0; _hjAbsoluteSessionInProgress=0; _hjFirstSeen=1; _hjSession_162402=eyJpZCI6ImYwMWQ3ZjU0LWRmYTUtNGFhYy1iNWM5LTI0Njg2MTZkN2NhMiIsImNyZWF0ZWQiOjE2NzcyODM2NTAwMjcsImluU2FtcGxlIjpmYWxzZX0=; da_searchTerm=azure data; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%2244839513%22%7D; skl-lcid=89d06c31-04d1-4997-b177-7bd2f387c0cb; sol_id=c493d04a-1819-4153-b477-b98688bf1cf4; _hjIncludedInSessionSample_162402=0; _gat_tealium_0=1; _ga=GA1.1.305958570.1677283650; _gid=GA1.3.2066954810.1677283650; _hjSessionUser_162402=eyJpZCI6ImZlYjA3MTA5LWQyNjgtNWFjNi1hNTJmLTlkODVkYjVmYTAxNCIsImNyZWF0ZWQiOjE2NzcyODM2NTAwMjMsImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=27e4a226cdcc9034:T=1677283694:RT=1677284081:S=ALNI_MZAF-_fT4tlKsq8zutfhQgxIO6wcg; __gpi=UID=00000bcb93f54dbb:T=1677283694:RT=1677283694:S=ALNI_MYe4SVFJ70plcO3av0wgKsIciruCw; _pin_unauth=dWlkPVpEQTNNakk1WVdFdE9EWmtaUzAwT0RJNUxUZzBaall0WVdNd1ptVTFOakF5Wm1VeQ; last-known-sol-user-id=2627ecc5ed53b8cf7bf9de0354d92b4a6882063d81776d40c1acb68e42006d7547e438cd69c0f47f41ab5d69d6478a4be543f6c0fdb5044d401510aa53a9ee3a962cd4c2c956a08754e7eb84d890d89638331189dc6a1471ec5b7c325d8a29592ccfd01eb7589ed35076e9f8bfe7ced887f42dca53ddc77e1e2702c4ed947a56a3a6af16f8c59d821992508292803e37d637c51359113f90c844efdfe10d914a8838771b9b87; _legacy_auth0.yGBVge66K5NJpSN5u71fU90VcTlEASNu.is.authenticated=true; auth0.yGBVge66K5NJpSN5u71fU90VcTlEASNu.is.authenticated=true; _sctr=1|1677243600000; _gcl_au=1.1.898508618.1677283651; _schn=_tvku74; _scid=8ec6412d-6fcf-4b1b-8ce5-2650b878bde2; da_marketing_channel=Direct; da_marketing_channel_value=https://www.seek.com.au/; da_tracking_code=null; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22b1qcHy3vpTtJD9r5TLxE%22%7D; JobseekerSessionId=65501bc6-3bec-480c-818b-6873d2a382e8; __cf_bm=9Yl49sHmb0Qvo4_8BKDmuj8y7L7El2QMyu31pg2.xK8-1677283648-0-AVGhVBF9g8VmgblmK36M1oLVtbB3OJGdxsDjjMdt13JS4fIbxQCLbuyK4iEJei7U9qItCucTtPSSM54+3JwgGYM=; AB_VARIANTS=%7B%22default%22%3A%22A%22%2C%22AB_TEST_Role_Bootcamp_Whole_Card%22%3A%22A%22%7D; JobseekerVisitorId=6daccc9a4463e494a55744b16b4c689b",
                "Connection": "keep-alive",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15",
                "Referer": "https://www.seek.com.au/azure-data-jobs?page=22",
                "x-seek-checksum": "12aff385",
                "Accept-Language": "en-AU,en;q=0.9",
            },
        )
        return response.json()
    except requests.exceptions.RequestException:
        print("HTTP Request failed")
        return response


def get_job_details(job_id=61392564):
    data = json.loads(
        r"""{
                            "operationName": "GetJobDetails",
                            "variables": {
                                "jobId": "61392564",
                                "jobDetailsViewedCorrelationId": "6256d60e-13a0-4af2-a223-d7000ebdfcaf",
                                "sessionId": "65501bc6-3bec-480c-818b-6873d2a382e8",
                                "zone": "anz-1",
                                "locale": "en-AU"
                            },
                            "query": "query GetJobDetails($jobId: ID!, $jobDetailsViewedCorrelationId: String!, $sessionId: String!, $zone: Zone!, $locale: Locale!) {\n  jobDetails(\n    id: $jobId\n    tracking: {channel: \"WEB\", jobDetailsViewedCorrelationId: $jobDetailsViewedCorrelationId, sessionId: $sessionId}\n  ) {\n    job {\n      tracking {\n        adProductType\n        classificationInfo {\n          classificationId\n          classification\n          subClassificationId\n          subClassification\n          __typename\n        }\n        hasRoleRequirements\n        isPrivateAdvertiser\n        locationInfo {\n          area\n          location\n          locationIds\n          __typename\n        }\n        __typename\n      }\n      id\n      title\n      phoneNumber\n      isExpired\n      isLinkOut\n      contactMatches {\n        type\n        value\n        __typename\n      }\n      abstract\n      content(platform: WEB)\n      status\n      listedAt {\n        shortLabel\n        __typename\n      }\n      salary {\n        currencyLabel(zone: $zone)\n        label\n        __typename\n      }\n      shareLink(platform: WEB, zone: $zone)\n      workTypes {\n        label\n        __typename\n      }\n      advertiser {\n        id\n        name\n        __typename\n      }\n      location {\n        label(locale: $locale, type: LONG)\n        __typename\n      }\n      categories {\n        label\n        __typename\n      }\n      products {\n        branding {\n          id\n          cover {\n            url\n            __typename\n          }\n          thumbnailCover: cover(isThumbnail: true) {\n            url\n            __typename\n          }\n          logo {\n            url\n            __typename\n          }\n          __typename\n        }\n        bullets\n        questionnaire {\n          questions\n          __typename\n        }\n        video {\n          url\n          position\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    companyReviews(zone: $zone) {\n      id\n      name\n      fullName\n      rating\n      reviewCount\n      reviewsUrl\n      __typename\n    }\n    companySearchUrl(zone: $zone)\n    learningInsights(platform: WEB, zone: $zone) {\n      analytics\n      content\n      __typename\n    }\n    companyTags {\n      key\n      value\n      __typename\n    }\n    sourcr {\n      image\n      imageMobile\n      link\n      __typename\n    }\n    __typename\n  }\n}\n"
                            }"""
    )
    data["variables"]["jobId"] = job_id
    try:
        response = requests.post(
            url="https://www.seek.com.au/graphql",
            headers={
                "Host": "www.seek.com.au",
                "X-Seek-Site": "chalice",
                "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1SNnNiT3cyS1hRVGc1Q2JJWjRyVCJ9.eyJodHRwOi8vc2Vlay9jbGFpbXMvY291bnRyeSI6IkFVIiwiaHR0cDovL3NlZWsvY2xhaW1zL2JyYW5kIjoic2VlayIsImh0dHA6Ly9zZWVrL2NsYWltcy9leHBlcmllbmNlIjoiY2FuZGlkYXRlIiwiaHR0cDovL3NlZWsvY2xhaW1zL3VzZXJfaWQiOiI0NDgzOTUxMyIsImlzcyI6Imh0dHBzOi8vbG9naW4uc2Vlay5jb20vIiwic3ViIjoiYXV0aDB8NmJhOGRlNjQ1Zjg0NGI1MGE4N2E5YzZjMDIwYzQxMjUiLCJhdWQiOlsiaHR0cHM6Ly9zZWVrL2FwaS9jYW5kaWRhdGUiLCJodHRwczovL3NlZWthbnoub25saW5lYXV0aC5wcm9kLm91dGZyYS54eXovdXNlcmluZm8iXSwiaWF0IjoxNjc3MjgzNjc4LCJleHAiOjE2NzcyODcyNzgsImF6cCI6InlHQlZnZTY2SzVOSnBTTjV1NzFmVTkwVmNUbEVBU051Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBvZmZsaW5lX2FjY2VzcyJ9.Tccm6w9_TPTKoKC1L3VAonAv78tEi7tKCwsvdDefs26aYnjhvmbT8NAPKh4y4bHzFkWdbOkM8dorqthVBbdvYzB4xLbRpuyZqBSo8P8fVuQcXbOzKjIUcSbAQFPlJLAKh2AZnIvNhAbhaBi9iDVtE77aZaU44gD-ByTQiK9LB3YVtcrIJ-1KvqAHZm8N0BBYYpyZYl4CNo_FJ0QQXrxZDK11xFmUfzAGUV6xBT06cii8em2JaHHMEHwIcl6HKNx0gxNlq2Bh3hddt6-BC1bVYlpJyPpN3YIeaoeBw74qyEIsCRncFq8CFLBqWn7z9k2xvmw33Nc0XrIcEPC_qEfJjw",
                "seek-request-brand": "seek",
                "x-application": "au",
                "X-Seek-EC-SessionId": "65501bc6-3bec-480c-818b-6873d2a382e8",
                "X-Seek-EC-VisitorId": "6daccc9a4463e494a55744b16b4c689b",
                "Accept": "*/*",
                "Accept-Language": "en-AU,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/json",
                "Origin": "https://www.seek.com.au",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15",
                "seek-request-country": "AU",
                "Referer": "https://www.seek.com.au/job/61392564?type=standout",
                "Content-Length": "2711",
                "Connection": "keep-alive",
                "Cookie": "_fbp=fb.2.1677283651971.1642895202; sol_id=c493d04a-1819-4153-b477-b98688bf1cf4; _dd_s=rum=0&expire=1677284656209; da_anz_candi_sid=1677283649551; da_cdt=visid_018685e5680f00168144f45105bb01075001806d00b35-sesid_1677283649551; utag_main=v_id:018685e5680f00168144f45105bb01075001806d00b35$_sn:1$_se:19$_ss:0$_st:1677285544804$ses_id:1677283649551%3Bexp-session$_pn:4%3Bexp-session$dc_visit:1$dc_event:19%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session; _ga_JYC9JXRYWC=GS1.1.1677283651.1.1.1677283742.60.0.0; _gat_tealium_0=1; da_searchTerm=snowflake; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%2244839513%22%7D; skl-lcid=a9ca3c6d-f011-48d9-ae0f-dc38b999d973; sol_id=c493d04a-1819-4153-b477-b98688bf1cf4; _hjAbsoluteSessionInProgress=0; main=V%7C2~P%7Cjobsearch~K%7Csnowflake~WID%7C3000~N%7C3~L%7C3000~OSF%7Cquick&set=1677283741853; _hjIncludedInSessionSample_162402=0; _hjFirstSeen=1; _hjSession_162402=eyJpZCI6ImYwMWQ3ZjU0LWRmYTUtNGFhYy1iNWM5LTI0Njg2MTZkN2NhMiIsImNyZWF0ZWQiOjE2NzcyODM2NTAwMjcsImluU2FtcGxlIjpmYWxzZX0=; __gads=ID=27e4a226cdcc9034:T=1677283694:RT=1677283694:S=ALNI_MZAF-_fT4tlKsq8zutfhQgxIO6wcg; __gpi=UID=00000bcb93f54dbb:T=1677283694:RT=1677283694:S=ALNI_MYe4SVFJ70plcO3av0wgKsIciruCw; _ga=GA1.1.305958570.1677283650; _pin_unauth=dWlkPVpEQTNNakk1WVdFdE9EWmtaUzAwT0RJNUxUZzBaall0WVdNd1ptVTFOakF5Wm1VeQ; _gid=GA1.3.2066954810.1677283650; _hjSessionUser_162402=eyJpZCI6ImZlYjA3MTA5LWQyNjgtNWFjNi1hNTJmLTlkODVkYjVmYTAxNCIsImNyZWF0ZWQiOjE2NzcyODM2NTAwMjMsImV4aXN0aW5nIjp0cnVlfQ==; last-known-sol-user-id=2627ecc5ed53b8cf7bf9de0354d92b4a6882063d81776d40c1acb68e42006d7547e438cd69c0f47f41ab5d69d6478a4be543f6c0fdb5044d401510aa53a9ee3a962cd4c2c956a08754e7eb84d890d89638331189dc6a1471ec5b7c325d8a29592ccfd01eb7589ed35076e9f8bfe7ced887f42dca53ddc77e1e2702c4ed947a56a3a6af16f8c59d821992508292803e37d637c51359113f90c844efdfe10d914a8838771b9b87; _legacy_auth0.yGBVge66K5NJpSN5u71fU90VcTlEASNu.is.authenticated=true; auth0.yGBVge66K5NJpSN5u71fU90VcTlEASNu.is.authenticated=true; _sctr=1|1677243600000; _gcl_au=1.1.898508618.1677283651; _schn=_tvku74; _scid=8ec6412d-6fcf-4b1b-8ce5-2650b878bde2; da_marketing_channel=Direct; da_marketing_channel_value=https://www.seek.com.au/; da_tracking_code=null; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22b1qcHy3vpTtJD9r5TLxE%22%7D; JobseekerSessionId=65501bc6-3bec-480c-818b-6873d2a382e8; __cf_bm=9Yl49sHmb0Qvo4_8BKDmuj8y7L7El2QMyu31pg2.xK8-1677283648-0-AVGhVBF9g8VmgblmK36M1oLVtbB3OJGdxsDjjMdt13JS4fIbxQCLbuyK4iEJei7U9qItCucTtPSSM54+3JwgGYM=; AB_VARIANTS=%7B%22default%22%3A%22A%22%2C%22AB_TEST_Role_Bootcamp_Whole_Card%22%3A%22A%22%7D; JobseekerVisitorId=6daccc9a4463e494a55744b16b4c689b",
            },
            data=json.dumps(data, indent=4),
        )
        return response.json()
    except requests.exceptions.RequestException:
        print("HTTP Request failed")


def write_json(data, file_time=None):
    if file_time is None:
        file_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # Create data directory
    if not os.path.exists("data"):
        os.makedirs("data")

    # Write responses to json file, named with timestamp
    with open(f"data/seek-{file_time}.json", "w") as f:
        json_object = json.dumps(responses, indent=4)
        f.write(json_object)


if __name__ == "__main__":
    responses = []
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    try:
        for i in tqdm(range(1, 23)):
            res = send_request(i)
            job_ids = [r["id"] for r in res["data"]]
            job_details = []
            index = 0
            for job in job_ids:
                index += 1
                print(
                    f"Getting details for job {job}, {index} of {len(job_ids)}"
                )
                details = get_job_details(job)["data"]
                job_details.append(details)
                time.sleep(0.5)
                res["job_details"] = job_details
            responses.append(res)
            time.sleep(1)
            write_json(responses, now)
    except KeyboardInterrupt:
        write_json(responses, now)

    ...
