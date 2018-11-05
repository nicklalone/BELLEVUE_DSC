import sys

def main(input,output):
    with open(input, encoding='ISO-8859-1') as f:
        text = f.read()

    with open(output, 'w', encoding = 'UTF-8') as f:
        f.write(text)

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print('Requires 2 files:  <input> and <output>')
        print(len(args))
    else:
        main(str(args[1]), str(args[2]))
