from django.shortcuts import render

def home(request):
    import json
    import requests
    
    api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=100&API_KEY=0F0131C0-5F0D-476F-B8FA-8445F52CE76C")
    
    try:
        api = json.loads(api_requests.content)
        
    except Exception as e:
        api = "Error..."
    
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})

