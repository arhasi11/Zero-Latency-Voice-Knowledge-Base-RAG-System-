from voice_postprocess import voice_optimize

text = (
    "To initialize the second power module, "
    "check the LED indicator on the CPU board."
)

chunks = voice_optimize(text)

for c in chunks:
    print("🔊", c)
