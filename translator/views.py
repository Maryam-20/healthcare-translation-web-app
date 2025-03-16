from django.shortcuts import render, redirect
from google.cloud import translate_v2 as translate  # Import the translation library
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from google.cloud import speech
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    return render(request, "index.html")

# Initialize the Google Cloud Translation client
translate_client = translate.Client()


@csrf_exempt
def translate_text(request):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode("utf-8")
            print("Received Raw Data:", body_unicode) 

            if not body_unicode:  # If the request body is empty
                return JsonResponse({"error": "Empty request body"}, status=400)

            data = json.loads(body_unicode)  # Attempt to parse JSON
            print("Parsed JSON Data:", data)  # Debugging step
            
            text = data.get("text", "")
            language = data.get("language", "")
            if not text:
                return JsonResponse({"error": "No text provided"}, status=400)

            # Actual translation logic using Google Cloud Translation API
            translation = translate_client.translate(text, target_language=language)
            translated_text = translation['translatedText']

            return JsonResponse({"message": "Text received successfully", "translated_text": translated_text})
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)  

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def transcribe_audio(request):
    if request.method == "POST":
        if 'audio' not in request.FILES:
            return JsonResponse({"error": "No audio file provided"}, status=400)

        audio_file = request.FILES['audio']

        # Initialize the Google Speech client
        client = speech.SpeechClient()

        try:
            # Read the audio file
            content = audio_file.read()

            audio = speech.RecognitionAudio(content=content)
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code="en-US",
                model="medical_conversation"  # Optimized for medical transcription
            )

            # Perform speech recognition
            response = client.recognize(config=config, audio=audio)

            transcript = ""
            for result in response.results:
                transcript += result.alternatives[0].transcript + " "

            return JsonResponse({"transcript": transcript.strip()})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)  
    return JsonResponse({"error": "Invalid request"}, status=400)

def logout_view(request):
    logout(request)  
    return render(request, 'registration/logout.html')  


