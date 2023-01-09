import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QTextEdit
import requests
from bs4 import BeautifulSoup

# Create the PyQt5 application
app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()
window.setWindowTitle('PyQt5 Browser')

# Create the URL bar
url_bar = QLineEdit(window)
url_bar.resize(400, 30)
url_bar.move(10, 10)

# Create the "Go" button
go_button = QPushButton('Go', window)
go_button.resize(30, 30)
go_button.move(420, 10)

# Set up the "Go" button's clicked signal
go_button.clicked.connect(go)

# Create the text area
text_area = QTextEdit(window)
text_area.resize(480, 360)
text_area.move(10, 50)

# Define the `go` function
def go():
  # Get the URL from the URL bar
  url = url_bar.text()

  # Make the HTTP request and parse the HTML
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')

  # Find the title of the webpage
  title = soup.find('title').text

  # Update the URL bar to show the title
  url_bar.setText(title)

# Show the main window and run the PyQt5 event loop
window.show()
app.exec_()
