import sys
import os
import subprocess as subp

filetypes = {
          '.htm':      ['HTML'],
          '.md':       ['markdown', 'pandoc'],
          '.markdown': ['markdown'],
          '.mkd':      ['markdown'],
          '.docx':     ['MS word document', 'pandoc', '-f', 'docx', '-t', 'plain'],
          '.doc':      ['MS word document'],
          '.pptx':     ['MS powerpoint'],
          '.PPTX':     ['MS powerpoint'],
          '.ppt':      ['MS powerpoint'],
          '.ppsx':     ['MS powerpoint'],
          '.potx':     ['MS powerpoint template'],
          '.dotx':     ['MS word document template'],
          '.xlsm':     ['MS macro-enabled spreadsheet'],
          '.odf':      ['open document formula'],
          '.odp':      ['open document presentation'],
          '.ods':      ['open document spreadsheet'],
          '.odt':      ['open document text'],
          '.ott':      ['open document text template'],
          '.txt':      ['plain text', 'cat'],
          '.txx':      ['plain text'],
          '.xt':       ['plain text'],
          '.pdf':      ['portable document format'],
          '.PDF':      ['portable document format'],
          '.rtf':      ['rich text format'],
          '.tex':      ['TeX'],
         }
   
skip = ['.git',
        '__pycache__',
        '.plugins'
       ]

_exts = []

def conv(path):
    fnam, fext = os.path.splitext(path)
    if fext not in filetypes:
        print(f'WARNING: unknown file type {fext}, cannot convert {path}, skipping')
        return None
    converter = filetypes[fext]
    if len(converter) < 2:
        print(f'WARNING: no converter defined for file type {fext}, skipping')
        return None
    command = converter[1:] + [path]
    return subp.Popen(command, stdout=subp.PIPE)

def finddocs(d):
    for e in os.listdir(d):
        path=f'{d}/{e}'
        ext = os.path.splitext(e)[1]
        global _exts
        if ext not in _exts:
            _exts.append(ext)
        if e not in skip and os.path.isdir(path):
            finddocs(path)
        else:
            if ext in filetypes:
                print(path)
            else:
                pass

def main(args):
    if len(args) > 0:
        for d in args:
            finddocs(d)
    else:
        finddocs('.')

if __name__ == '__main__':
    main(sys.argv[1:])
