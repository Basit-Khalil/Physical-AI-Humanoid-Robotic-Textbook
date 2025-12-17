import requests
import time

def test_backend():
    url = "http://localhost:8001/"
    try:
        print("Testing connection to backend server...")
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        print("Backend server is running and accessible!")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to backend server. It may not be running or accessible.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Backend server may be slow to respond.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_backend()