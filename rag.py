conversation_history = []


def add_to_history(text):
    conversation_history.append(text)


def rewrite_query(partial_text):
    text = partial_text.lower()

    if "second" in text and conversation_history:
        last_topic = conversation_history[-1].lower()

        if "power module" in last_topic:
            return "second power module in the server"

        return f"{partial_text} related to {conversation_history[-1]}"

    return partial_text
