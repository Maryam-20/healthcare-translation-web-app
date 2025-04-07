# 🏥 Healthcare Translation Web App with Generative AI

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-Speech_&_Translation-blueviolet)](https://cloud.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A real-time, multilingual healthcare communication assistant powered by generative AI. This web application converts spoken input into text,
provides live translation, and offers audio playback—improving interactions between healthcare providers and patients.

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [📦 Installation](#-installation)
- [🚀 Usage](#-usage)
- [🔧 Technologies Used](#-technologies-used)
- [🔐 Security Considerations](#-security-considerations)
- [🧠 AI Services Used](#-ai-services-used)
- [📜 License](#-license)

---

## ✨ Features

- 🎤 **Voice-to-Text with Generative AI**  
  Transcribes spoken audio into text using Google Cloud's Speech-to-Text, optimized for medical terminology.

- 🌐 **Real-Time Translation**  
  Translate transcripts instantly using Google Cloud Translation API.

- 🔊 **Audio Playback**  
  Translated text can be played back via browser text-to-speech.

- 📱 **Mobile-First Design**  
  Responsive UI/UX optimized for both mobile and desktop environments.

- 🌍 **Language Selection**  
  Easily switch input and output languages.

- 🔐 **Secure Communication**  
  Environment variable management, user authentication, and safe handling of healthcare data.

---

## 📦 Installation

### Step-by-step to run locally:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Maryam-20/healthcare-translation.git
   cd healthcare-translation
   ```

2. **Set Up Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Google Cloud Credentials**  
   - Create a service account in Google Cloud Console.
   - Download the JSON key.
   - Set the environment variable:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
     ```

5. **Apply Migrations**  
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**  
   ```bash
   python manage.py runserver
   ```

---

## 🚀 Usage

1. **Start the App**  
   Launch the server and open `http://localhost:8000` in your browser.

2. **Record Voice**  
   Click the **“Start Recording”** button. The browser captures your voice.

3. **Transcription**  
   The backend uses Google Cloud Speech-to-Text to transcribe spoken words into text.

4. **Translate**  
   Click **“Translate”** to convert your transcript into the target language.

5. **Audio Playback**  
   Hit the **“Speak”** button to hear the translated text.

🖼️ _Screenshots & examples coming soon!_

---

## 🔧 Technologies Used

| Layer        | Tool/Tech                         |
|--------------|-----------------------------------|
| Backend      | Django, Python                    |
| Frontend     | React (w/ Tailwind CSS)           |
| AI Services  | Google Cloud Speech-to-Text, Google Cloud Translation API |
| Voice Capture| Web Speech API                    |
| Deployment   | Render  https://healthcare-translation-web-app-qx4h.onrender.com  |
| Auth/Security| Django Auth, Environment Variables, Whitenoise |

---

## 🔐 Security Considerations

- **Authentication**: Uses Django’s built-in user system for access control.
- **Data Privacy**: Credentials and secrets handled via environment variables.
- **Validation**: User inputs are validated via Django forms and serializers.
- **Error Handling**: Translation and transcription services include fallback messages.
- **HTTPS**: Recommended for deployment to ensure encrypted communication.
- **Static Files**: Served securely via Whitenoise in production.

---

## 🧠 AI Services Used

- **Google Cloud Speech-to-Text API**  
  Transcribes spoken medical conversations into accurate, structured text.

- **Google Cloud Translation API**  
  Translates text between supported languages in real time.

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
