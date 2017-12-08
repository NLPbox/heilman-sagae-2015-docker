
# heilman-sagae-2015-docker

This docker container allows you to build, install and run the
[Heilman and Sagae (2015) RST discourse parser](https://github.com/EducationalTestingService/discourse-parsing)
in a docker container.

## Building / Installing heilman-sagae-2015

```
git clone https://github.com/NLPbox/heilman-sagae-2015-docker
cd heilman-sagae-2015-docker
docker build -t heilman-sagae-2015 .
```

## Running heilman-sagae-2015

To test if parser works, just run ``docker run heilman-sagae-2015``.
To run the parser on the file ``/tmp/input.txt`` on your
local machine, run:

```
docker run -v /tmp:/tmp -ti heilman-sagae-2015 /tmp/input.txt
```

## Example Input

Henryk Szeryng (22 September 1918 - 8 March 1988) was a violin virtuoso 
of Polish and Jewish heritage.

He was born in Zelazowa Wola, Poland. Henryk started piano and harmony 
training with his mother when he was 5, and at age 7 turned to the 
violin, receiving instruction from Maurice Frenkel. After studies with 
Carl Flesch in Berlin (1929-32), he went to Paris to continue his 
training with Jacques Thibaud at the Conservatory, graduating with a 
premier prix in 1937.

He made his solo debut in 1933 playing the Brahms Violin Concerto. From 
1933 to 1939 he studied composition in Paris with Nadia Boulanger, and 
during World War II he worked as an interpreter for the Polish 
government in exile (Szeryng was fluent in seven languages) and gave 
concerts for Allied troops all over the world. During one of these 
concerts in Mexico City he received an offer to take over the string 
department of the university there.

In 1946, he became a naturalized citizen of Mexico.

Szeryng subsequently focused on teaching before resuming his concert 
career in 1954. His debut in New York City brought him great acclaim, 
and he toured widely for the rest of his life. He died in Kassel.

Szeryng made a number of recordings, including two of the complete 
sonatas and partitas for violin by Johann Sebastian Bach, and several 
of sonatas of Beethoven and Brahms with the pianist Arthur Rubinstein. 
He also composed; his works include a number of violin concertos and 
pieces of chamber music.

He owned the Del Gesu "Le Duc", the Stradivarius "King David" as well 
as the Messiah Strad copy by Jean-Baptiste Vuillaume which he gave to 
Prince Rainier III of Monaco. The "Le Duc" was the instrument on which 
he performed and recorded mostly, while the latter ("King David" Strad) 
was donated to the State of Israel.

## Example Output

```
{"edu_tokens": [["Henryk", "Szeryng"], ["(", "22", "September", "1918", 
"-", "8", "March", "1988", ")"], ["was", "a", "violin", "virtuoso", 
"of", "Polish", "and", "Jewish", "heritage", "."], ["He", "was", 
"born", "in", "Zelazowa", "Wola", ",", "Poland", "."], ["Henryk", 
"started", "piano", "and", "harmony", "training", "with", "his", 
"mother"], ["when", "he", "was", "5", ","], ["and", "at", "age", "7", 
"turned", "to", "the", "violin", ","], ["receiving", "instruction", 
"from", "Maurice", "Frenkel", "."], ["After", "studies", "with", 
"Carl", "Flesch", "in", "Berlin"], ["(", "1929-32", ")", ","], ["he", 
"went", "to", "Paris"], ["to", "continue", "his", "training", "with", 
"Jacques", "Thibaud", "at", "the", "Conservatory", ","], ["graduating", 
"with", "a", "premier", "prix", "in", "1937", "."], ["He", "made", 
"his", "solo", "debut", "in", "1933"], ["playing", "the", "Brahms", 
"Violin", "Concerto", "."], ["From", "1933", "to", "1939"], ["he", 
"studied", "composition", "in", "Paris", "with", "Nadia", "Boulanger", 
","], ["and", "during", "World", "War", "II", "he", "worked", "as", 
"an", "interpreter", "for", "the", "Polish", "government", "in", 
"exile"], ["(", "Szeryng", "was", "fluent", "in", "seven", "languages", 
")"], ["and", "gave", "concerts", "for", "Allied", "troops", "all", 
"over", "the", "world", "."], ["During", "one", "of", "these", 
"concerts", "in", "Mexico", "City", "he", "received", "an", "offer"], 
["to", "take", "over", "the", "string", "department", "of", "the", 
"university", "there", "."], ["In", "1946", ",", "he", "became", "a", 
"naturalized", "citizen", "of", "Mexico", "."], ["Szeryng", 
"subsequently", "focused", "on", "teaching"], ["before", "resuming", 
"his", "concert", "career", "in", "1954", "."], ["His", "debut", "in", 
"New", "York", "City", "brought", "him", "great", "acclaim", ","], 
["and", "he", "toured", "widely", "for", "the", "rest", "of", "his", 
"life", "."], ["He", "died", "in", "Kassel", "."], ["Szeryng", "made", 
"a", "number", "of", "recordings", ","], ["including", "two", "of", 
"the", "complete", "sonatas", "and", "partitas", "for", "violin", "by", 
"Johann", "Sebastian", "Bach", ",", "and", "several", "of", "sonatas", 
"of", "Beethoven", "and", "Brahms", "with", "the", "pianist", "Arthur", 
"Rubinstein", "."], ["He", "also", "composed", ";"], ["his", "works", 
"include", "a", "number", "of", "violin", "concertos", "and", "pieces", 
"of", "chamber", "music", "."], ["He", "owned", "the", "Del", "Gesu", 
"\"", "Le", "Duc", "\"", ",", "the", "Stradivarius", "\"", "King", 
"David", "\"", "as", "well", "as", "the", "Messiah", "Strad", "copy", 
"by", "Jean-Baptiste", "Vuillaume"], ["which", "he", "gave", "to", 
"Prince", "Rainier", "III", "of", "Monaco", "."], ["The", "\"", "Le", 
"Duc", "\"", "was", "the", "instrument"], ["on", "which", "he", 
"performed"], ["and", "recorded", "mostly", ","], ["while", "the", 
"latter"], ["(", "\"", "King", "David", "\"", "Strad", ")"], ["was", 
"donated", "to", "the", "State", "of", "Israel", "."]], 
"scored_rst_trees": [{"score": -37.44206864647109, "tree": "(ROOT 
(nucleus:span (nucleus:span (nucleus:span (nucleus:span (nucleus:span 
(nucleus:same-unit (nucleus:span (text 0)) (satellite:elaboration (text 
1))) (nucleus:same-unit (text 2))) (satellite:elaboration 
(nucleus:joint (text 3)) (nucleus:joint (nucleus:span (nucleus:joint 
(nucleus:span (text 4)) (satellite:background (text 5))) (nucleus:joint 
(text 6))) (satellite:elaboration (text 7))))) (satellite:background 
(nucleus:same-unit (nucleus:span (text 8)) (satellite:elaboration (text 
9))) (nucleus:same-unit (nucleus:span (text 10)) (satellite:elaboration 
(nucleus:span (text 11)) (satellite:enablement (text 12)))))) 
(satellite:elaboration (nucleus:span (text 13)) (satellite:cause (text 
14)))) (satellite:elaboration (nucleus:span (nucleus:span (text 15)) 
(satellite:elaboration (nucleus:joint (text 16)) (nucleus:joint 
(nucleus:span (text 17)) (satellite:elaboration (text 18))) 
(nucleus:joint (text 19)))) (satellite:elaboration (nucleus:span (text 
20)) (satellite:elaboration (text 21))))) (satellite:elaboration 
(nucleus:span (nucleus:span (nucleus:joint (text 22)) (nucleus:joint 
(nucleus:span (text 23)) (satellite:temporal (text 24)))) 
(satellite:elaboration (nucleus:span (nucleus:span (nucleus:joint (text 
25)) (nucleus:joint (text 26))) (satellite:elaboration (nucleus:joint 
(text 27)) (nucleus:joint (nucleus:span (text 28)) 
(satellite:elaboration (text 29))))) (satellite:elaboration 
(nucleus:span (text 30)) (satellite:elaboration (text 31))))) 
(satellite:elaboration (nucleus:span (nucleus:span (text 32)) 
(satellite:elaboration (text 33))) (satellite:elaboration 
(nucleus:same-unit (nucleus:span (text 34)) (satellite:elaboration 
(nucleus:joint (text 35)) (nucleus:joint (text 36)))) 
(nucleus:same-unit (nucleus:same-unit (nucleus:span (text 37)) 
(satellite:elaboration (text 38))) (nucleus:same-unit (text 
39)))))))"}]}
```

# Citation

Heilman, Michael and Sagae, Kenji (2015).
[Fast Rhetorical Structure Theory Discourse Parsing](https://arxiv.org/abs/1505.02425)
arXiv preprint arXiv:1505.02425
