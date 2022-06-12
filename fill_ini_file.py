import configparser, argparse

def get_args() -> argparse.ArgumentParser:
    #python translate.py originfile inifile.ini [[-fl] fromline] [[-tl] toline] [-i]
    args_parser = argparse.ArgumentParser()

    args_parser.add_argument("origin_file_path", help="this origen file path")
    args_parser.add_argument("ini_file_path", help="this ini file path")
    args_parser.add_argument('-c',dest="case_sensitive" ,help="case sensitive",
                             action=argparse.BooleanOptionalAction, default=False)
    args_parser.add_argument('-l',"--load_ini_file",dest="load_ini_file" ,help="load ini file "
                             ,action=argparse.BooleanOptionalAction, default=True)

    return args_parser.parse_args()



def read_origin_file(case_sensitive, path_file) -> str:
    # read to dict
    # if we need append will read with configparser to auto fill ini file
    txt = [word for word in open(path_file, "r").read().split()
               if word!="\n"]

    if not case_sensitive:
        txt=[word.lower() for word in txt]

    return txt


def update_dict(txt,ini_file_path, config) -> None:
    #config.add_section('DEFAULT')
    keys = config['DEFAULT'].keys()

    for word in txt:
        if word not in keys:
          config['DEFAULT'][word] = ""

    #print(list(config['DEFAULT'].keys()))

def write_to_ini_file(ini_file_path, config) -> None:

    with open(ini_file_path, 'w') as f:
        config.write(f)


if __name__ == "__main__":
    args =get_args()

    config = configparser.ConfigParser()

    if not args.load_ini_file:
        config.read(args.ini_file_path)

    if args.case_sensitive:
        config.optionxform=str


    txt = read_origin_file(args.case_sensitive, args.origin_file_path)

    update_dict(txt, args.ini_file_path, config)

    write_to_ini_file(args.ini_file_path, config)

    #print(txt, args)
