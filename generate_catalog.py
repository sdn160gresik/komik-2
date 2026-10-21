#!/usr/bin/env python3
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
OUT=ROOT/"komik.json"
SKIP={".git",".github","assets","node_modules",".venv","__pycache__"}
EXT={".jpg",".jpeg",".png",".webp",".gif"}
COVERS={"cover.jpg","cover.jpeg","cover.png","cover.webp","sampul.jpg","sampul.png","thumbnail.jpg","thumbnail.png"}
LABELS={"mtk":"Matematika","matematika":"Matematika","bhsi":"Bahasa Indonesia","bahasa":"Bahasa Indonesia","bahasa-indonesia":"Bahasa Indonesia","ipas":"IPAS","pkn":"Pendidikan Pancasila","ppkn":"Pendidikan Pancasila","soal-cerita":"Soal Cerita","seni":"Seni Rupa"}
def pretty(s):
 s=re.sub(r"[?_]+"," ",str(s or "")).replace("-"," ")
 return re.sub(r"\s+"," ",s).strip().title()
def nk(p): return [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)",p.name)]
def rel(p): return p.relative_to(ROOT).as_posix()
def metadata(folder):
 for n in ("info.json","metadata.json"):
  f=folder/n
  if f.is_file():
   try:
    v=json.loads(f.read_text(encoding="utf-8"))
    if isinstance(v,dict): return v
   except Exception as e: print("WARNING",f,e)
 return {}
def build():
 items=[]
 for folder in sorted(ROOT.rglob("*")):
  if not folder.is_dir() or any(x in SKIP for x in folder.relative_to(ROOT).parts): continue
  parts=folder.relative_to(ROOT).parts
  if len(parts)<2: continue
  imgs=sorted([p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in EXT],key=nk)
  if not imgs: continue
  m=metadata(folder); key=parts[0].lower()
  subject=m.get("mataPelajaran") or m.get("mata_pelajaran") or m.get("mapel") or LABELS.get(key,pretty(parts[0]))
  title=m.get("judul") or m.get("title") or m.get("nama") or pretty(folder.name)
  cov=m.get("thumbnail") or m.get("cover") or m.get("sampul")
  if cov: cover=cov if str(cov).startswith(("http://","https://")) else rel(folder/str(cov))
  else: cover=rel(next((p for p in imgs if p.name.lower() in COVERS),imgs[0]))
  pages=[p for p in imgs if p.name.lower() not in COVERS]
  numbered=[p for p in pages if re.match(r"^halaman-\d+\.(jpg|jpeg|png|webp|gif)$",p.name,re.I)]
  if numbered: pages=numbered
  if not pages: pages=[imgs[0]]
  try: order=int(m.get("urutan",m.get("order",9999)))
  except (TypeError,ValueError): order=9999
  item={"id":rel(folder),"folder":rel(folder),"mapelKey":key,"mapel":subject,"judul":title,"nama":title,"subjudul":m.get("subjudul",m.get("subtitle","")),"deskripsi":m.get("deskripsi",m.get("description",f"Jelajahi cerita seru dalam {title}.")),"thumbnail":cover,"halaman":[rel(p) for p in sorted(pages,key=nk)],"jumlahHalaman":len(pages),"kelas":m.get("kelas",m.get("grade",[])),"urutan":order,"updatedAt":m.get("updatedAt","")}
  for k,v in m.items():
   if k not in item and k not in {"mataPelajaran","mata_pelajaran","title","nama","subtitle","description","cover","sampul","order","grade"}: item[k]=v
  items.append(item)
 items.sort(key=lambda x:(x["mapel"].casefold(),x["urutan"],x["judul"].casefold()))
 OUT.write_text(json.dumps({"generatedBy":"generate_catalog.py","total":len(items),"komik":items},ensure_ascii=False,indent=2),encoding="utf-8")
 print(f"Katalog baru: {len(items)} bab")
if __name__=="__main__": build()
