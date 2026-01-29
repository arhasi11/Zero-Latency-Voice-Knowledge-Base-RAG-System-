import re

# 1️⃣ Replace formal / technical words with spoken English
def simplify_words(text):
    replacements = {
        "initialize": "set up",
        "terminate": "stop",
        "approximately": "about",
        "module": "unit",
        "utilize": "use",
        "configuration": "setup",
    }

    for k, v in replacements.items():
        text = re.sub(rf"\b{k}\b", v, text, flags=re.IGNORECASE)

    return text


# 2️⃣ Convert acronyms to phonetic speech
def phoneticize(text):
    phonetics = {
        "CPU": "C P U",
        "GPU": "G P U",
        "LED": "L E D",
        "PCIe": "P C I Express",
        "RAM": "R A M",
    }

    for k, v in phonetics.items():
        text = re.sub(rf"\b{k}\b", v, text, flags=re.IGNORECASE)

    return text


# 3️⃣ Break long text into TTS-friendly chunks
def split_for_speech(text, max_words=12):
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks


# 🔊 Main function used by app.py
def voice_optimize(text):
    text = simplify_words(text)
    text = phoneticize(text)
    return split_for_speech(text)
