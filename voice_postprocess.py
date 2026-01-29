import re


def simplify_words(text):
    replacements = {
        "initialize": "set up",
        "utilize": "use",
        "terminate": "stop",
        "approximately": "about",
        "module": "unit",
    }

    for k, v in replacements.items():
        text = re.sub(rf"\b{k}\b", v, text, flags=re.IGNORECASE)

    return text


def phoneticize(text):
    phonetics = {
        "PCIe": "P C I Express",
        "CPU": "C P U",
        "GPU": "G P U",
        "LED": "L E D",
    }

    for k, v in phonetics.items():
        text = re.sub(rf"\b{k}\b", v, text)

    return text


def split_for_speech(text, max_words=12):
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks


def voice_optimize(text):
    text = simplify_words(text)
    text = phoneticize(text)
    return split_for_speech(text)
