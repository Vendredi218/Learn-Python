print filter(lambda s: s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END'])

print filter(lambda s: s, ['test', None, '', 'str', '  ', 'END'])