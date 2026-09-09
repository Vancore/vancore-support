from data import db

def welcome(uid):
    return (
        "<b>Vancore Support</b>\n\n"
        "This is your direct line to me.\n\n"
        "Found a bug? Have an idea? Or just want to share your feedback? "
        "Send it here. I review every message personally.\n\n"
    )


def ticket_received(uid):
    return (
        "<b>Message Delivered</b>\n\n"
        "Your thoughts have been sent directly to the developer. "
        "Quality takes time, so wait for the response.\n\n"
        "<i>Status: In Queue</i>"
    )
