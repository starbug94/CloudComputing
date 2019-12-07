'''
Natural Language Sentiment Analysis
    using Google Cloud Natural Language API


Accepted file types:
    - .xls/.xlsx (! without a header)
        for multi-analysis where each cell is analyzed individually
    - .txt for a single analysis on the whole file

Accepted languages(detected automatically) for Sentiment Analysis:
    Language                            ISO-639-1 Code
    Chinese (Simplified)	                zh
    Chinese (Traditional)	                zh-Hant
    English	                                en
    French	                                fr
    German	                                de
    Italian	                                it
    Japanese	                            ja
    Korean	                                ko
    Portuguese (Brazilian & Continental)	pt
    Spanish	                                es
https://cloud.google.com/natural-language/docs/languages


SCORE of the sentiment ranges between -10 (negative) and 10 (positive)
    and corresponds to the overall emotional leaning of the text.

MAGNITUDE indicates the overall strength of emotion
    (both positive and negative) within the given text, between 0.0 and +inf.


Example usage:
    python3 analyze.py test.xls
'''

# To show progress bar
from tqdm import tqdm
import check
import excel as xl
import google_nl as g
import print_results



if __name__ == '__main__':
    # If check won't go through, program will show error msg and exit
    FILE, NEW_FILE, TYPE = check.arguments()
    # FILE = "test.xlsx"
    # NEW_FILE = "test2.xlsx"

    print("fffffffffffffffff")
    print(FILE)
    print(NEW_FILE)
    #
 
    # print(g.analyze_sentiment("좋다"))
    # print(g.analyze_sentiment("나쁘다"))
    # print(g.analyze_sentiment("love"))
    # print(g.analyze_sentiment("hate"))
    # print(g.analyze_sentiment("겨울왕국 재미없어요"))
    # print(g.analyze_sentiment("wtf"))
    # print(g.analyze_sentiment("fucking jejus"))

    if TYPE == '.txt':
        TXT = open(FILE, "r")
        SEN = g.analyze_sentiment(TXT.read())
        TXT.close()
        print_results.text(SEN)
    elif TYPE == 'excel':
        DATA, ROWS_NB = xl.get_xl(FILE, NEW_FILE)
        print(range(ROWS_NB));
        print(tqdm(range(ROWS_NB)))

        for ROW in tqdm(range(ROWS_NB)):
            print(ROW)
            print("######")
            print(DATA.iloc[ROW, 0])

            SEN = g.analyze_sentiment(DATA.iloc[ROW, 0])
            print(SEN)
            DATA.iloc[ROW, 1] = round(SEN.score, 1) * 10
            DATA.iloc[ROW, 2] = round(SEN.magnitude, 1)
        DATA.to_excel(NEW_FILE, index=None)
        print_results.excel(NEW_FILE)

# Project files
