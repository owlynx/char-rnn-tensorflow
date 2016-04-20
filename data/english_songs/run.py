from tempfile import mkstemp
from shutil import move
from os import remove, close
import argparse
from subprocess import call

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filePath', type=str, default='test.txt',
                    help='file containing lyrics')
parser.add_argument('-r', '--remove', type=str, default='-----',
                    help='remove unwanted patterns')
parser.add_argument('-p', '--place', type=str,
                    help='place new pattern')
parser.add_argument('-a', '--artist', type=str,
                    help='artist name')
parser.add_argument('-t', '--title', type=str,
                    help='title name')
parser.add_argument('-o', '--output', type=str, default='input.txt',
                    help='output file')
args = parser.parse_args()

def delete(file_path, pattern):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if pattern not in line:
                    new_file.write(line)
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

# call("../../../songtext/songtext -a" + args.artist + "-t" + args.title + "> temp.txt", shell=True)
delete("temp.txt", "-----")       ## Remove the line with -------
delete("temp.txt", ":")  ## Remove the line with :
delete("temp.txt", "Your query did not match any tracks.")
delete("temp.txt", "track(s) matched your search query.")
call("cat temp.txt >> " + args.output, shell=True)	## Write to final 'input.txt'
call("cp " + args.output + " ../../../songtext/", shell=True)	## Backup

#replace(args.filePath, args.remove, args.place)
