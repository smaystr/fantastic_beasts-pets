pth = []
builtins = {'global': {}}
global_ans = []
query_names = ('add', 'create', 'get')


def tree_dict(b, t, val=None):
    for k, v in b.items() if isinstance(b, dict) else enumerate(b):
        if isinstance(v, (list, tuple, dict)):
            p = tree_dict(v, t, val)
            if p:
                if not isinstance(val, (type(None), dict)):
                    pth.append(k)
                return p
        if t[0] in (k, v):
            if isinstance(val, (type(None), dict)):
                b[t[0]].update({t[1]: val})
            else:
                return t[0] if v and t[1] in v else t[1]


for query in range(int(input())):
    t = [str(i) for i in input().split(' ')]
    if t[0] == query_names[0]:
        tree_dict(builtins, (t[1], t[2]), val={})
    elif t[0] == query_names[1]:
        tree_dict(builtins, (t[2], t[1]), val={})
    elif t[0] == query_names[2]:
        pth = [t[1]]
        for ti in pth:
            ans = tree_dict(builtins, (ti, t[2]), val=query_names[2])
            if ans == ti:
                pth = []
                break
            else:
                ans = None
        else:
            pth = []
            ans = None
        global_ans.append(ans)

for value in global_ans:
    print(str(value))
