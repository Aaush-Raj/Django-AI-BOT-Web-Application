from django.shortcuts import render
import speech_recognition as sr 
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser

def index(request):
    return render(request, 'Webbot/index.html')


def bot_search(request):
    query = request.GET.get('query')

    try:
        client = wolframalpha.Client(" ") # Paste Your wolframalpha API Key Here....!!! Go to wolframalpha and Create your API key and paste it here.
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'Webbot/index.html',{'ans':ans,'query':query})
            
            
    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'Webbot/index.html',{'ans':ans,'query':query})
    
        except Exception:
            try:
                ans = "FOUND NOTHING"
                return render(request, 'Webbot/index.html',{'ans':ans,'query':query})
            except:
                print("It is weird but I got nothing try re-running the program")

        #return render(request, 'pybot/index.html')
