WRITE_ERR_STATEMENT = 'Cannot write to output file'
READ_ERR_STATEMENT = 'Cannot read from input file'

MAN_STATEMENT = '''Commands:
    man -- show commands
    show all words in lexicon -- disp-all
    add new word -- add
    remove word -- rem
    update word ipa -- update-ipa
    update word meaning -- update-mean
    update word part of speech -- update-pos
    begin search loop -- search
    search for word by ipa -- search-ipa
    search for word by ipa regex -- search-ipa-regex
    search for word by meaning -- search-mean
    search for word by definition contains -- search-about
    search for word by pos -- search-pos
    exit lex manager -- quit, q, exit, done     
'''

INTRO_STATEMENT = 'Welcome to the Lexicon Manager\n' + MAN_STATEMENT
EXIT_STATEMENT = 'Goodbye! :)' 
INPUT_ERROR_STATEMENT = 'Not a valid command :(\nType \'man\' to see valid commands.'

