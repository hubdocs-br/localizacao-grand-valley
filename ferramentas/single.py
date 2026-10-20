import re,base64,io,sys
from PIL import Image
s=open('/home/claude/mapa_grand_valley_cores.html',encoding='utf-8').read()
m=[m for m in re.finditer(r'<script>(.*?)</script>',s,re.S)][-1]; js=m.group(1)
pat=re.compile(r'"data:image/(\w+);base64,([A-Za-z0-9+/=]+)"'); lines=[];names=[]
def repl(mm):
    k='IMGD%02d'%len(names)
    if mm.group(1)=='webp':
        names.append(k); lines.append('var %s="data:image/webp;base64,%s";'%(k,mm.group(2))); return k
    im=Image.open(io.BytesIO(base64.b64decode(mm.group(2)))).convert('RGB'); b=io.BytesIO(); im.save(b,'JPEG',quality=82,optimize=True)
    names.append(k); lines.append('var %s="data:image/jpeg;base64,%s";'%(k,base64.b64encode(b.getvalue()).decode())); return k
js2=pat.sub(repl,js); assert 'data:image' not in js2
open('/tmp/claude-0/single.js','w',encoding='utf-8').write(js2)
open(sys.argv[1]+'/imgs.js','w').write('\n'.join(lines)); open(sys.argv[1]+'/names.txt','w').write(','.join(names))
open(sys.argv[1]+'/shell.html','w',encoding='utf-8').write(s[:m.start()]+'<script>@@IMGS@@</script>\n<script>@@MAIN@@'+s[m.end(1):])
print(len(names),'imgs')
