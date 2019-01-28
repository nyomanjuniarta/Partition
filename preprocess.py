import sys


if __name__ == "__main__":
    path = sys.argv[1]
    file_out = open('binary.txt', 'w+')
    string_out = ''
    with open(path, 'r') as f:
        for line in f:
            numbers = line.replace('\n', '').replace('\r', '').split(',')
            for number in numbers:
                if int(number)<0:
                    string_out += '- '
                else:
                    string_out += '+ '
            file_out.write(string_out[:-1] + '\n')
            string_out = ''
