import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import webbrowser
import os
import wikipedia

horas_invertidas = 20;

name = 'DaddyBeto'

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
wikipedia.set_lang("es")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen(texto):
    try:
        with sr.Microphone() as source:
            print(texto)
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name,'')
                print("Usted dijo: " + rec)                                                
    except:
        pass

    return rec

    
def run():
    #Música y Videos en YT
    rec = listen('Esperando ordenes...')
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo '+ music)
        pywhatkit.playonyt(music)
                    
    #Hora
    elif 'dime la hora actual' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
                    
    # BUSCA EN WIKIPEDIA
    elif 'busca en wikipedia' in recognizer:
        consulta = recognizer.replace('busca en wikipedia', '')
        talk('buscando en wikipedia' + consulta)
        resultado = wikipedia.summary(consulta, sentences=3)
        talk(resultado)

    #Buscador 
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        talk('Buscando '+ order)
        pywhatkit.search(order)

 # BUSCA EN GOOGLE
    elif 'busca en google' in recognizer:
        consulta = recognizer.replace('busca en google', '')
        talk('Buscando en google' + consulta)
        pywhatkit.search(consulta)
        
    #Chistes
    elif 'dime un chiste' in rec:
        talk(pyjokes.get_joke('es'))
    
    elif 'créditos' in rec:
        webbrowser.open('https://www.youtube.com/watch?v=AOamtC2_r7k')


    #Ejecución de aplicaciones.exe
    elif 'ejecuta' in rec:
        order = rec.replace('ejecuta','')
        talk('Abriendo '+ order)
        app = order+'.exe'
        os.system(app)

    #Creación de directorios
    elif 'crea el directorio' in rec:
        home = "C:\Users\Danielmer\Documents\programacion avanzada\momento 3 practica"            
        order = rec.replace('crea el directorio','')

        if os.path.exists(order):
            talk("El directorio ya existe")

        else:
            mrk = os.mkdir(home+order)
            talk("Se creo el directorio correctamente")

    #Eliminación de directorios
    elif 'borra el directorio' in rec:
        order = rec.replace('borra el directorio','')
        if os.path.exists(order):
            rd = os.rmdir(order)
            talk("Se elimino el directorio correctamente")
        else:
            talk("El directorio no existe")

    #Creación de archivos de texto
    elif 'crea el archivo' in rec:
        order = rec.replace('crea el archivo','')
        order = order+'.txt'
        if os.path.exists(order):
            talk("El archivo ya existe")

        else:    
            archivo = open(order,"w")
            archivo.close()
            talk("Se creo el archivo correctamente")
                    
    #Eliminación de archivos de texto
    elif 'borra el archivo' in rec:
        order = rec.replace('borra el archivo','')
        order = order+'.txt'
        if os.path.exists(order):
            os.remove(order)
            talk("Se elimino el archivo correctamente")
        else:
            talk("El archivo no existe")

    else:
        talk("No te entendi muy bien, vuelve a intentarlo")
        


#Iniciador
if __name__ == "__main__":
    run()