def read_file_by_lines(file):
    return open("test", "r").read().split("\n")

def get_comments_index(f):
    comment_index = []
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] != "#" and f[i][j] != "	":
                break
            if f[i][j] == "#":
                comment_index.append(i)
                break
    return comment_index

def remove_comments(f, comments_index):
    comments_index.reverse()
    for i in comments_index:
        f.pop(i)
    return

def print_text(text):
    for i in text:
        print(i)

def run():
    f = read_file_by_lines("test")
    comments_index = get_comments_index(f)
    remove_comments(f, comments_index)
    print_text(f)

run()