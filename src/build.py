import base64,pathlib,shutil
here=pathlib.Path(__file__).parent
root=here.parent
src=(here/'nimodo-map.src.html').read_text(encoding='utf-8')
b64=base64.b64encode((here/'mexico_bunny_3d.glb').read_bytes()).decode()
page=src.replace('__BUNNY_GLB__',b64)
# 아티팩트용: 머리 없이 (게시할 때 자동으로 감쌈)
(root/'nimodo-map.html').write_text(page,encoding='utf-8')
# GitHub Pages용: 문서 머리를 직접 붙임
head=('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
      '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
      '<meta name="description" content="마냐나 × 뚜벅냥이 — 멕시코시티 공항 시설 찾기와 길고양이 수집 앱 프로토타입">\n</head>\n<body>\n')
dep=root/'deploy'
dep.mkdir(exist_ok=True)
(dep/'index.html').write_text(head+page+'\n</body>\n</html>\n',encoding='utf-8')
(dep/'src').mkdir(exist_ok=True)
for f in ['nimodo-map.src.html','build.py','mexico_bunny_3d.glb']:
    shutil.copy(here/f,dep/'src'/f)
print('built',len(page))
