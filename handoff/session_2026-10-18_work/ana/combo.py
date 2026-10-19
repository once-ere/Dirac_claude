import sys
from PIL import Image
pages=[int(x) for x in sys.argv[2:]]
imgs=[Image.open('/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad/ana/png/h-%02d.png'%i) for i in pages]
w=sum(i.width for i in imgs); h=max(i.height for i in imgs)
m=Image.new('RGB',(w,h),'white'); x=0
for i in imgs: m.paste(i,(x,0)); x+=i.width
m.save('/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad/ana/png/'+sys.argv[1])
