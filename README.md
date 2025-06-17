# Schreifmaschinn-Lite (Command Line Tool) fir Windows

Dësen Tool benotzt den ZLS Whisper-Modell fir d'Transkriptioun vu lëtzebuergeschen Audiodonnéeën. Heidrënner fënnt een d'Schrëtt fir d'Installatioun an d'Benotzung op Windows.

---

## Installatioun
1. **Fichiere vu Github eroflueden**
   Luet d'Fichieren an dësem Github-Repository erof a späichert se an engem lokalen Dossier op Ärem Computer.
   
2. **Modell eroflueden**  
   Luet déi follgend zwee Fichiere vum HuggingFace-Repository erof a späichert se an deem nämmlechten Dossier:  
   [`pytorch_model.bin`](https://huggingface.co/ZLSCompLing/whisper_large_lb_ZLS_v4_38h/resolve/main/pytorch_model.bin)  
   [`config.json`](https://huggingface.co/ZLSCompLing/whisper_large_lb_ZLS_v4_38h/resolve/main/config.json)  

3. **Audio-Dossier uleeën**  
   Leet an deem selwechten Dossier en neie Fichier mam Numm un:  
   ```
   audio
   ```

4. **Python 3.10 Virtual Environment (venv) an Dependencies installéieren**  

OPGEPASST: Fir de Modell kënnen ze benotzen, muss Python 3.10 benotzt ginn

   ```bash
   python3.10 -m venv venv
   venv\Scripts\activate.bat
   pip install -r requirements.txt
   ```

5. **Audiodonnéeën bäisetzen**  
   Setzt all d'Audiodonnéeën, déi Dir wëllt transkribéieren, an den `audio`-Dossier bäi.

6. **Transkriptioun starten**  

   ```bash
   python transcribe_audio_in_folder.py
   ```
   
   Fir all Audiodonnéeë gëtt en Text-Fichier mam selwechten Numm generéiert, deen d'Transkriptioun enthält.
