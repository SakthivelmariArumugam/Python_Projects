import pyttsx3
import PyPDF2
path = open('D:\\Python Projects\\text_to_speech\\story.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(path)
page_number = int(input("Enter the from page: "))
from_page = pdfReader.pages[page_number]
text = from_page.extract_text()
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
