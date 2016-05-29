import time
totaltime = time.time()
days = int(totaltime//(24*60*60))
hours = int((totaltime - days * (24*60*60))//3600)
minutes = int((totaltime - days * (24*60*60) - hours * 3600)//60)
seconds = int((totaltime - days * (24*60*60) - hours * 3600 - minutes * 60))

print ('days', days, 'hours', hours, 'minutes', minutes, 'seconds', seconds)
