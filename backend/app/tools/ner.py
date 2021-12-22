def get_ner(sents, myltp):
    # myltp = ltp.LTP()
    if isinstance(sents, str):
        sents = [sents]
    seg, hidden = myltp.seg(sents)
    ner = myltp.ner(hidden)
    res_list = []
    for tokens, es in zip(seg, ner):
        for e in es:
            res_list.append((e[0], " ".join(tokens[e[1]: e[2] + 1])))
    res_list = list(set(res_list))
    return res_list