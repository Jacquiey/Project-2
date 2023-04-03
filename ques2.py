# ID- 10984191
# DEPARTMENT - BIOMEDICAL ENGINEERING
import PySimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()

layout = [
    [sg.Text("Enter your text here:")],
    [sg.InputText(key="input_text")],
    [sg.Text("Select a voice:")],
    [sg.Radio("Male", group_id="voice", key="male_voice"), sg.Radio("Female", group_id="voice", key="female_voice")],
    [sg.Button("Speak")]
]

window = sg.Window("Text-to-Speech App", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Stop":
        break

    if event == "Speak":
        
        if values["male_voice"]:
            voices = engine.getProperty('voices')
            engine.setProperty("voice", voices[0].id)
        elif values["female_voice"]:
            voices= engine.getProperty('voices')
            engine.setProperty("voice", voices[1].id)

        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)

        engine.say(values["input_text"])
        engine.runAndWait()

window.close()
engine.stop()
