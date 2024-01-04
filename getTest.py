import sys
import requests

# login to adventofcode.com in your browser
# download file from https://adventofcode.com/2023/day/X/input
# call it by python getTest.py X
# write it to ./Day X/testX.txt

def download_input(day):
    # read session cookie from session_cookie.txt    
    with open("session_cookie.txt", "r") as file:
        session_cookie = file.read().strip()
    
    url = f"https://adventofcode.com/2023/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    input_text = response.text.strip()
    file_path = f"./Day {day}/test.txt"
    
    with open(file_path, "w") as file:
        file.write(input_text)
    
    print(f"Input file for Day {day} downloaded successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python getTest.py <day>")
        sys.exit(1)
    
    day = sys.argv[1]
    download_input(day)
