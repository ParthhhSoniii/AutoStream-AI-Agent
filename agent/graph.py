from agent.Intent import detect_intent
from agent.RAG import answer_with_rag
from agent.Tools import mock_lead_capture


def run_agent(user_input: str, stage: str, lead: dict):
    intent = detect_intent(user_input)

    # -------- STAGE 1: GREETING --------
    if stage == "start":
        return (
            "Hi! 👋 I'm the AutoStream assistant. "
            "I can help with pricing, features, or getting you started.",
            "info",
            lead
        )

    # -------- STAGE 2: INFO --------
    elif stage == "info":
        if intent == "high_intent":
            return (
                "That's great! 😊 May I know your name?",
                "lead_name",
                lead
            )
        return (answer_with_rag(user_input), "info", lead)

    # -------- STAGE 3: NAME --------
    elif stage == "lead_name":
        lead["name"] = user_input
        return (
            "Thanks! Could you share your email address?",
            "lead_email",
            lead
        )

    # -------- STAGE 4: EMAIL --------
    elif stage == "lead_email":
        lead["email"] = user_input
        return (
            "Great 👍 Which platform do you mainly create content on?",
            "lead_platform",
            lead
        )

    # -------- STAGE 5: PLATFORM --------
    elif stage == "lead_platform":
        lead["platform"] = user_input

        # ✅ TOOL CALL WITH ALL DATA
        mock_lead_capture(
            lead["name"],
            lead["email"],
            lead["platform"]
        )

        return (
            "🎉 Lead captured successfully! Our team will contact you shortly.",
            "done",
            lead
        )

    return ("You're all set! 😊", stage, lead)
