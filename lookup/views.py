from django.shortcuts import render

def home(request):
    import json
    import requests



    api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=100&API_KEY=0F0131C0-5F0D-476F-B8FA-8445F52CE76C")

    try:
        api = json.loads(api_requests.content)

    except Exception as e:
        api = "Error..."

    if api[0]['Category']['Name'] == "Good":
        category_description = "0 to 50	Air quality is satisfactory, and air pollution poses little or no risk."
        category_color = "Good"
    elif api[0]['Category']['Name'] == "Moderate":
        category_description = "1 to 100 Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
        category_color = "Moderate"
    elif api[0]['Category']['Name'] == "UnhealthyforSensitiveGroups":
        category_description = "101 to 150 members of sensitive groups may experience health effects. The general public is less likely to be affected."
        category_color = "UnhealthyforSensitiveGroups"
    elif api[0]['Category']['Name'] == "Unhealthy":
        category_description = "151 to 200 Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
        category_color = "Unhealthy"
    elif api[0]['Category']['Name'] == "VeryUnhealthy":
        category_description = "201 to 300 Health alert: The risk of health effects is increased for everyone."
        category_color = "VeryUnhealthy"
    elif api[0]['Category']['Name'] == "Hazardous":
       category_description = "301 and higher Health warning of emergency conditions: everyone is more likely to be affected."
       category_color = "Hazardous"


    return render(request, 'home.html', {'api': api,
        'category_description' : category_description,
        'category_color': category_color,})
def about(request):
    return render(request, 'about.html', {})
