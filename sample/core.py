from . import helpers


def get_hmm():
    print("""Get a thought.""")
    return "hmmm..."


def hmm():
    print("""Contemplation...""")
    if helpers.get_answer():
        print(get_hmm())
        return "test"
