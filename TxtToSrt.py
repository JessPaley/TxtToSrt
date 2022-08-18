# Uses the contents of a text file to generate an srt file
# Input: text file, subtitle start time (hh:mm:ss,000), subtitle end time
# (hh:mm:ss,000)
def txttosrt(file, start_time, end_time):
    txt = open(file)
    text = txt.read()
    words = text.split()
    srt = open(file[:len(file) - 4] + ".srt", "w")
    lines = []
    current = ''
    charcount = 0
    for w in words:
        if charcount == 0:
            current += w
            charcount += len(w)
        elif charcount < 32:
            if charcount + len(w) + 1 < 32:
                current += (' ' + w)
                charcount += len(w) + 1
            else:
                lines.append(current)
                current = w
                charcount = len(w)
        else:
            lines.append(current)
            current = ''
            charcount = 0
            print('Line {} exceeds 32 characters'.format(len(lines)))
    timediff = 0
    if len(words) != 0:
        timediff = (end_time - start_time) / len(lines)  # formatting hh:mm:ss,000
        # round at last step
        # convert time?
    start = start_time
    end = start_time + timediff
    count = 1
    for l in lines:
        srt.write("{}\n{} --> {}\n{}\n\n".format(
            count, start, end, l))
        count += 1
        start = end
        end += timediff
    txt.close()
    srt.close()
