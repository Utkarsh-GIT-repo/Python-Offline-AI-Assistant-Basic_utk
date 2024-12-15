import spacy

nlp = spacy.load("en_core_web_sm")
text = "Tell me the weather today"
doc = nlp(text)

for token in doc:
    print(f'{token.text}  -> {token.pos_}')