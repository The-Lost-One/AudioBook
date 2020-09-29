import pyttsx3
import PyPDF2
book = open('D:\Chrome\Ebook\Deep_Learning_Interview_Guide.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)  # 0 for male 1 for female

'''rate = engine.getProperty('rate') # For speech Rate Change
speaker.setProperty('rate', 125)'''

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

#speaker.save_to_file(text, 'test.mp3')  #to save the audio file
speaker.stop()