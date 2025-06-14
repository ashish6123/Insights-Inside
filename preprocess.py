import re

# Hard-coded list of English stopwords (no nltk required)
stop_words = set("""
i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself
they them their theirs themselves what which who whom this that these those am is are was were be been being have has had
having do does did doing a an the and but if or because as until while of at by for with about against between into through
during before after above below to from up down in out on off over under again further then once here there when where why
how all any both each few more most other some such no nor not only own same so than too very s t can will just don don
should now
""".split())

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation and digits
    text = re.sub(r"[^a-z\s]", "", text)
    # Tokenize and remove stopwords
    tokens = text.split()
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)
