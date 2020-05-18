import csv

TEXFILE = "np_template.tex"
CSVFILE = "np_data.csv"

BEGIN_ENUMERATE = "\\begin{enumerate}"
END_ENUMERATE = "\\end{enumerate}" 

GLOSSTEMP = '''\item
\t\\trigloss[preamble={\\textipa{%s}}]
\t\t{%s}
\t\t{%s}
\t\t{%s}
\t\t{%s}'''

TEXTIPATEMP = "\\textipa{%s}"

def makegloss(line):
    gloss1 = " ".join( [ TEXTIPATEMP % (s.strip()) for s in line[1].strip().split(" ") ] )

    gloss_out = GLOSSTEMP % (line[0].strip(), gloss1, line[2].strip(), line[3].strip(), line[4].strip()) + "\n"

    return gloss_out

def read_n_print_csv(in_file, out_file):
    with open (out_file, 'w') as outwrite:
       outwrite.write(BEGIN_ENUMERATE + "\n")
       with open(in_file, 'r') as inread:
            inread = csv.reader(inread, delimiter = "%")
            header = next(inread)
        
            for np in inread:
                gloss = makegloss(np)
                outwrite.write(gloss)

            outwrite.write(END_ENUMERATE)

    print("read n print done")

def main():
    read_n_print_csv(CSVFILE, TEXFILE)

if __name__ == '__main__':
    main()
    
