def stream_transcript(full_text):
    """
    Simulates streaming ASR by yielding partial transcripts.
    Always guarantees at least one partial and the final transcript.
    """

    words = full_text.split()
    partials = []

    # Handle very short queries safely
    if len(words) <= 3:
        return [full_text]

    # Generate partial transcripts
    for i in range(3, len(words), 3):
        partials.append(" ".join(words[:i]))

    # 🔥 Ensure final full transcript is always included
    if partials[-1] != full_text:
        partials.append(full_text)

    return partials
