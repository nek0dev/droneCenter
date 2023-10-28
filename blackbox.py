from httpx import Client
import time

blackbox = Client()

for i in range(50, 70):
    resp = blackbox.post(url="http://91.107.125.237:8001/drone/change-coordinates", json={
        "serial_number": "SAMARITANIN",
        "latitude": i,
        "longitude": i
    }, 
    headers={
        "content-type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pbl9pZCI6MSwidHlwZSI6ImFkbWluIiwiZXhwaXJlcyI6MTcwMTA2NzM2NC4wMDM2MzY4fQ._BDkHzHRptHtM8aWmEUvuOm8kt4zuUacy5DCE0JgFFw"
    },
    follow_redirects=True)
    print(resp)
    input()
    time.sleep(2)