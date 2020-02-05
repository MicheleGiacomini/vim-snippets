texmathzones = ['texmathzone'+x for x in ['a', 'as', 'b', 'bs', 'c',
'cs', 'd', 'ds', 'e', 'es', 'f', 'fs', 'g', 'gs', 'h', 'hs', 'i', 'is',
'j', 'js', 'k', 'ks', 'l', 'ls', 'ds', 'v', 'w', 'x', 'y', 'z']]

texignoremathzones = ['texmathtext']

texmathzoneids = vim.eval('map('+str(texmathzones)+", 'hlid(v:val)')")
texignoremathzoneids = vim.eval('map('+str(texignoremathzones)+", 'hlid(v:val)')")

ignore = texignoremathzoneids[0]

def math():
	synstackids = vim.eval("synstack(line('.'), col('.') - (col('.')>=2 ? 1 : 0))")
	try:
		first = next(
            i for i in reversed(synstackids)
            if i in texignoremathzoneids or i in texmathzoneids
        )
		return first != ignore
	except stopiteration:
		return false
