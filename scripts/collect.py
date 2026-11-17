import urllib.request,xml.etree.ElementTree as ET,json,datetime
from pathlib import Path
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
sources=[('Agência Brasil','https://agenciabrasil.ebc.com.br/rss/ultimasnoticias/feed.xml')]
out={'collectedAt':now,'sources':[],'items':[]}
for name,url in sources:
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'SegundoRadarWorkshop/0.1'}),timeout=25).read()
  root=ET.fromstring(raw); n=0
  for item in root.findall('.//item')[:25]:
   title=item.findtext('title','');link=item.findtext('link','')
   # Scope gate: only reviewed national coverage; new items await editorial triage.
   blocked=['facções','polícia','futebol','campeonato','homicídio','prisão']
   if any(w in title.lower() for w in blocked): continue
   related=[]
   for child in item:
    if child.tag.endswith('news_item'):
     entry={x.tag.split('}')[-1]:x.text for x in child}
     related.append(entry)
   out['items'].append({'title':title,'url':link,'publishedAt':item.findtext('pubDate',''),'source':name,'related':related,'status':'Publicado na fonte; apuração pendente'})
   n+=1
  out['sources'].append({'name':name,'url':url,'status':'ok','count':n})
 except Exception as e:out['sources'].append({'name':name,'url':url,'status':'error','error':str(e)})
Path('dist/radar-data.json').write_text(json.dumps(out,ensure_ascii=False))
print(json.dumps({'collectedAt':now,'sources':out['sources'],'count':len(out['items'])},ensure_ascii=False))
