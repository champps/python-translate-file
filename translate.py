import configparser, argparse

def get_args() -> argparse.ArgumentParser:
    #python translate.py originfile inifile.ini [[-fl] fromline] [[-tl] toline] [-i]
    args_parser = argparse.ArgumentParser()
    boolean=argparse.BooleanOptionalAction

    args_parser.add_argument("origin_file_path", help="this origen file path",type=str )
    args_parser.add_argument("ini_file_path", help="this ini file path",type=str)
    args_parser.add_argument('-c',dest="case_sensitive" ,help="case sensitive", action=boolean, default=False)
    #args_parser.add_argument('-r',dest="reverse" ,help="reverse translate",action=boolean, default=False)
    args_parser.add_argument("-fl", "--from_line", dest="from_line", help="from line int start 1",type=int, default=0)
    args_parser.add_argument("-tl", "--to_line", dest="to_line", help="to line int start with 1",type=int, default=0)
    args_parser.add_argument("-sh", "--show", dest="show", help="show the txt",type=int, action=boolean, default=1)
    args_parser.add_argument("-w", "--write", dest="write", help="write to origin file",type=int, action=boolean,  default=0)
    args_parser.add_argument("-o", "--output", dest="output", help="chose outher file to save output", default="")
    args_parser.add_argument("-b", "--backup", dest="backup", help="save backup file if you choose write", default=None)


    return args_parser.parse_args()



def read_origin_file(args) -> str:
    # read to dict
    # if we need append will read with configparser to auto fill ini file

    path_file = args.origin_file_path

    txt = open(path_file, "r").read()

    txt_split_list = [line.split()  for line in txt.split("\n")]


    #print("test = ", txt)

    #print(txt_lines)
    return txt_split_list, txt



def update_txt(txt,args, config) -> None:
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

def write_to_file(txt,origin_txt, args) -> None:

    txt_temp = txt

    txt = "\n".join([" ".join(line)  for line in txt])
    if args.show == True:
        txt_temp = [" ".join(line)  for line in txt_temp]
        #print (txt)
        for num, line in enumerate(txt_temp):
            print(num+1, line)

    if args.backup == "":
        open(args.origin_file_path+".bcakup", "w")
    elif args.backup:
        open(args.backup, "w")


    if args.write == True:
        #print(txt)
        open(args.origin_file_path, 'w').write(txt)

    if args.output:
        open(args.output, 'w').write(txt)
    print(args.output)

if __name__ == "__main__":
    args =get_args()

    config = configparser.ConfigParser()

    if args.case_sensitive:
        config.optionxform=str

    config.read(args.ini_file_path)

    txt, origin_txt  = read_origin_file(args)

    update_txt(txt, args,  config)

    write_to_file(txt, origin_txt,  args)

    #print(txt, args)
