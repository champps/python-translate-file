usage: translate.py [-h] [-c] [-n | --new | --no-new] [-fl FROM_LINE] [-tl TO_LINE] [-sh | --show | --no-show]
                    [-w | --write | --no-write] [-o OUTPUT]
                    origin_file_path ini_file_path

positional arguments:
  origin_file_path      this origen file path
  ini_file_path         this ini file path

options:
  -h, --help            show this help message and exit
  -c                    case sensitive (default: False)
  -fl FROM_LINE, --from_line FROM_LINE
                        from line int start 1
  -tl TO_LINE, --to_line TO_LINE
                        to line int start with 1
  -sh, --show, --no-show
                        show the txt (default: 1)
  -w, --write, --no-write
                        write to origin file (default: 0)
  -o OUTPUT, --output OUTPUT
                        chose outher file to save output


--------------
usage: fill_ini_file.py [-h] [-c] [-l | --load_ini_file | --no-load_ini_file]
                        [-w | --write | --no-write] [-o OUTPUT]
                        [-sh | --show | --no-show]
                        origin_file_path ini_file_path

positional arguments:
  origin_file_path      this origen file path
  ini_file_path         this ini file path

options:
  -h, --help            show this help message and exit
  -c                    case sensitive (default: False)
  -l, --load_ini_file, --no-load_ini_file
                        load ini file (default: True)
  -w, --write, --no-write
                        write to origin file (default: 0)
  -o OUTPUT, --output OUTPUT
                        chose other file to save output
  -sh, --show, --no-show
                        show the txt (default: 1)
 ---------------
 
 examples :
 
 python ../fill_ini_file.py file_one.txt file_one.ini 
 that will print result on terminal with no.of lines
 
 add -w for writer to origen file 
 or add -o path/of/file to save it in other file
 
 if you have old file you wont load it use -l

-c for case sensitive
 
 then 
 
 python ../translate.py file_one.txt file_one.ini -fl 3 -o new.txt
this will save changes to new.txt file 
use ini file to cange word in txt file from line 3 to end file

 all examples in example file (not alot :) 
  
 you can use this for encrype words  

---—

todo :
- [ ] split symbols with attached spaces
- [ ] add reverse method in translate file
- [ ] make code more readable
- [ ] use object to easy maintenance and development
- [ ] add part of string (more than one word without space)
- [ ] add packup option