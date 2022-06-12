import configparser, argparse

def get_args() -> argparse.ArgumentParser:
    #python translate.py originfile inifile.ini [[-fl] fromline] [[-tl] toline] [-i]
    args_parser = argparse.ArgumentParser()
    boolean=argparse.BooleanOptionalAction
    boolean

    args_parser.add_argument("origin_file_path", help="this origen file path")
    args_parser.add_argument("ini_file_path", help="this ini file path")
    args_parser.add_argument('-c',dest="case_sensitive" ,help="case sensitive", action=boolean, default=False)
    #args_parser.add_argument('-r',dest="reverse" ,help="reverse translate",action=boolean, default=False)
    args_parser.add_argument("-fl", "--from_line", dest="from_line", help="from line int start 1",type=int, default=0)
    args_parser.add_argument("-tl", "--to_line", dest="to_line", help="to line int start with 1",type=int, default=0)
    args_parser.add_argument("-sh", "--show", dest="show", help="show the txt",type=int, action=boolean, default=1)
    args_parser.add_argument("-w", "--write", dest="write", help="write to origin file",type=int, action=boolean,  default=0)
    args_parser.add_argument("-o", "--output", dest="output", help="chose outher file to save output", default="")

    return args_parser.parse_args()



def read_origin_file(args) -> str:
    # read to dict
    # if we need append will read with configparser to auto fill ini file
    path_file = args.origin_file_path

    txt_split_list = [line.split()  for line in open(path_file, "r").read().split("\n")]

    #print("test = ", txt)

    #print(txt_lines)
    return txt_split_list



def update_txt(txt, config) -> None:
    #config.add_section('DEFAULT')
    case_sensitive = args.case_sensitive
    from_line = args.from_line#1 if args.from_line else args.from_line
    to_line = args.to_line

    #print(from_line)
    if from_line == 0: from_line =1
    if to_line == 0:to_line = len(txt)

    keys= config['DEFAULT'].keys()

    for count_line, line in enumerate(txt):
        for count_word,word in enumerate(line):
            # not go out range
            if count_line >= from_line-1 and count_line < to_line:
                if case_sensitive == 0:
                    word = word.lower()
                # if find it and not None
                if word in keys:
                    value = config['DEFAULT'][word]
                    if value:
                        txt[count_line][count_word] = value

    #print("text after edit =", *txt)
    #print(list(config['DEFAULT'].keys()))

def write_to_file(txt, args) -> None:


    txt = "\n".join([" ".join(line)  for line in txt])
    if args.show == True:
        print(txt)

    if args.write == True:
        #print(txt)
        open(args.orignal_file_path, 'w').write(txt)

    if args.output:
        open(args.output, 'w').write(txt)
    print(args.output)

if __name__ == "__main__":
    args =get_args()

    config = configparser.ConfigParser()

    if args.case_sensitive:
        config.optionxform=str

    config.read(args.ini_file_path)

    txt  = read_origin_file(args)

    update_txt(txt, config)

    write_to_file(txt, args)

    #print(txt, args)
