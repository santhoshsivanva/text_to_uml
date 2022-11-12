import spacy
nlp = spacy.load("en_core_web_sm")

def get_classes(text):
    classes = set()
    business_env = ["database", "record", "system", "information", "organization", "detail", "website", "computer"]
    noun_or_gerund  = ["NOUN"]
    doc = nlp(text)
    for token in doc:
        if token.pos_ in noun_or_gerund and token.text not in business_env:
            classes.add(token.lemma_)
    return classes

text = "Every day, the mailman delivers registered mail in a geographical area assigned to him. The inhabitants are also associated with a geographical area. There are two types of registered mail: letters and parcels. As several letter carriers can intervene in the same area, we want, for each registered letter, the letter carrier who delivered it, in addition to the addressee."
classes = get_classes(text)
print(classes)