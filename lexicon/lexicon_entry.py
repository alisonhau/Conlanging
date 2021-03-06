from enum import Enum
class POS(Enum):
    NOUN = 1
    VERB = 2
    NUM = 1
    ADJ = 3
    PNOUN = 1
    UNKNOWN = -1

def pos_enum(enumstring):
    # add more parts of speech as tsv file expands
    if enumstring is None:
        return POS.UNKNOWN
    elif 'proper' in enumstring:
        return POS.PNOUN
    elif 'noun' in enumstring:
        return POS.NOUN
    elif 'num' in enumstring:
        return POS.NUM
    elif 'verb' in enumstring:
        return POS.VERB
    elif 'adj' in enumstring:
        return POS.ADJ
    else:
        return POS.UNKNOWN

class LexiconEntry:
    # allows for multiple translations (list)
    # allows for multiple examples (list)

    # init with at most one translation and one example
    def __init__(self, ipa=None, pos=None, trans='', eg=''):
        self.ipa = ipa
        self.pos = pos
        self.pos_enum = pos_enum(pos)
        self.trans = trans
        self.eg = eg

    # set eq and ne funcs
    def __eq__(self, other):
        # returns TRUE if same ipa and definition
        return self.ipa == other.ipa and self.pos == other.pos

    # change hashing function for set
    def __hash__(self):
        return hash("%s%s" % (self.ipa, self.pos)) 
    
    def __len__(self):
        return len(self.ipa)

    # GET funcs
    def get_ipa(self):
        return self.ipa
    def get_pos(self):
        return self.pos
    def get_pos_enum(self):
        return self.pos_enum
    def get_trans(self):
        return self.trans
    def get_eg(self):
        return self.eg

    # SET funcs
    def set_ipa(self, ipa):
        self.ipa = ipa
    def set_pos(self, pos):
        self.pos = pos
        self.pos_enum = pos_enum(pos)
    def set_trans(self, trans):
        self.trans = trans
    def set_eg(self, eg):
        self.eg = eg

    # work with eg as a list of string examples
    def set_eg_idx(self,idx, ex):
        eg_arr = self.eg.split("; ")
        eg_arr[idx] = ex
        self.eg = "; ".join(eg_arr)
    def get_eg_idx(self, idx):
        eg_arr = self.eg.split("; ")
        return eg_arr[idx]
    def add_eg(self, ex):
        self.eg += "; " + eg

    # work with trans as a list of possible translations
    def set_trans_idx(self, idx, t):
        trans_arr = self.trans.split("; ")
        trans_arr[idx] = t
        self.trans = "; ".join(trans_arr)
    def get_trans_idx(self, idx):
        trans_arr = self.trans.split("; ")
        return trans_arr[idx]
    def add_trans(self, t):
        self.trans += "; " + t

    # show entry contents
    def show_long_entry(self):
        if self.eg.strip() != '':
            print("\nIPA Latex:\t%s\nPart of Speech:\t%s\nEnglish Translation(s):\t%s\nExample Sentence(s):\t%s\n" % 
                    (self.ipa, self.pos, self.trans, self.eg) )
        else:
            print("\nIPA Latex:\t%s\nPart of Speech:\t%s\nEnglish Translation(s):\t%s\n" % 
                    (self.ipa, self.pos, self.trans))

    def show_line_entry(self):
        if self.eg.strip() != '':
            print("%s(%s):\t%s\t\te.g. %s" % (self.ipa, self.pos, self.trans, self.eg))
        else:
            print("%s(%s):\t%s" % (self.ipa, self.pos, self.trans) )
