from statements import MAN_STATEMENT
from lexicon_entry import LexiconEntry
from tsv_funcs import dict_to_tsv
# implement search loop

# helper funcs
def accept_entry(entry_type):
    entry = input("%s: " % entry_type).strip()
    while entry == '':
        entry = input("Invalid %s.\n%s or \'quit\' to quit: " % (entry_type, entry_type)).strip()
        if entry == 'quit':
            print("Cancelled.")
            return None
    
    return entry

def lex__search( lex_dictionary, field, target ):
   return
    
def accept_word_params():
    word_ipa = accept_entry("IPA")
    if word_ipa is None: 
        return None, None

    word_pos = accept_entry("POS")
    if word_pos is None:
        return None, None

    return word_ipa, word_pos

#

def add(lex_d):
    print("Add new word")
    new_ipa = accept_entry("IPA")
    if new_ipa is None: 
        return lex_d

    new_pos = accept_entry("Part of Speech")
    if new_pos is None: return lex_d

    new_trans = accept_entry("Closest English translation(s) (separate by ; if multiple)")
    if new_trans is None: return lex_d

    new_eg = input("Example sentence(s) (optional, separate by ; if multiple): ")

    new_word = LexiconEntry(ipa=new_ipa, pos=new_pos, trans=new_trans, eg=new_eg)
    
    if (new_ipa, new_pos) in lex_d:
        print("%s is already in lexicon!" % new_ipa)
        lex_d[ (new_ipa, new_pos) ].show_long_entry()
        usr_update = input("Overwrite? ([Y]/n) ").strip().lower()
        while usr_update not in ['y', 'n', '']:
            usr_update = input("Overwrite? ([Y]/n) ").strip()
        if usr_update == 'n':
            print("New word discarded.")
            return lex_d
    
    lex_d[ (new_ipa, new_pos) ] = new_word
    new_word.show_long_entry()
    print("Added!")

    return lex_d

def rem(lex_d):
    print("Remove word")
    deleted_ipa = accept_entry("IPA")
    if deleted_ipa is None: 
        return lex_d

    deleted_pos = accept_entry("Part of Speech")
    if deleted_pos is None: return lex_d

    if (deleted_ipa, deleted_pos) in lex_d:
        deleted_word = lex_d.pop( (deleted_ipa, deleted_pos) , None)
        deleted_word.show_long_entry()

        usr_conf = input("Delete? ([Y]/n) ").strip().lower()
        while usr_conf not in ['y', 'n', '']:
            usr_conf = input("Delete? ([Y]/n) ").strip()
        if usr_conf == 'n':
            lex_d[ (deleted_ipa, deleted_pos) ] = deleted_word
            print("Cancelled.")
        else:
            print("Deleted!")
    else:
        print("%s(%s) not found in dictionary." % (deleted_ipa, deleted_pos))
    
    return lex_d

def show(lex_d):
    lex_keys = sorted(lex_d)

    for key in lex_keys:
        lex_d[key].show_line_entry()

    print("%s entries" % (len(lex_keys)))

    return lex_d

def show_long(lex_d):
    lex_keys = sorted(lex_d)

    for key in lex_keys:
        lex_d[key].show_long_entry()

    print("%s entries" % (len(lex_keys)))

    return lex_d

def update_ipa(lex_d):
    print("Update word IPA.  Which word do you want to update?")
    word_ipa, word_pos = accept_word_params()
    if word_ipa is None or word_pos is None:
        return lex_d
   
    lex_word = lex_d.pop( (word_ipa, word_pos), None )
    if lex_word is None:
        print("%s(%s) not in lexicon.  To see all words in lexicon, use command \'show\'." % (word_ipa, word_pos))
        return lex_d
    
    lex_word.show_long_entry()

    new_ipa = accept_entry("\nUpdated IPA")
    if new_ipa is None: return lex_d

    lex_word.set_ipa(new_ipa)
    print("Proposed update: ")
    lex_word.show_long_entry()
    usr_update = input("Update? ([Y]/n) ").strip().lower()
    while usr_update not in ['y', 'n', '']:
        usr_update = input("Update? ([Y]/n) ").strip()
    if usr_update == 'n':
        lex_word.set_ipa(word_ipa)
        print("Update discarded.")
    else: 
        lex_word.show_long_entry()
        print("Updated!")
    
    lex_d[ (new_ipa, word_pos) ] = lex_word
    return lex_d


def update_pos(lex_d):
    print("Update word POS.  Which word do you want to update?")
    word_ipa, word_pos = accept_word_params()
    if word_ipa is None or word_pos is None:
        return lex_d
   
    lex_word = lex_d.pop( (word_ipa, word_pos), None )
    if lex_word is None:
        print("%s(%s) not in lexicon.  To see all words in lexicon, use command \'show\'." % (word_ipa, word_pos))
        return lex_d
    
    lex_word.show_long_entry()

    new_pos = accept_entry("\nUpdated POS")
    if new_pos is None: return lex_d

    lex_word.set_pos(new_pos)
    print("Proposed update: ")
    lex_word.show_long_entry()
    usr_update = input("Update? ([Y]/n) ").strip().lower()
    while usr_update not in ['y', 'n', '']:
        usr_update = input("Update? ([Y]/n) ").strip()
    if usr_update == 'n':
        lex_word.set_pos(word_pos)
        print("Update discarded.")
    else: 
        lex_word.show_long_entry()
        print("Updated!")
    
    lex_d[ (word_ipa, new_pos) ] = lex_word
    return lex_d


def update_mean(lex_d):
    print("Update word translations.  Which word do you want to update?")
    word_ipa, word_pos = accept_word_params()
    if word_ipa is None or word_pos is None:
        return lex_d
   
    lex_word = lex_d.pop( (word_ipa, word_pos), None )
    if lex_word is None:
        print("%s(%s) not in lexicon.  To see all words in lexicon, use command \'show\'." % (word_ipa, word_pos))
        return lex_d
    
    lex_word.show_long_entry()
    word_trans = lex_word.get_trans()

    new_trans = accept_entry("\nUpdated English translations")
    if new_trans is None: return lex_d

    lex_word.set_trans(new_trans)
    print("Proposed update: ")
    lex_word.show_long_entry()
    usr_update = input("Update? ([Y]/n) ").strip().lower()
    while usr_update not in ['y', 'n', '']:
        usr_update = input("Update? ([Y]/n) ").strip()
    if usr_update == 'n':
        lex_word.set_trans(word_trans)
        print("Update discarded.")
    else: 
        lex_word.show_long_entry()
        print("Updated!")
    
    lex_d[ (word_ipa, word_pos) ] = lex_word
    return lex_d

def update_eg(lex_d):
    print("Update example sentences.  Which word do you want to update?")
    word_ipa, word_pos = accept_word_params()
    if word_ipa is None or word_pos is None:
        return lex_d
   
    lex_word = lex_d.pop( (word_ipa, word_pos), None )
    if lex_word is None:
        print("%s(%s) not in lexicon.  To see all words in lexicon, use command \'show\'." % (word_ipa, word_pos))
        return lex_d
    
    lex_word.show_long_entry()
    word_eg = lex_word.get_eg()

    new_eg = accept_entry("\nUpdated example sentences")
    if new_eg is None: return lex_d

    lex_word.set_eg(new_eg)
    print("Proposed update: ")
    lex_word.show_long_entry()
    usr_update = input("Update? ([Y]/n) ").strip().lower()
    while usr_update not in ['y', 'n', '']:
        usr_update = input("Update? ([Y]/n) ").strip()
    if usr_update == 'n':
        lex_word.set_eg(word_eg)
        print("Update discarded.")
    else: 
        lex_word.show_long_entry()
        print("Updated!")
    
    lex_d[ (word_ipa, word_pos) ] = lex_word
    return lex_d


def search(lex_d):
    return

def search_ipa(lex_d):
    return

def search_ipa_reg(lex_d):
    return

def search_mean(lex_d):
    return

def search_about(lex_d):
    return

def search_pos(lex_d):
    return

def man(lex_d):
    print(MAN_STATEMENT)
    return lex_d
