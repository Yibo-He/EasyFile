from .process import process
from .process import process_ent
from .ner import get_ner
import os

def formatter(document, requirements, myltp=None,cwd = os.getcwd()):
    # print("OK")
    os.chdir(cwd)
    # transform the requirements
    print("requirements: ", requirements)
    if len(requirements) == 1 and requirements[0]['src_str'] == '<ENT>':
        print("In the processing of entites.")
        sents = ""
        for para in document.paragraphs:
            for run in para.runs:
                if len(run.text) > 0:
                    sents+=run.text
        try:
            ents = get_ner(sents, myltp)
        except Exception as e:
            print(e)
            ents=[]
        print("entities: ", ents)
        # all_ents = [i[1] for i in ents]
        # reqs = []
        # for ent_t in ents:
        #     ent = ent_t[1] # only use the name
        #     tmp = requirements[0].copy()
        #     tmp['src_str'] = ent
        #     if requirements[0]['dst_str'] == '<ENT>':
        #         tmp['dst_str'] = ent
        #     reqs.append(tmp)
        req = requirements[0].copy()
        req['src_str'] = [ent[1] for ent in ents]
        req['dst_str'] = [ent[1] for ent in ents]
        print("transformed requirements: ", req)
        document = process_ent(document,req)

    for requirement in requirements:
        document=process(document,requirement)
    document.save("res.docx")
