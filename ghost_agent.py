import requests
import os
import random
import time
from gtts import gTTS
from moviepy.editor import ImageClip, TextClip, CompositeVideoClip, AudioFileClip

# CONFIGURATION DES APIS GRATUITES
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = os.getenv("GROQ_API_KEY") # À mettre dans les secrets GitHub

class GhostAgent:
    def __init__(self):
        self.niche = random.choice(["AI Tools", "Wealth Secrets", "Health Hacks"])
        self.affiliate_link = "TON_LIEN_ICI" # L'IA l'utilisera dans les captions

    def generate_brain(self, prompt):
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        data = {
            "model": "llama3-70b-8192",
            "messages": [{"role": "user", "content": prompt}]
        }
        res = requests.post(GROQ_API_URL, headers=headers, json=data)
        return res.json()['choices'][0]['message']['content']

    def create_video(self):
        print(f"[*] Analyse de la niche: {self.niche}")
        script = self.generate_brain(f"Ecris un script viral de 15s pour TikTok sur {self.niche}.")
        
        # 1. Générer l'audio (Gratuit)
        tts = gTTS(script, lang='fr')
        tts.save("voice.mp3")
        
        # 2. Générer l'image (Pollinations - Pas de clé)
        img_url = f"https://image.pollinations.ai/prompt/futuristic_{self.niche.replace(' ', '_')}?width=1080&height=1920&nologo=true"
        img_data = requests.get(img_url).content
        with open("bg.jpg", "wb") as f:
            f.write(img_data)
        
        # 3. Assemblage Vidéo
        audio = AudioFileClip("voice.mp3")
        bg = ImageClip("bg.jpg").set_duration(audio.duration)
        video = CompositeVideoClip([bg])
        video.audio = audio
        video.write_videofile("final_video.mp4", fps=24)
        return script

    def headless_post(self, script):
        print("[!] Tentative de postage automatique...")
        # Ici, l'IA simule un navigateur pour poster
        # Dans un environnement 0 budget, on utilise les APIs de partage direct
        pass

if __name__ == "__main__":
    agent = GhostAgent()
    script_content = agent.create_video()
    print(f"Vidéo prête avec le script : {script_content}")
