# LaTeX Templates
template_global='''\\documentclass[a4paper]{{article}}
\\usepackage[nome={},razza={},professione={},authentic={}]{{girsa}}

\\begin{{document}}

\\fontsize{{5pt}}{{7pt}}\\selectfont

\\begin{{multicols}}{{3}}

{}

\\end{{multicols}}

\\begin{{multicols}}{{2}}

{}

\\end{{multicols}}

{}
\\newpage
\\pagestyle{{fancy}}
{}

\\end{{document}}
'''


template_scheda='''
\\begin{{cbox}}[tabularx={{lX}},title=Scheda del Personaggio]
Nome    & {}\\\\
Razza   & {}\\\\
Peso    & {} kg\\\\
Altezza & {} m\\\\
Capelli & {}\\\\
Occhi   & {}\\\\
Temperamento & {}\\\\
Odio         & {}\\\\
Speciale     & {}\\\\
Professione  & {}\\\\
Punti Esperienza     & {}\\\\
Livello      & {}\\\\
Regno        & {}\\\\
Punti Magia  & {}\\\\
\\end{{cbox}}\n
'''

template_caratteristiche='''\\begin{{cbox}}[tabularx={{lYYYYY}},title=Caratteristiche]
\\headcolor Caratteristica & \\headcolor Abbr & \\headcolor Punteggio &\\headcolor Norm. &\\headcolor Razza &\\headcolor Totale \\\\
{}
\\end{{cbox}}\n
'''

template_caratteristica='{}\t& {} & {}  & {}  &  {}  & {} \\\\'

template_abilita='''\\begin{{abilbox}}{{{}}}{{{}}}
\\abilhead
{}
\\end{{abilbox}}\n
'''

template_abil='{}  & \\score{{{}}}{{{}}}\\emptyspace{{{}}} &{}&{} \hfill {} &{} &{} &{} &{}   &{} \\hfill {}\\\\'

template_lingue='''\\begin{{cbox}}[tabularx={{Xc}},title=Lingue]
\\headcolor Lingue \\hfill {{ \\fbox{}}} & \\headcolor Grado \\\\
{}
\\end{{cbox}}'''

template_lingua='{} {} & {} \\\\'


template_armature='''
\\begin{{cbox}}[tabularx={{XX}},title=Equipaggiamento: Armatura]
Armatura  & {} \\\\
Scudo     & {} \\\\
Elmo      & {} \\\\
Bracciali & {} \\\\
Schinieri & {} \\\\
\\end{{cbox}}
'''

armature = {
'Armatura' : '\\blankline{5}',
'Scudo' : '\\blankline{5}',
'Elmo' : '\\blankline{5}',
'Bracciali' : '\\blankline{5}',
'Schinieri' : '\\blankline{5}',
}


template_armi='''
\\begin{{cbox}}[tabularx={{X||cXX||cccc}},title=Equipaggiamento: Armi]
\\headcolor Arma          & \\headcolor Mal. &\\headcolor Crit &\\headcolor Abil & \\headcolor Ogg &\\headcolor P/M &\\headcolor NA/C &\\headcolor Ric \\\\
{}
\\end{{cbox}}
'''

template_arma='{}\t & {} & {} & {} & {} & {} & {} & {} \\\\'


template_magic='''
\\begin{{cbox}}[tabularx={{p{{0.2\\textwidth}}||cp{{0.075\\textwidth}}c||X}},title=Equipaggiamento: Oggetti Magici]
\\headcolor Oggetto       & \\headcolor Bonus & \\headcolor Usi/Giorno & \\headcolor Cariche & \\headcolor Descrizione \\\\
{}
\\end{{cbox}}
'''

template_magic_item='{} & {} & {} & {} & {}\\\\'

template_equip='''
\\begin{{cbox}}[tabularx={{p{{0.2\\textwidth}}||p{{0.075\\textwidth}}c||X}},title=Equipaggiamento: Oggetti Normali]
\\headcolor Oggetto       & \\headcolor Bonus &\\headcolor Quantit\\`a &\\headcolor  Descrizione \\\\
{}
\\end{{cbox}}
'''

template_monete='''
\\begin{{cbox}}[tabularx={{p{{0.15\\textwidth}}||p{{0.1\\textwidth}}c||X}},title=Equipaggiamento: Monete{{,}} Gemme e Gioielli]
\\headcolor Oggetto       & \\headcolor Valore unit. &\\headcolor Quantit\\`a &\\headcolor  Descrizione \\\\
{}
\\end{{cbox}}
'''


template_equip_obj='{}\t & {} & {}  & {}\\\\'

template_liste='''
\\begin{{cbox}}[tabularx={{Xc}},title=Liste di Incantesimi]
\\headcolor Liste \\hfill {{ \\fbox{{{}}} }} &\\headcolor [Prob] \\\\
{}
\\end{{cbox}}
'''

template_lista='{} {} & {} \\\\'
template_lista_blank='{} \\blankline{{5}} & \\blankline{{5}} \\\\'

template_incantesimi='''
\\begin{{cbox}}[tabularx={{lrlrrX}},title=Liste di Incantesimi]
\\headcolor Lista & \\headcolor Liv. & \\headcolor Incantesimo &\\headcolor R &\\headcolor D &\\headcolor Descrizione \\\\
{}
\\end{{cbox}}
'''

template_incantesimo='{} & {} & {} & {} & {} & {} \\\\'

