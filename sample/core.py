from . import helpers


def get_hmm():
    print("""Get a thought.""")
    return "hmmm..."


def hmm():
    print("""Contemplation...""")
    if helpers.get_answer():
        hmm = get_hmm()
        print(hmm)
        return hmm
