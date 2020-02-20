from statements import MAN_STATEMENT
from lexicon_entry import LexiconEntry
from tsv_funcs import dict_to_tsv
# implement search loop

def accept_entry(entry_type):
    entry = input("%s: " % entry_type).strip()
    while entry == '':
        entry = input("Invalid %s.\n%s or \'quit\' to quit: " % (entry_type, entry_type)).strip()
        if entry == 'quit':
            print("Cancelled.")
            return None
    
    return entry

def add(lex_d):
    print("Add new word")
    new_ipa = accept_entry("IPA")
    if new_ipa is None: 
        return lex_d

    new_pos = accept_entry("Part of Speech")
    if new_pos is None: return lex_d

    new_trans = accept_entry("Closest English translation(s) (separate by ; if multiple)")
    if new_trans is None: return lex_d

    new_eg = input("Example sentence(s) (optional, separate by ; if multiple): ") or ''


    new_word = LexiconEntry(ipa=new_ipa, pos=new_pos, trans=new_trans, eg=new_eg)
    
    if (new_ipa, new_pos) in lex_d:
        print("%s is already in lexicon!" % new_word)
        lex_d[ (new_ipa, new_pos) ].show_long_entry()
        usr_update = input("Overwrite? ([Y]/n) ").strip().lower()
        while usr_update not in ['y', 'n', '']:
            usr_update = input("Overwrite? ([Y]/n) ").strip()
        if usr_update == 'n':
            print("New word discarded.")
    else:
        lex_d[ (new_ipa, new_pos) ] = new_word
        new_word.show_long_entry()
        print("Added!")

    return lex_d

def rem():
    return

def disp_all():
    return

def update_ipa():
    return

def update_mean():
    return

def update_pos():
    return

def search():
    return

def search_ipa():
    return

def search_ipa_reg():
    return

def search_mean():
    return

def search_about():
    return

def search_pos():
    return

def man(lex_d):
    print(MAN_STATEMENT)
    return lex_d
