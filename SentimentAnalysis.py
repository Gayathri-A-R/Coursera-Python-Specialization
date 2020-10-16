punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation (string):
    for i in string:
        for k in punctuation_chars:
            if i==k:
                string = string.replace(i,"") 
    return string
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_pos(sent):
    count = 0
    sentstripedlist = sent.split(" ")
    for i in sentstripedlist:
        word = strip_punctuation(i);
        wordlower = word.lower()
        for k in positive_words:
            if wordlower == k:
                count+=1
    return count

            
def get_neg(sent):
    count = 0
    sentstripedlist = sent.split(" ")
    for i in sentstripedlist:
        word = strip_punctuation(i);
        wordlower = word.lower()
        for k in negative_words:
            if wordlower == k:
                count+=1
    return count

fd = open('resulting_data.csv','w')
fd.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n') 

with open('project_twitter_data.csv') as data:
    content = data.readlines()[1:]
    for line in content:
        datalist = line.split(',')
        tweet = datalist[0]
        retweet = datalist[1]
        replay = datalist[2].split('\n')[0]
        pos = get_pos(tweet)
        neg = get_neg(tweet)
        net = pos - neg
        result = '{},{},{},{},{}\n'.format(retweet,replay,pos,neg,net)
        fd.write(result)
        
fd.close()