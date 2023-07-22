import requests

url = 'http://localhost:5000/api/trigger_report'
response = requests.post(url)

if response.status_code == 200:
    print("Report triggered successfully!")
    report_id = response.json().get('report_id')
    print(f"Report ID: {report_id}")
else:
    print("Failed to trigger the report.")
    print(f"Status Code: {response.status_code}")
    print(response.json())