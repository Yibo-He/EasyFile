from docx.shared import Pt, RGBColor

from . import runtools
from .myfont import Font
from .myfont import RepStr
from docx.oxml.ns import qn


def get_typeface(run, paragraph, default):
    name = default.name
    if run.font.name is not None:
        name = run.font.name
    else:
        style = run.style
        while style is not None and style.font.name is None:
            style = style.base_style
        if style is not None:
            name = style.font.name
        elif paragraph.style.font.name != None:
            name = paragraph.style.font.name
        else:
            style = paragraph.style
            while style is not None and style.font.name is None:
                style = style.base_style
            if style is not None:
                name = style.font.name
    return name


def get_size(run, paragraph, default):
    size = default.size
    if run.font.size is not None:
        size = run.font.size.pt
    else:
        style = run.style
        while style is not None and style.font.size is None:
            style = style.base_style
        if style is not None:
            size = style.font.size
        elif paragraph.style.font.size is not None:
            size = paragraph.style.font.size
        else:
            style = paragraph.style
            while style is not None and style.font.size is None:
                style = style.base_style
            if style is not None:
                size = style.font.size
    return size


def get_rgbcolor(run, paragraph, default):
    color = default.color
    if run.font.color.type is not None:
        color = run.font.color.rgb
    else:
        style = run.style
        while style is not None and style.font.color.rgb is None:
            style = style.base_style
        if style is not None:
            color = style.font.color.rgb
        elif paragraph.style.font.color.rgb is not None:
            color = paragraph.style.font.color.rgb
        else:
            style = paragraph.style
            while style is not None and style.font.color.rgb is None:
                style = style.base_style
            if style is not None:
                color = style.font.color.rgb
    return color


def get_font(run, paragraph, default):
    name = get_typeface(run, paragraph, default)
    color = get_rgbcolor(run, paragraph, default)
    size = get_size(run, paragraph, default)
    return Font(color=color, name=name, size=size)


def check(old: RepStr, now: RepStr):
    ret = []
    ret.append(old.str == "" or old.str == now.str)
    ret.append(old.font.color == "" or old.font.color == now.font.color)
    ret.append(old.font.size == 0 or old.font.size == now.font.size)
    #   if(now.font.size==16.0):
    #       print(now.str)
    ret.append(old.font.name == "" or old.font.name == now.font.name)
    for x in ret:
        if x is False:
            return False
    #   print(now.font.name)
    return True

class KmpAlgorithm:
    nxt = []
    def __init__(self,str=""):
        lens = len(str)
        i=0
        j=0
        self.nxt.append(-1)
        while i < lens:
            while j!=-1 and str[i]!=str[j]:
                j=self.nxt[j]
            self.nxt.append(j)
            j += 1
            i += 1


def replace(document, default, old, new):
    for para in document.paragraphs:
        for run in para.runs:
            if (len(run.text) > 1):
                t = range(len(run.text))
                runtools.split_run_by(para, run, t)
    myruns = []
    for para in document.paragraphs:
        for run in para.runs:
            if len(run.text) < 1:
                continue
            nowfont = get_font(run, para, default)
            myruns.append([run, nowfont])
    if len(old.str) != 0:
        KmpAlgorithm(old.str)
        i = 0
        j = 0
        while i < len(myruns):
            if len(myruns[i][0].text) == 0:
                continue
            while j != -1 and check(RepStr(old.str[j], old.font.color, old.font.name, old.font.size), RepStr(myruns[i][0].text[0], myruns[i][1].color,myruns[i][1].name,myruns[i][1].size)) is False:
                j = KmpAlgorithm.nxt[j]
            i += 1
            j += 1
            if j != len(old.str):
                continue
            run = myruns[i - j][0]
            run.text = new.str
            if new.font.color:
                run.font.color.rgb = RGBColor.from_string(new.font.color)
            # print(new.font.name)
            if run.font.name:
                run.font.name = new.font.name
                run._element.rPr.rFonts.set(qn('w:eastAsia'),new.font.name)
            if new.font.size:
                run.font.size = Pt(new.font.size)
            for k in range(1, len(old.str)):
                myruns[i - k][0].text = ""
            j = KmpAlgorithm.nxt[j]
    else:
        for run in myruns:
            if check(RepStr(color=old.font.color, name=old.font.name, size=old.font.size),
                     RepStr(color=run[1].color, name=run[1].name,size=run[1].size)):
                run=run[0]
                if new.str:
                    run.text = new.str
                if new.font.color:
                    run.font.color.rgb = RGBColor.from_string(new.font.color)
                # print(new.font.name)
                if run.font.name:
                    run.font.name = new.font.name
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), new.font.name)
                if new.font.size:
                    run.font.size = Pt(new.font.size)
    return
  