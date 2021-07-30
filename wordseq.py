import sys

FINALW = ""
def change_alphabet(initial_word, successors=[]):
        for index in range(0, len(initial_word)):
            for i in range(ord("a"), ord("z")):
                new_str = (initial_word[0:index] + chr(i) + initial_word[index + 1: len(initial_word)]).lower()

                if new_str != initial_word.lower():
                    with open(sys.argv[1]) as f:
                        if "\n"+new_str+"\n" in f.read().lower():
                            if new_str == FINALW:
                                return successors
                            successors.append(new_str)
        return successors

def rotate_alphabets(initial_word, successors=[], len_rotated=0):
    if len_rotated == len(initial_word)-1:
        return successors;
    rotated_word = (initial_word[1:] + initial_word[0]).lower()
    with open(sys.argv[1]) as f:
        if "\n"+rotated_word+"\n" in f.read().lower():
            if rotated_word == FINALW:
                return successors
            successors.append(rotated_word)
    return rotate_alphabets(rotated_word, successors,len_rotated+1)

def successors(initial_word):
    successors = []
    successors.extend(rotate_alphabets(initial_word, successors))
    successors.extend(change_alphabet(initial_word, successors))
    return successors

def make_path(initial_word, current, parents):
    path = [current]
    while current != initial_word:
        current = parents[current]
        path.append(current)
    return path

def bfs(initial_word, final_word, parents, queue):
    current = queue[0];
    print(current)
    if final_word == current:
        return make_path(initial_word, current, parents)
    for s in successors(current):
        if s not in parents:
            queue.append(s)
            parents[s] = current
            if s == final_word:
                return make_path(initial_word, s, parents)
    queue = queue[1:]
    return bfs(initial_word, final_word, parents, queue)


def find_word_path(initial_word, final_word):
    FINALW = final_word.lower()
    queue =[initial_word.lower()];
    parents = {}
    parents[initial_word.lower()] = None
    return bfs(initial_word.lower(),final_word.lower(), parents, queue)


def check_in_file():
    with open('Words.txt') as f:
        if 'chip\n' in f.read().lower():
            print("true")

def main():
    # check_in_file()
    # print( change_alphabet("CHIP"))
    # print(rotate_alphabets("CHIP"))
    # print(SUCCESSORS)
    if(len(sys.argv) == 4):
        print(find_word_path(sys.argv[2], sys.argv[3]))



    # file_name = "Words.txt"
    # initial_word= "CHIP"
    # final_word = "STOP"
    #
    # find_word_path(initial_word,final_word)

main()