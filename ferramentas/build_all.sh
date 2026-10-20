set -e
S=/tmp/claude-0/-home-claude/d0de281f-dff3-56fe-a314-cd79ef836235/scratchpad
cd /home/claude; rm -rf mapa_sun_place_leve
python3 externalize.py
python3 - <<'PY'
import re
s=open('mapa_sun_place_leve/index.html',encoding='utf-8').read(); m=[m for m in re.finditer(r'<script>(.*?)</script>',s,re.S)][-1]
open('/tmp/claude-0/leve.js','w',encoding='utf-8').write(m.group(1))
PY
javascript-obfuscator /tmp/claude-0/leve.js --output /tmp/claude-0/leve.obf.js --compact true --rename-globals true --reserved-names 'galMove' --string-array true --string-array-encoding base64 >/dev/null
python3 - <<'PY'
import re
P='mapa_sun_place_leve/index.html'; s=open(P,encoding='utf-8').read(); m=[m for m in re.finditer(r'<script>(.*?)</script>',s,re.S)][-1]
s=s[:m.start(1)]+open('/tmp/claude-0/leve.obf.js',encoding='utf-8').read()+s[m.end(1):]; open(P,'w',encoding='utf-8').write(s)
PY
rm -f mapa_grand_valley_netlify.zip; (cd mapa_sun_place_leve && zip -qr ../mapa_grand_valley_netlify.zip . -x '.*')
python3 $S/scripts/single.py $S/single
N=$(cat $S/single/names.txt)
javascript-obfuscator /tmp/claude-0/single.js --output /tmp/claude-0/single.obf.js --compact true --rename-globals true --reserved-names "galMove,$N" --string-array true --string-array-encoding base64 >/dev/null
python3 - "$S/single" <<'PY'
import sys
d=sys.argv[1]; sh=open(d+'/shell.html',encoding='utf-8').read()
out=sh.replace('@@IMGS@@',open(d+'/imgs.js').read()).replace('@@MAIN@@',open('/tmp/claude-0/single.obf.js',encoding='utf-8').read())
open('/mnt/user-data/outputs/gv_single/index.html','w',encoding='utf-8').write(out)
PY
cp mapa_grand_valley_cores.html mapa_sun_place_leve/index.html mapa_grand_valley_netlify.zip /mnt/user-data/outputs/gv2/
ls -la /mnt/user-data/outputs/gv_single/index.html
