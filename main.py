import librosa.display
import keyEstimator as k

# Choix de la musique
audio_path = 'res/Clavar-la-espada.wav'
y, sr = librosa.load(audio_path)

# Décompose la musique en composantes harmoniques et à percussions
# pour améliorer les performances de l'analyse
y_harmonic, y_percussive = librosa.effects.hpss(y)


espada = k.keyEstimator(y_harmonic, sr)
espada.chromagram("La espada")
espada.print_chroma()
espada.print_key()








