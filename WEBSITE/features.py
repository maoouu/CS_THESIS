import librosa
import numpy as np


def extract_features(audio, sample_rate=22050) -> dict:
    """
    Extract features from audio file using Librosa library.

    Parameters:
    audio (str): audio file
    sample_rate (int): number of samples, default is 22050hz

    Returns:
    features (dict): a dictionary of extracted features
    """
    # audio, sample_rate = librosa.load(file, sr=22050)

    # Extract Chroma STFT
    chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sample_rate)

    # Extract Root Mean Squared (RMS) Energy
    rms = librosa.feature.rms(y=audio)

    # Extract Spectral Centroid
    spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sample_rate)

    # Extract Spectral Bandwidth
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=audio, sr=sample_rate)

    # Extract Rolloff Frequency
    rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sample_rate)

    # Extract Zero-Crossing Rate
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y=audio)

    # Extract Harmonic Elements
    harmony = librosa.effects.harmonic(y=audio)

    # Extract Percussive Elements
    perceptr = librosa.effects.percussive(y=audio)

    # Extract Tempo
    tempo = librosa.beat.tempo(y=audio, sr=sample_rate)

    # Extract Mel-Frequency Cepstral Coefficients (mfcc)
    mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate)

    features = {
        'chroma_stft_mean': np.mean(chroma_stft),
        'chroma_stft_var': np.var(chroma_stft),
        'rms_mean': np.mean(rms),
        'rms_var': np.var(rms),
        'spectral_centroid_mean': np.mean(spectral_centroid),
        'spectral_centroid_var': np.var(spectral_centroid),
        'spectral_bandwidth_mean': np.mean(spectral_bandwidth),
        'spectral_bandwidth_var': np.var(spectral_bandwidth),
        'rolloff_mean': np.mean(rolloff),
        'rolloff_var': np.var(rolloff),
        'zero_crossing_rate_mean': np.mean(zero_crossing_rate),
        'zero_crossing_rate_var': np.var(zero_crossing_rate),
        'harmony_mean': np.mean(harmony),
        'harmony_var': np.var(harmony),
        'perceptr_mean': np.mean(perceptr),
        'perceptr_var': np.var(perceptr),
        'tempo': np.mean(tempo),
    }

    # Append the mean and var of 20 MFCC coefficients
    for i in range(20):
        features[f"mfcc{i + 1}_mean"] = np.mean(mfcc[i].T, axis=0)
        features[f"mfcc{i + 1}_var"] = np.var(mfcc[i].T, axis=0)


    return features