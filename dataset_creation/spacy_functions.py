import spacy
nlp = spacy.load("en_core_web_sm")

def get_classes(text):
    if not text.endswith("."): text += "."
    classes = set()
    business_env = ["database", "record", "system", "information", "organization", "detail", "website", "computer"]
    doc = nlp(text)
    skip_next = False
    for i, token in enumerate(doc):
        # Check if we need to skip the token
        if skip_next:
            skip_next = False
            continue
        # Check if the token is a noun and do not appear in business_env
        if token.pos_ == "NOUN" and token.text not in business_env:
            # Check if the next token is a noun (compound)
            if token.dep_ == "compound":
                classes.add(token.lemma_ + '_' + doc[i+1].lemma_)
                skip_next = True # Skip the next token

            # Check if the next token is a gerund
            elif doc[i+1].tag_ == "VBG":
                classes.add(token.lemma_ + '_' + doc[i+1].text)
                skip_next = True # Skip the next token

            # if the next token is nor a noun nor a gerund, add the token as a class
            else: classes.add(token.lemma_)
        
        # Check if the token is a gerund
        elif token.tag_ == "VBG":
            # Check if the next token is a noun
            if doc[i+1].pos_ == "NOUN":
                classes.add(token.text + '_' + doc[i+1].lemma_)
                skip_next = True # Skip the next token
    
    return classes

def get_attributes(text):
    pass

def get_relations(text):
    pass

def get_inheritances(text):
    pass

text = "bottle opener"
classes = get_classes(text)
print(classes)
text = "a bottle can be oppened using a bottle opener"
classes = get_classes(text)
print(classes)
text = "bottle opener is used to open bottles"
classes = get_classes(text)
print(classes)
text = "question answering"
classes = get_classes(text)
print(classes)
text = "covering letter"
classes = get_classes(text)
print(classes)
text = "students write covering letter to apply for a job"
classes = get_classes(text)
print(classes)
text = "Every day, the mailman delivers registered mail in a geographical area assigned to him. The inhabitants are also associated with a geographical area. There are two types of registered mail: letters and parcels. As several letter carriers can intervene in the same area, we want, for each registered letter, the letter carrier who delivered it, in addition to the addressee"
classes = get_classes(text)
print(classes)