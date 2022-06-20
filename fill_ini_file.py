import configparser, argparse, re

def get_args() -> argparse.ArgumentParser:
    #python translate.py originfile inifile.ini [[-fl] fromline] [[-tl] toline] [-i]
    args_parser = argparse.ArgumentParser()
    boolean=argparse.BooleanOptionalAction

    args_parser.add_argument("origin_file_path", help="this origen file path")
    args_parser.add_argument("ini_file_path", help="this ini file path")
    args_parser.add_argument('-c',dest="case_sensitive" ,help="case sensitive",
                             action=boolean, default=False)
    args_parser.add_argument('-l',"--load_ini_file",dest="load_ini_file" ,help="load ini file "
                             ,action=boolean, default=False)
    args_parser.add_argument("-w", "--write", dest="write", help="write to origin file",type=int, action=boolean,  default=0)
    args_parser.add_argument("-o", "--output", dest="output", help="chose other file to save output", default="")
    args_parser.add_argument("-sh", "--show", dest="show", help="show the txt",type=int, action=boolean, default=1)
    args_parser.add_argument("-regex_s", "--regex_search", dest="regex_search", help="regex for sellect key from txt", default="")

    #reg_replce = args_parser.add_subparsers("-regex_r", "--regex_replace", help="replace char in key to set in value",dest=regex_set_value, de#ult=None)
    args_parser .add_argument("-regex_r", "--regex_replce", dest="regex_set_value", help="regex for set value to key ini_file", default=None)




    return args_parser.parse_args()



def read_origin_file(args) -> str:
    # read to dict
    # if we need append will read with configparser to auto fill ini file
    case_sensitive = args.case_sensitive
    path_file = args.origin_file_path

    #print(re.findall(args.regex_search, open(path_file, "r").read()))
    txt = [word for word in open(path_file, "r").read().split()
               if word!="\n"]

    if not case_sensitive:
        txt=[word.lower() for word in txt]

    return txt


def update_dict(txt, args, config) -> None:
    #config.add_section('DEFAULT')a

    search_regex = args.regex_search
    set_value_regex = args.regex_set_value
    if search_regex == "": set_value_regex= None

    keys = config['DEFAULT'].keys()

    #print(txt)
    for word in txt:
        if word not in keys and re.search(search_regex, word):
          config['DEFAULT'][word] = re.sub(search_regex, set_value_regex, word)\
          if set_value_regex != None \
          else ""

    #print(list(config['DEFAULT'].keys()))

def write_to_ini_file(args, config) -> None:
    ini_file_path= args.ini_file_path

    if args.write:
        with open(args.ini_file_path, 'w') as f:
            config.write(f)

    if args.output:
       with open(args.output, 'w') as f:
            config.write(f)

    if args.show:
        print("\n".join([ f"{k} : {y}" for k,y in config['DEFAULT'].items()]))

if __name__ == "__main__":
    args =get_args()

    config = configparser.ConfigParser()

    if args.case_sensitive:
        config.optionxform=str

    if args.load_ini_file:
        config.read(args.ini_file_path)



    txt = read_origin_file(args)

    update_dict(txt, args, config)

    write_to_ini_file(args, config)

    #print(txt, args)
