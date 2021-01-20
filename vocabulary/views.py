from django.template import Context, Template
import os
import re
import mimetypes
from . import levels

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def vocabulary(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['subtitle']
        proficiency = int(request.POST['proficiency'])
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        f = fs.open(uploaded_file.name)
        srt_read = f.read().decode('utf-8')
        final_list = srt_to_list(srt_read, proficiency)
        return render(request, 'vocabulary/raw.html', {'final_list': final_list})
    return render(request, 'vocabulary/vocabulary.html', {'title': 'Vocabulary'})


def srt_to_list(srt_read, proficiency):
    words = set(re.findall(r"[a-zA-Z\-'/]+", srt_read))
    words = [word.lower() for word in words]
    apos = re.compile(r"[a-zA-Z]+\'+?")


    ignore_list = []

    if proficiency == 1:
        for item in levels._1:
            ignore_list.append(item.strip().lower())

    elif proficiency == 2:
        for item in levels._2:
            ignore_list.append(item.strip().lower())
    
    elif proficiency == 3:
        for item in levels._3:
            ignore_list.append(item.strip().lower())

    elif proficiency == 4:
        for item in levels._4:
            ignore_list.append(item.strip().lower())
    
    elif proficiency == 5:
        for item in levels._5:
            ignore_list.append(item.strip().lower())
    
    elif proficiency == 6:
        for item in levels._6:
            ignore_list.append(item.strip().lower())

    elif proficiency == 7:
        for item in levels._7:
            ignore_list.append(item.strip().lower())

    elif proficiency == 8:
        for item in levels._8:
            ignore_list.append(item.strip().lower())

    elif proficiency == 9:
        for item in levels._9:
            ignore_list.append(item.strip().lower())
    
    elif proficiency == 10:
        for item in levels._10:
            ignore_list.append(item.strip().lower())
    
    elif proficiency == 11:
        for item in levels._11:
            ignore_list.append(item.strip().lower())


    pre_final = []

    for word in words:
        if word in ignore_list:
            pass
        else:
            if apos.match(word):
                span = apos.match(word).span()
                root = word[span[0]:span[1] - 1].lower()
                if root in ignore_list:
                    pass
                else:
                    pre_final.append(root)
            else:
                pre_final.append(word.lower())


    final = set(pre_final)
    final = sorted(list(final))

    return final
