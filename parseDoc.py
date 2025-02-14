import requests
from bs4 import BeautifulSoup

def parse_google_doc(url):
    # Step 1: Access the Google Doc content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 2: Extract the relevant data
    data = []
    rows = soup.find_all('tr')[1:]  # Skip the header row
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 3:
            x = int(cells[0].text.strip())
            char = cells[1].text.strip()
            y = int(cells[2].text.strip())
            data.append((x, y, char))

    # Step 3: Process the data to create the grid
    max_x = max(item[0] for item in data)
    max_y = max(item[1] for item in data)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in data:
        grid[y][x] = char

    # Step 4: Print the grid
    for row in reversed(grid):
        print(''.join(row))

# Example usage
url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
parse_google_doc(url)