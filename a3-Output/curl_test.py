import requests
import matplotlib.pyplot as plt

# Number of requests to send
num_requests = 1000

# URL to send requests to
url = "http://192.168.58.2/"

# Counters for responses from app-1 and app-2
app1_count = 0
app2_count = 0

# Send requests and count responses
for _ in range(num_requests):
    response = requests.get(url)
    if "app-1-dep" in response.text:
        app1_count += 1
    elif "app-2-dep" in response.text:
        app2_count += 1

# Plot results
plt.bar(["app-1", "app-2"], [app1_count, app2_count])
plt.ylabel('Number of responses')
plt.title('Distribution of responses from app-1 and app-2')

# Save the figure as a PNG file
plt.savefig('output.png')
