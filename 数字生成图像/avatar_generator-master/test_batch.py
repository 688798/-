import identicon
def gen_avatar_batch(code,size):
	img= identicon.render_identicon(code, 16)
	#img.show()
	img.save('%s_%s.png'%(code,size))

for x in range(10000000,10000000+5):
    gen_avatar_batch(x, 16)
for x in range(20000000,20000000+5):
    gen_avatar_batch(x, 16)
for x in range(40000000,40000000+5):
    gen_avatar_batch(x, 16)
for x in range(80000000,80000000+5):
    gen_avatar_batch(x, 16)
for x in range(160000000,160000000+5):
    gen_avatar_batch(x, 16)