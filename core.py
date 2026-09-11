from data import db

def welcome():
    return (
        "<b>Vancore Support</b>\n\n"
        "This is your direct line to me.\n\n"
        "Found a bug, have an architectural idea, or want to challenge a design decision?\n\n"
        "Just send your message below. I review everything personally."
    )


def ticket_received():
    return (
        "<b>Message Delivered</b>\n\n"
        "Your message has been sent directly to the developer.\n\n"
        "Quality feedback deserves a thoughtful review. "
        "If your note requires a response, you will hear back directly.\n\n"
        "<i>Status: Delivered</i>"
    )
