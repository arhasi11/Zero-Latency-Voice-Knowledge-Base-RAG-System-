def stream_transcript(full_text):
    words = full_text.split()
    partials = []

    for i in range(3, len(words), 3):
        partials.append(" ".join(words[:i]))

    # 🔥 IMPORTANT: ensure final full transcript is included
    if partials[-1] != full_text:
        partials.append(full_text)

    return partials
