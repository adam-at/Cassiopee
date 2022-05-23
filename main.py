import librosa.display
import keyEstimator as k

# Choix de la musique
# audio_path = 'res/Perfect.wav'
# y, sr = librosa.load(audio_path)

# Décompose la musique en composantes harmoniques et à percussions
# pour améliorer les performances de l'analyse
# y_harmonic, y_percussive = librosa.effects.hpss(y)


# espada = k.keyEstimator(y_harmonic, sr)
# espada.chromagram("La espada")
# espada.print_chroma()
# espada.print_key()
# print(espada.correlations())

C_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
Csharp_notes = ['C#', 'Eb', 'F', 'F#', 'Ab', 'Bb', 'B#']
D_notes = ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']
Eb_notes = ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D']
E_notes = ['E', 'F#', 'Ab', 'A', 'B', 'C#', 'Eb']
F_notes = ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']
Fsharp_notes = ['F#', 'Ab', 'Bb', 'B', 'C#', 'Eb', 'F']
G_notes = ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
Ab_notes = ['Ab', 'Bb', 'C', 'C#', 'Eb', 'F', 'G']
A_notes = ['A', 'B', 'C#', 'D', 'E', 'F#', 'Ab']
Bb_notes = ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A']
B_notes = ['B', 'C#', 'Eb', 'E', 'F#', 'Ab', 'Bb']

#retourne la nouvelle probabilité à partir
def new_probs(note:str, prob:float, music:k.keyEstimator):
    pitches = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
    notes_by_key = [C_notes, Csharp_notes, D_notes, Eb_notes, E_notes, F_notes, Fsharp_notes, G_notes, Ab_notes, A_notes, Bb_notes, B_notes]

    # music est obtenu de la façon suivante à partir du path vers l'audio audio_path:
    # y, sr = librosa.load(audio_path)
    # y_harmonic, y_percussive = librosa.effects.hpss(y)
    # music = k.keyEstimator(y_harmonic, sr)

    correlations = music.correlations()
    correct_keys = []
    for i in range(12):
        if note in notes_by_key[i]:
            correct_keys.append(pitches[i])
    max_correlation = 0
    for i in range(len(correct_keys)):
        max_correlation = max(max_correlation, correlations.get(correct_keys[i]))
    return prob*max_correlation
    










