def detect_intent(user_message: str) -> str:
    """
    Detects user intent in a minimal, rule-based way.
    Returns one of: greeting, info, high_intent
    """

    msg = user_message.lower()

    scores = {
        "greeting": 0,
        "info": 0,
        "high_intent": 0
    }

    greeting_words = ["hi", "hello", "hey"]
    info_words = ["price", "pricing", "cost", "plan", "features", "refund", "support"]
    high_intent_words = ["try", "buy", "purchase", "register","sign up", "signup", "subscribe", "get started"]

    for w in greeting_words:
        if w in msg:
            scores["greeting"] += 1

    for w in info_words:
        if w in msg:
            scores["info"] += 2

    for w in high_intent_words:
        if w in msg:
            scores["high_intent"] += 3

    # Pick the intent with the highest score
    print(scores,scores.get)
    return max(scores, key=scores.get)

detect_intent("What is the price of the Pro plan?")

