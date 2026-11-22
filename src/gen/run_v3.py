import v3_platform,v3_how,v3_ind,v3_sec,v3_co,v3_brief,inspect
OUT='/home/claude/mc2/project/'
jobs={'Platform-V3.dc.html':v3_platform,'HowWeWork-V3.dc.html':v3_how,'Industries-V3.dc.html':v3_ind,'Security-V3.dc.html':v3_sec,'Company-V3.dc.html':v3_co,'Briefing-V3.dc.html':v3_brief}
for fn,m in jobs.items():
    fs=[f for n,f in inspect.getmembers(m,inspect.isfunction) if f.__module__==m.__name__ and not inspect.signature(f).parameters]
    out=[f() for f in fs]; out=[o for o in out if isinstance(o,str) and '<x-dc' in o]
    assert len(out)==1,(fn,[f.__name__ for f in fs]); open(OUT+fn,'w').write(out[0]); print('wrote',fn)
