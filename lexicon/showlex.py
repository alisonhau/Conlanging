import csv 
from lexicon_entry import LexiconEntry, POS

# FUTURE TODO
# implement search
    # search by meaning
    # search by word
    # search by contains
    # search by regex
# implement add
# implement remove
# implement lock (can't remove?)
# implement update
    # spelling
    # meaining
    # part of speech
# implement sorting for ipa (dictionary order for different symbols

LEX_FILE = 'lexicon.tsv'

def print_intro():
    # print("lexicon commands:\n\tshow lexicon -- show\n\tadd new word -- add\n\tremove word -- remove\n\tupdate word spelling -- update\n\tupdate word meaning\n\tupdate word POS\n\tsearch for word -- search")
    return

def main():
    lex_set = set()
    print_intro()

    with open(LEX_FILE, 'r') as lexfile:
        lexfile = csv.reader(lexfile, delimiter='\t')
        next(lexfile)
        numlines = 1    # line nos. start at 1, skip header line
        for line in lexfile:
            numlines += 1
            if len(line) == 3:
                lex_set.add(LexiconEntry(line[0], line[1], line[2]))
            elif len(line) >= 4:
                lex_set.add(LexiconEntry(line[0], line[1], line[2], line[3]))
            else:
                print("Entry on line %s has insufficient fields" % (numlines))
                print(line)
        
        for entry in sorted(lex_set, key=lambda e: e.get_trans()):
            entry.show_long_entry()

        print("\nNumber of entries: %s" % (numlines-1))

if __name__ == '__main__':
    main()
