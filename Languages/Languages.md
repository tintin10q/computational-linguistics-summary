# Languages

Languages are the set of valid combinations of an [alphabet](Alphabet.md) following the [grammar](Grammar.md). The process of proving that a language belongs to a language is called **parsing**. 

Let's do another definition:

A language is a set of [sentences](../Data/Sentences.md) build from an [alphabet](Alphabet.md) which for some reason we call correct. This reason is that the sentences follow the grammar rules we defined for the language. 

[Parsing](parsing.md) is the act of proving that some input belongs to a language (set). 

# Types of languages 
**[Natural languages](Natural%20languages.md)** are languages where you can also have sentences that are almost correct, and they will still be accepted mostly without any complaints. **Formal Languages** are languages where every sentence has to be from the set of correct sentences otherwise there will be complaint (by the compiler).


**Formal Language** A formal language is a language where you **have** to follow the rules, and you can not deviate. This means that you can always use the rewrite rules. Every sentence has to be from the set of correct sentences otherwise there will be complaint (by the compiler). There are different classes of formal languages based on the rules that the grammar may use.  For instance, you have regular languages and context free languages. These types of grammars are defined by the [Chompsky heirarchy](chompsky%20heirarchy.md)
