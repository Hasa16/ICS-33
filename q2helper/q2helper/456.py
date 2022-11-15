#Author jchan20(Chan, Justin)



import re


# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt,
#   repattern1c.txt, and repattern2.txt.
# The patterns must be all on the first line, enclosed in ^ and $


def expand_re(pat_dict:{str:str}):
    string = re.compile('#(\w)#')
    print(string)


def multi_search(pat_file : open, text_file : open) -> [(int,str,[int])]:
    pass
#printing the file
print(multi_search(open('pats1.txt'),open('texts1.txt')))




if __name__ == '__main__':

    import driver
    driver.default_file_name = "bscq2S22.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
