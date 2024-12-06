import re
i=open("3").read().replace("\n","")
p=r"mul\((\d+),(\d+)\)"
print(sum(int(a)*int(b)for a,b in re.findall(p,i)))
i=re.sub(r"don't\(\).*?(do\(\))","",i)
print(sum(int(a)*int(b)for a,b in re.findall(p,i[:i.find("don't()")])))

# 189527826 63013756
# 237 chars