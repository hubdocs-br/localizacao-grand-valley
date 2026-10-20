import re, base64, io, os
from PIL import Image
src = open('mapa_grand_valley_cores.html', encoding='utf-8').read()
out_dir = 'mapa_sun_place_leve'; img_dir = os.path.join(out_dir, 'img'); os.makedirs(img_dir, exist_ok=True)
pat = re.compile(r'(\b\w+)(\s*=\s*)"data:image/(\w+);base64,([A-Za-z0-9+/=]+)"')
count = 0
def repl(m):
    global count
    var, eq, fmt, b64 = m.group(1), m.group(2), m.group(3), m.group(4)
    raw = base64.b64decode(b64)
    if fmt == 'webp':
        open(os.path.join(img_dir, var + '.webp'),'wb').write(raw); count += 1
        return var + eq + '"img/' + var + '.webp"'
    im = Image.open(io.BytesIO(raw)).convert('RGB')
    im.save(os.path.join(img_dir, var + '.jpg'), 'JPEG', quality=82, optimize=True)
    th = im.copy(); th.thumbnail((150,150)); th.save(os.path.join(img_dir, var + '_thumb.jpg'), 'JPEG', quality=72, optimize=True)
    count += 1
    return var + eq + '"img/' + var + '.jpg"'
new = pat.sub(repl, src)
open(os.path.join(out_dir,'index.html'),'w',encoding='utf-8').write(new)
print('externalizadas:', count, 'sobrou', new.count('data:image'))
