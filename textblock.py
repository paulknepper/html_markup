# textblock.py--takes text from a file and divides into blocks for markup
import sys

def get_line(file):
    """
    This function ensures file ends with a '\n', without having to read the
    entire file into memory as a string in order to append the '\n', as you
    could potentially do in get_block.
    """
    for line in file:
        yield line
    yield "\n"

def get_block(file):
    block = ''
    for line in get_line(file):
        if line.strip(): 
            # if True there is text; add it to the block
            block += line  
        elif block: # you hit a line that was all white space, so end of block
            yield block.strip()
            block = ''  # reset block to empty


