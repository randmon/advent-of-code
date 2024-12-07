a,b=zip(*[tuple(map(int,c.split()))for c in open("1").read().strip().split("\n")])
f={g:b.count(g)for g in b}
print(sum(abs(d-e)for d,e in zip(sorted(a),sorted(b))),sum([l*f.get(l,0)for l in a]))

# 1873376 18997088
# 197 chars