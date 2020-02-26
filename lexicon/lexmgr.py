import lex_funcs as LexFuncs
import tsv_funcs as TSVFuncs
from statements import INTRO_STATEMENT, EXIT_STATEMENT, INPUT_ERROR_STATEMENT

# FUTURE TODO
# implement search
    # search by meaning
    # search by word
    # search by about
    # search by part of speech
    # search by regex
# update translation/ex sentences by index (change/delete)
# word lock (can't delete unless unlock)
# improve sorting of ipa symbols (low priority)
# search loop -- search + keywords to filter results one keyword at a time
# up arrow for repl history??? (necessary?)
# ^ https://docs.python.org/3/library/readline.html

IN_LEX_FILE = 'lexicon-data.tsv'
OUT_LEX_FILE = 'lexicon-data.tsv'

EXIT_KEYS = ['quit', 'q', 'exit', 'done']
FUNCTION_KEYS = {
        'add': LexFuncs.add,
        'rem': LexFuncs.rem,
        'show': LexFuncs.show,
        'show-long': LexFuncs.show_long,
        'update-ipa': LexFuncs.update_ipa,
        'update-mean': LexFuncs.update_mean,
        'update-eg': LexFuncs.update_eg,
        'update-pos': LexFuncs.update_pos,
        'search': LexFuncs.search,
        'search-ipa': LexFuncs.search_ipa,
        'search-ipa-reg': LexFuncs.search_ipa_reg,
        'search-mean': LexFuncs.search_mean,
        'search-about': LexFuncs.search_about,
        'search-pos': LexFuncs.search_pos,
        'man': LexFuncs.man,
        }

PROMPT = '> '
def print_statement(statement):
    print(statement)

def main():
    print_statement(INTRO_STATEMENT )

    lex_dict, lex_head = TSVFuncs.tsv_to_dict(IN_LEX_FILE)

    last_cmd = ''

    # repl
    usr_input = input(PROMPT).strip()
    
    while usr_input not in EXIT_KEYS:
        if usr_input == '':
            usr_input = last_cmd
        if usr_input != '':
            last_cmd = usr_input
            if usr_input not in FUNCTION_KEYS:
                print_statement(INPUT_ERROR_STATEMENT)
            else:
                lex_dict = FUNCTION_KEYS[usr_input](lex_dict)
                TSVFuncs.dict_to_tsv(OUT_LEX_FILE, lex_dict, lex_head)
        
        usr_input = input(PROMPT).strip()

    TSVFuncs.dict_to_tsv(OUT_LEX_FILE, lex_dict, lex_head)
    print_statement(EXIT_STATEMENT)

if __name__ == '__main__':
    main()
