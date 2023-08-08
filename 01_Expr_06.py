bh = int(input())
bm = int(input())
bs = int(input())
eh = int(input())
em = int(input())
es = int(input())

bt = bh * 3600 + bm * 60 + bs
et = eh * 3600 + em * 60 + es

if(bt > et):
    et += 24*60*60

diff = et-bt

dh = diff // 3600
diff -= dh*3600
dm = diff // 60
diff -= dm*60
ds = diff

print(str(dh)+":"+str(dm)+":"+str(ds))