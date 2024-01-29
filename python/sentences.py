# A code by Collins Ekpenyong Asikpo......... From Nigeria
import random

def main():
    # Print six sentences with different grammar combinations
    for _ in range(6):
        sentence = make_sentence()
        print(sentence)

def make_sentence(tense, plurality):
    determiner = get_determiner(plurality)
    noun = get_noun(plurality)
    verb = get_verb(tense, plurality)
    prepositional_phrase = get_prepositional_phrase(plurality)
    
    return f"{determiner} {noun} {verb} {prepositional_phrase}."

def get_determiner(plurality):
    determiners_singular = ["A", "One", "The"]
    determiners_plural = ["Some", "Many"]
    
    return random.choice(determiners_plural if plurality == "plural" else determiners_singular)

def get_noun(plurality):
    nouns_singular = ["cat", "man", "woman"]
    nouns_plural = ["girls", "dogs", "men"]
    
    return random.choice(nouns_plural if plurality == "plural" else nouns_singular)

def get_verb(tense, plurality):
    verbs_past_singular = ["laughed", "ate", "thought"]
    verbs_present_singular = ["laughs", "eats", "thinks"]
    verbs_future_singular = ["will laugh", "will eat", "will think"]
    
    verbs_past_plural = ["laughed", "ate", "thought"]
    verbs_present_plural = ["laugh", "eat", "think"]
    verbs_future_plural = ["will laugh", "will eat", "will think"]
    
    if tense == "past":
        return random.choice(verbs_past_plural if plurality == "plural" else verbs_past_singular)
    elif tense == "present":
        return random.choice(verbs_present_plural if plurality == "plural" else verbs_present_singular)
    elif tense == "future":
        return random.choice(verbs_future_plural if plurality == "plural" else verbs_future_singular)

def get_preposition():
    prepositions = ["in", "on", "under", "over", "between", "beside"]
    return random.choice(prepositions)

def get_prepositional_phrase(plurality):
    determiner = get_determiner(plurality)
    noun = get_noun(plurality)
    preposition = get_preposition()
    
    return f"{preposition} {determiner} {noun}"

if __name__ == "__main__":
    main()
