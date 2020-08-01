# Conlanging | 11-423
0. Lexicon

  - lex\_funcs.py: functions corresponding to valid repl commands
  - lexicon.data.tsv: output from lexmgr.py, used to generate lexicon.pdf
  - lexicon.data.in.tsv: handwritten lexicon data (in case i heck up writing to lexicon.data.tsv)
  - lexicon.pdf: doc of words in language
  - lexicon.tex: tex for above
  - lexicon\_entry.py: class and enum for lexicon entries
  - lexmgr.py: starts repl
  - showlex.py: show all words in lexicon (not used for anything)
  - statements.py: common constant output messages
  - tsv\_funs.py: input to and output from .tsv files

- FUTURE TODO
- implement search
    - search by meaning
    - search by word
    - search by about
    - search by part of speech
    - search by regex
- update translation/ex sentences by index (change/delete)
- word lock (can't delete unless unlock)
- improve sorting of ipa symbols (low priority)
- search loop -- search + keywords to filter results one keyword at a time
- up arrow for repl history??? (necessary?)
- ^ https://docs.python.org/3/library/readline.html

0.1 Auto-Glossary
Generates a glossary from a .tsv/.csv file (used in portfolio)
---
1. Backstory (needs updating)
2. Cognitive Metaphors
3. Sounds & Syllables	(needs updating)
4. Time Sentences
5. Talking Clock
6. 50 Noun Phrases
7. Morphological Analyzer (FST/foma)
8. 100 Sentences
9. Chat Bot
10. Narrative
11. Portfolio
- FIX (NOT-) CLITICS
