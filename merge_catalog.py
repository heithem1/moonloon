from pathlib import Path
import argparse,json
p=argparse.ArgumentParser();p.add_argument('catalog');p.add_argument('--entry',default=str(Path(__file__).with_name('catalog.entry.json')));p.add_argument('--output',required=True);a=p.parse_args();c=json.loads(Path(a.catalog).read_text(encoding='utf-8-sig'));e=json.loads(Path(a.entry).read_text(encoding='utf-8-sig'))
if not isinstance(c.get('apps'),list):raise SystemExit('Catalogue invalide : apps doit être une liste.')
if any(x.get('id')==e['id'] and x.get('package_name')!=e['package_name'] for x in c['apps']):raise SystemExit('Identifiant déjà utilisé par une autre application.')
apps=[];done=False
for x in c['apps']:
 if x.get('id')==e['id'] or x.get('package_name')==e['package_name']:
  if not done:apps.append(e);done=True
 else:apps.append(x)
if not done:apps.append(e)
c['apps']=apps;revision=str(c.get('revision','moonloon'))
if 'Dashboard 2.3.1' not in revision:c['revision']=revision+' · Dashboard 2.3.1 · icône'
Path(a.output).write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
