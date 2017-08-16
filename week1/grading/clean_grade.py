
import os
import sys


def process_file(name):
    flag = False
    newfile = False


    filebasename = os.path.splitext(name)[0]
    newfile = open(filebasename + "_clean.py", "w")
    #try:
    with open(name) as handle:
        for line in handle:
            if line[0:2] == "ls":
                newfile.write("#" + line)
            elif line[0:2] == "cd":
                newfile.write("#" + line)
            elif line[0] == "!":
                newfile.write("#" + line)
            elif line[0:14] == "get_ipython()":
                newfile.write("#" + line)
            else:
                newfile.write(line)
        gradingstrings = (
            "print('Grading')\n"
            "print(get_lowest(mydata, 1))\n"
            "print(get_difference(mydata[1]))\n"
            "print(get_lowest_with_date(mydata, 3))\n"
            "print(list(volumedict.items())[0])\n"
            )
        newfile.write(gradingstrings)
    newfile.close()
    return filebasename


def main():
    print(sys.argv[1:])
    print("Files {}".format(len(sys.argv[1:])))
    for sourcefile in sys.argv[1:]:
        if sourcefile != "clean_files.py":
            print("Processed {} file.".format(process_file(sourcefile)))

if __name__ == '__main__':
    main()