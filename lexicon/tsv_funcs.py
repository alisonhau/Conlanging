import csv
from lexicon_entry import LexiconEntry, POS
from statements import WRITE_ERR_STATEMENT, READ_ERR_STATEMENT

LEX_NUM_COLS = 4
BLANK_TSV_LINE = '\t' * (LEX_NUM_COLS-1) + '\n'

def tsv_to_dict(infile):
    lex_dict = dict()
    
    with open(infile, 'r') as lexfile:
        lexfile = csv.reader(lexfile, delimiter='\t')
        header = next(lexfile)
        numlines = 1    # line nos. start at 1, skip header line
        for line in lexfile:
            if line[0] == '': continue
            numlines += 1
            if len(line) == 3:
                new_entry = LexiconEntry(line[0], line[1], line[2])
                lex_dict[(new_entry.get_ipa(), new_entry.get_pos())] = new_entry
            elif len(line) >= 4:
                new_entry = LexiconEntry(line[0], line[1], line[2], line[3])
                lex_dict[(new_entry.get_ipa(), new_entry.get_pos())] = new_entry
            else:
                print("tsv_to_dict: Entry on line %s has insufficient fields" % (numlines))
                print(line)
        
    return lex_dict, header

def find_first_char(word):
    if word == '': return ''
    if word[0] == '\\':
        return word.index(' ')
    return word[0]

def dict_to_tsv(outfile, output_dict, output_header):
    sorted_output = sorted(output_dict)
    with open(outfile, 'w') as lexfile:
        lexfile.write('\t'.join(output_header)+'\n')
        prev_first_char = find_first_char(sorted_output[0][0])
        for entry in sorted_output:
            first_char = find_first_char(entry[0])
            if first_char != prev_first_char:
                lexfile.write(BLANK_TSV_LINE)
            ipa = output_dict[entry].get_ipa().strip()
            pos = output_dict[entry].get_pos().strip()
            trans = output_dict[entry].get_trans()
            ex = output_dict[entry].get_eg()
            lexfile.write('%s\t%s\t%s\t%s\n' % (ipa, pos, trans, ex)) 
            prev_first_char = first_char

    return

