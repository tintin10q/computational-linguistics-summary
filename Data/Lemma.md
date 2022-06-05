# Lemma
A lemma is the dictionary entry of a word. So this is always a word, not just a character. Types and tokens can also be characters. So if you have “The ape shared bananas with the other apes” then ape and apes here are the same lemma. It is like removing the 's and like the extra things. These extra modifier things are called [Morphemes](Morphemes.md). Walking and walk are considered the same lemma. Is and am are also considered the same lemma. 

The citation form is a [synonym](../Languages/Synonyms.md) for lemma. 

## Word forms 

Word forms are the other possible versions of a lemma, which mean the same thing. For instance, the verb *sing*. Sing is the lemma for the word forms sing, sang and sung. 

## Lemmatization

Lemmatization is the process of **reducing each word-form** found in a corpus **to its corresponding lemma**.

### Examples
- Went → Go
- Geese → Goose
- Best → Good
- Talked → Talk
- Apples → Apple
- Biked → Bike
- Biking → Bike
- Bike → Bike

You go to the base form. Sometimes the base is language specific. Lemmatizers are specific for languages. [Here](./data.md) is an example of how lemmas compare to tokens and types.

## Word sense 

The meaning of a word can be considered separately from the word symbol. **The meaning of a word is captured in the word sense**. A word sense can be expressed in text. So the word sense of apple is a mostly round fruit. Interestingly, in this explanation I relied on other word senses for instance fruit to explain the word sense of apple.  

### Polysemous – Multiple meanings
Sometimes a lemma can have multiple word senses. For instance, apple can also refer to fruit or an organization. When this occurs, a lemma is called **polysemous** (have multiple senses). These multiple meanings lead to [ambiguity](../Languages/Ambiguity.md). In the book on page 103 the example of mouse is given. A mouse can be a rodent or an input device for a computer.  Each of these separate meanings is called a **word sense**. 