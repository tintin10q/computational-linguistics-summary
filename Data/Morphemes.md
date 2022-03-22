# Morphemes
Morphemes are the smallest meaning-bearng unit of languages. But this is controversial. 

So when doing [Lemmatization](Lemma.md) you turn a word into its lemma form. The lemma of apes is ape. Here you removed ths 's'. The parts you remove every are **affixes** and the part that stays behind is the **stem**. Both stems and affixes are **morphenes**. 

- **Stems** is the mean meaning bearing unit in a word.
- **Affixes** are the strings that modify stems in some way.

For something to be a morphene it has to have meaning. For instance if you have walk then if you remove anything of this:  

`['alk', 'Tlk', 'Tak', 'Tal', 'lk', 'ak', 'al', 'k', 'l', 'k', 'a', 'l', 'a', 'lk', 'Tk', 'Tl', 'k', 'l', 'k', 'T', 'l', 'T', 'ak', 'Tk', 'Ta', 'k', 'a', 'k', 'T', 'a', 'T', 'al', 'Tl', 'Ta', 'l', 'a', 'l', 'T', 'a', 'T']`

These all have no meaning. 

## Stemming

Stemming is when you remove all the affixes of a stem. It doesn't have to be the same as lematization. Because you don't have to go to the dictionary version. For instance with iregular verbs. Broke is the past version of break. However, both are stems. So if you do stemming on broke you get broke of you do stemming on break you get break if you do stemming on breaking you get break. If you do lemmatization on broke you get break. 

So stemming only removes affixes, lemmatization goes to the lemma. 

Sometimes a word with affixes occures seperatly in the dictionary. For instace the word "lemmatization". If you stem this you get lemma. If you lemmatize it you get "lemmatization" because lemmatization also occures sepeartly in the dicationary (with the affixes). 

So sometimes stemming is more disruptive sometimes lemmatization is more disruptive it depends on the dictionary and the kind of affixes. 

# Kinds of affixes

## Inflectional
The inflectional affixes don't create new words in the dictionary. This means that they are removed by lemmatization. They tent to encode number, tense, aspect, gender, case. Inflectional affixes are fully productive. This means that with any (regular) verb, noun etc you can add these to indicate the meaning. You can always add +ed to a verb to indicate the past. You can always indicate more then one by adding an -s. One  human multiple humans. 

So words of the same class can get the same inflectional affixes. These affixes are morphones. Irregular words can not. For instance one sheep and multiple sheep.

## Derivational 
The derivational affixes create new words in the dictionary. They do this by either chaning the grammatical category of the word which changes the meaning of the word. Or by encoding things like negation, nominalization, reiteration ... which directly changes the meaning of the word.

- Happy → unhappy 
	- Stem: happy
	- Lemmatization: unhappy
- Happy → happy + ness → happiness
	- Stem: happy
	- Lemmatization: happyness
- Happy → un + happy + ness → unhapiness 
	- Stem: happy
	- Lemmatization: unhappiness

# Compounding 
Sometimes you can also combine stems togeter to produce new meaning. For instance 
- fire + fighter = firefighter
- tele + vision = television
- moter + bike = moterbike

These types of words are called compounds. In Dutch it's called dubbel worden, double words. 

The meaning of a compound can be very clear and easy to guess to very opaque where the meaning is not very much if at all releated to the consituents.

# Morphological complexity
Words can have different morphological complexity. A word is <b><u>Mono</u>morphemic</b> when they only consist of a single morpheme (plus possible inflectional morphemes) 

<b><u>Poly</u>morphemic</b> is when the word includes derivational affixes or are compounts. 
