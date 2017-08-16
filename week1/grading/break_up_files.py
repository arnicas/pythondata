# Use jupyter nbconvert --to python NB first,
# then run this on the py notebooks.

import os
import sys

pattern1 = "answer"
pattern2 = "moving on"


def process_file(name):
    flag = False
    problems = 1
    newfile = False

    filebasename = os.path.splitext(name)[0]
    #try:
    with open(name) as handle:
        for line in handle:
            if line[0] == '#' and pattern1 not in line and pattern2 not in line.lower():
                continue
            # start of the code pattern
            elif line[0] == '#' and pattern1 in line and pattern2 not in line.lower():
                flag = True
                print("match {}".format(problems))
                if newfile:
                    newfile.close()
                newfile = open(filebasename + "_Answer" + str(problems) + ".py", "w")
                problems += 1
            if line[0] != "#" and flag:
                #print(line.strip())
                newfile.write(line)
            if line[0] != "#" and flag and ("ls" in line or "mkdir" in line or "cd" in line):
                newfile.write("#" + line)
            # end of the code answer
            if line[0] == "#" and pattern1 not in line and pattern2 in line.lower():
                flag = False
    return problems
    #except:
    #    return None

def main():
    print(sys.argv[1:])
    print("Files {}".format(len(sys.argv[1:])))
    for sourcefile in sys.argv[1:]:
        if sourcefile != "break_up_files.py":
            print("Processed {} file.".format(process_file(sourcefile)))

if __name__ == '__main__':
    main()
