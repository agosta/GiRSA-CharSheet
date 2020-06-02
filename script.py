#!/usr/bin/python3
# -*- coding: utf-8 -*-

__doc__ = '''Converts a GiRSA ODS character sheet to a formatted file via XeLaTeX.

TODO: detach Adolescenza from starting bonuses (e.g., languages known by default
from those learnt before level 1)

TODO: enable direct reading from Google Drive via gread2 and Google API

TODO: enable ouput to Salvatore's server to feed dice roller

TODO: general refactoring for increased readability and more flexible management
of bonuses (reduce reliance on Google Sheet formulae and do more checks in the 
script).

TODO: extend to support dual classed characters (major extension, needs redesign
of the Google Sheet as well!)

TODO: add details of new weapons, spell lists, and languages, as well as all 
major races and classes
'''

# Import Data from ODS file
import pyexcel as p
from sys import argv

infname=argv[-1] if len(argv)>1 else 'GiRSA-CharSheet.ods'
data=p.get_book(file_name=infname)

chars=data['Caratteristiche']
abils=data['Abilità']
equip=data['Equipaggiamento']
tarmi=data['Armi']
try : incan=data['Incantesimi']
except KeyError : incan=False

# LaTeX Templates
template_global='''\\documentclass[a4paper]{{article}}
\\usepackage[nome={},razza={},professione={}]{{girsa}}

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


# Extract character info
info=[]
stats=[]
for r in chars.rows():
	if r[0]=='Info' : 
		info.append(r[2:16])
	if r[0]=='Stat' : 
		stats.append(r[1:7])

info=dict(zip(*info))
scheda=template_scheda.format(
	info['Nome'],info['Razza'],info['Peso'], info['Altezza'],
	info['Capelli'],info['Occhi'],info['Temperamento'],info['Odio'],
	info['Speciale'],info['Classe'],info['XP'],info['Livello'],
	info['Regno'],info['Punti Magia']
)

caratteristiche=template_caratteristiche.format('\n'.join([ template_caratteristica.format(*s) for s in stats ]))

# Manage all Abilities and Bonuses
cat_abil = [ 'Movimento e Manovra', 'Abilità con le armi', 'Abilità generiche', 
		'Abilità di Sotterfugio', 'Abilità magiche', 'Abilità varie', 
		'Bonus e Tiri Resistenza', 'Abilità secondarie' ]

def to_int(x):
	try : return int(x)
	except Exception : return 0

BO={}
abilita=''
for ab in cat_abil :
	out=[]
	for r in abils.rows():
		if r[0]==ab :
			if ab=='Abilità con le armi' : BO[r[1]]=r[30]
			if ab=='Abilità secondarie' and r[25]==-25 : continue
			try : x=int(r[24])
			except ValueError : x=20
			try : x-=int(r[23])
			except ValueError : x=0
			if r[0]==r[1] : out.append(r[3] if r[3]!='' else -1)
			else : 
				out.append(r[1:2]+[to_int(r[23])]+[x,2]+r[25:34])
	abilita+=template_abilita.format(ab,out[0],'\n'.join([ template_abil.format(*x) for x in out[1:]]))

# Manage Languages
out=[]
n=1
for r in abils.rows():
	if r[0]=='Lingue' :
		if r[0]==r[1] : out.append(to_int(r[3]))
		else : 
			out.append([n,r[1],r[23]])
			n+=1
lingue=template_lingue.format(out[0],'\n'.join([ template_lingua.format(*x) for x in out[1:] if to_int(x[2])!=0]))

# Manage Spell Lists
def get_last(r):
	r.reverse()
	for x in r : 
		if x != '' : return x
	return ''

out=[]
n=1
for r in abils.rows():
	if r[0]=='Liste' :
		if r[0]==r[1] : out.append(to_int(r[4]))
		else : 
			if get_last(r[2:23]) in [ '', 0 ] : continue
			out.append([n,r[1],get_last(r[2:23])])
			n+=1
liste=template_liste.format(out[0], 
	'\n'.join([ template_lista.format(*x) for x in out[1:]]+
		  [template_lista_blank.format(x) for x in range(n,16)])
)


# Equipment
out=[ r[2:6]+r[7:8] for r in equip.rows() if r[1]=='Magico' ]
magici=template_magic.format('\n'.join([ template_magic_item.format(*x) for x in out]))

out=[ r[2:4]+r[6:8] for r in equip.rows() if r[1]=='Normale' and r[0]!='Valori' ]
oggetti=template_equip.format('\n'.join([ template_equip_obj.format(*x) for x in out]))

out=[ r[2:4]+r[6:8] for r in equip.rows() if r[1]=='Normale' and r[0]=='Valori' ]
monete=template_monete.format('\n'.join([ template_equip_obj.format(*x) for x in out]))


arms=['Armatura','Scudo','Elmo','Bracciali','Schinieri']
out={ r[0] : str(r[7]) for r in equip.rows() if r[0] in arms and r[8]=='Y' }
for a in out : 
	armature[a]=out[a]
armatura=template_armature.format(*[ armature[a] for a in arms ])

def add_BO(BO,cases):
	return [ to_int(x)+to_int(BO) for x in cases ]

armi={ r[2] : r[4] for r in equip.rows() if r[0] =='Arma' }
out =[ t[:4]+[armi[t[0]]]+add_BO(BO[t[3]],t[4:7]) for t in tarmi if t[0] in armi.keys() ]
armi=template_armi.format('\n'.join([template_arma.format(*x) for x in out]))

if incan :
	incantesimi = [i for i in incan.rows() ][1:]
	incantesimi=template_incantesimi.format('\n'.join([template_incantesimo.format(*x) for x in incantesimi ]))
else : incantesimi=''

# Write out the LaTeX file
res=template_global.format(
	info['Nome'],info['Razza'], info['Classe'],
	scheda+lingue+armatura+liste,
	caratteristiche+armi,
	abilita,
	magici+oggetti+monete+incantesimi
)
fname='-'.join(info['Nome'].split())+'.tex'
with open(fname, 'w') as fout :
	fout.write(res)

# Call XeLaTeX
import subprocess
x=subprocess.call(['xelatex', fname])
if x : print('Error compiling LaTeX file {}: {}'.format(fname,x))

