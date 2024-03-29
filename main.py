from __future__ import print_function

import classes


def start():
    document = classes.Document(input('what is the document ID? '), ['https://www.googleapis.com/auth/documents'])
    return document


def log(string):
    with open('logs.txt', 'w+', encoding='utf-8') as f:
        f.write(string)


def main():
    document = start()
    document.start()
    # print(document.data)
    print('The title of the document is: {}'.format(document.get().get('title')))
    while True:
        backticks = []
        while backticks == []:
            document.on_change()
            backticks = document.find_backticks()
        print(document.add_code_blocks(backticks))


def intel(thing):
    log(f"Size: {len(thing)}\nType: {type(thing)}\n---\n{thing}")
    print(f"Size: {len(thing)}\nType: {type(thing)}\n---\n{thing}")


if __name__ == '__main__':
    main()

