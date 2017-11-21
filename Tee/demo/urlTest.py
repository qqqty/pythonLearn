
import re, urllib


url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"

search_num = re.compile("(\d*)$")
search_html = re.compile("\.html$")


for i in range(4):
    print "%i-%s : " % (i, nothing)

    con = urllib.urlopen("%s%s" % (url, nothing)).read()

    print con


    if search_html.findall(con):
        break

    match = search_num.findall(con)
    if match:
        nothing = match[0]
    else:
        nothing = str(int(nothing) / 2)




