# Regular expression

Regular expressions are a domain specific [language](Languages/Languages.md) for the concise description and [parsing](Parsing.md) of [regular Languages](Regular%20Languages.md). 

Regular languages officially start and end with /. So you have /regular expression/. Often you leave these / out.

So let's have a regular expression for god. The regular expression is /god/. 

The grammar for this language looks like this:

- S → gA
- A → oB
- B → d

Regular languages can be expressions in regular expressions which can be expressed in [finite state automata](finite%20state%20automata.md). This is great because this makes regular expressions really fast to parse.

## Symbols
You can parse symbols at a position by just including them in the regular expression /hello/ [parses](Parsing.md) the word hello. But what if we want to parse multiple words. Then we have to define a regular expression where one position of the sentence can have multiple symbols. This is done with symbol ranges.

### Symbol Ranges

Now you can have groups at any position. So if we want to pare: [god, bod] then we can have a regular expression like this: /[gb]od/. This is like having a regular grammar rule like this. 

- S → gA
- S → bA
- A → oB
- B → d

There is special syntax for ranges /[a-z]od/ here we can parse any lowercase letter of the [alphabet](Alphabet.md) followed by od. These ranges are defined by the [ASCII](https://en.wikipedia.org/wiki/ASCII) number of the symbol which happens to be convenient. Some common ranges:
- [A-z] is all letters lowercase uppercase
- [0-9] is all numbers 0 to 9 
- [4-7] is all numbers 7 to  7. 

### The wildcard
If you don't care what the symbol of a position in the word is then you can use the . wildcard. So /h.i/ can match hai hoi hbi etc. The only thing the . does not match with is a newline character. This is like an enter or maybe \\n. 

### Negation
If you use ^ at the start of a character range than everything that is not this range matched. So you say [\^0-4] then everything that is not in the set $\set{0,1,2,3,4}$ is parsed. 


## Counters (repeating)
Often you want to repeat certain parts in a parse. This can be done with counters. 

### One or more
If something has to occur once or more than we can use the +.

So /so+/ will parse so, soooo, sooo but not s because o has to appear at least once. 

### Zero or more
Sometimes you want to check that the same part repeats sometimes. You can just define that like this: /aaaao/ but what if you don't know how often the a will appear? Then there are special symbols for this. /a* o/ will parse a string that starts with zero or more a's followed by a space followed by an o. 

This is for instance how we can parse so and sooooo as the same word. /so*/ However this also parses s because * means zero or more. 

### Zero or once 
Sometimes you have something optional that can occur or not. For instance in someone's last name. This is also sometimes called the optional. You can specify this with a ? So if you have /hi?/ then it would parse both h and hi.

### Custom repeat 
You can also define custom ranges. If we only want to parse a so with 4 to 10 o then we can say /so{4,10}/. The ? is a shortcut for {0,1}. If you have {n,m} n is the minimum number it has to appear and m is the maximum it can appear. 

### Combining with symbol ranges
You can use +, * , ? and {} with character ranges as well. So you can say /age:[0-9]{1,3}/ to parse any string like: "age:32" or "age:120".  

Or let's say /d[a-z]+d/. This parses any string starting and ending with a d with one or more lowercase letter in between them.

## Markers (End and start of the line)
^ can also mean start of the string where $ means end of the string line. This is based on newline characters. This means that something it only parsed if it is at the start or end of a line. So if you have /^hi/ then it will only parse something like:

**hi** there but it won't parse this hi

## Escaping

So far we defined special characters like . ? \* + {} [] and there are more like ^{ and $ which mean end of string start of string or ^ can also mean negation. However maybe you want to literally check for these characters. When you want this you have to put \ before the special character to indicate this. So you could use /.+\./ to check if sentences end with a string. The . is escaped here. Or what if you want to check for something like [1,2,3,4] then you have to do /\\[[0-9, ]\*\ \]/. Basically you want to literally check for the \[ and \] characters. Note that this also matches \[,9,9,9]\ we need groups to fix this.

### Special escapes
If you escape things that are letters so only a literal meaning you get opposite. So \\n is a new line (very common thing). But \\t is a tab or \\b is a word boundary for instance. A word boundary is anything that is not a letter, digit or underscore. Often the opposite of this selection is the capital version of this so \\B only match word boundary. These can be very useful. You can also use these special escapes in ranges like: [\\b] is the same as [A-z0-9_] is the same as \\b.


## Grouping
Often you want to repeat longer productions. In this case you can use groups. A group is (). So you can say (ha)+ which means the string ha repeated. So that can match ha, haha, hahaha, but not hah. These groups can contain anything we defined before, so you can have something like:

`/\[([0-9],)*\]/` which matches  \[\] and also  \[1,2,4,\]

The point of grouping is that it involves multiple characters. 

### Capture groups
Any time you define a group you can refer back to it by using the index with a \\ in front. The index is just the number that you defined the group as. 

So if you have /a(b)\\1/ then this matches abb. You repeat the group with the b again. You could also have /(a)(b)\\2\\1/ this would match abba. 

Now this is the thing what the \\1 has to match what you found in the group! So if you define /my_age:([0-9]{1-3})-I_am_\\1_years_old\\./ Then this can match: my_age:12,I_am_12_years_old. But it couldn't match my_age:12,I_am_33_years_old. Because the capture group and the referral back to it are not the same! So the result is really stored in memory. This is also great if you want to get the results of the group later.

## Actions

### Substitution (replace)
If you start your regular expresion with an s you define a replacement. Something like this for instance replaces one or more white spaces with a tab.

`s/ +/\t/` The s indicates replace the first block by the second block. The block is defined by what's between the / / .

You can add a g at the end to do this everywhere. This means global. So then you get `s/ +/\t/g`.

Or lets say you have: s/[0-9]/|number|/g this would replace:

Counting goes like 1, 2, 3, 4, 5!
with 
Counting goes like |number|,|number|,|number|,|number|,|number|!

If you don't have the g it would go to:

Counting goes like |number|, 2, 3, 4, 5!

You can also replace by capture group!

# Online resources
You can use websites to test your regular expressions. For instance this one is usefull: 

https://regex101.com

Play around with it. This website can also export Python code so that is pretty cool. 

This is a website I made to obfuscate minecraft behavior packs. It also uses a lot of regular expressions to figure out what to replace. https://minecraft-obfuscator.dev 

## Example of email regex

>```(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])```

This one works for 99.99 % of all emails.