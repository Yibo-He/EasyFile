from .process import process
from .ner import get_ner
def formatter(document, requirements, myltp=None):
    # print("OK")

    # transform the requirements
    print("requirements: ", requirements)
    if len(requirements) == 1 and requirements[0]['src_str'] == '<ENT>':
        print("In the processing of entites.")
        sents = []
        for para in document.paragraphs:
            for run in para.runs:
                if (len(run.text) > 1):
                    sents.append(run.text)
        ents = get_ner(sents, myltp)
        print("entities: ", ents)
        # all_ents = [i[1] for i in ents]
        reqs = []
        for ent_t in ents:
            ent = ent_t[1] # only use the name
            tmp = requirements[0].copy()
            tmp['src_str'] = ent
            if requirements[0]['dst_str'] == '<ENT>':
                tmp['dst_str'] = ent
            reqs.append(tmp)
        requirements = reqs
        print("transformed requirements: ", requirements)


    for requirement in requirements:
        document=process(document,requirement)
    return document
