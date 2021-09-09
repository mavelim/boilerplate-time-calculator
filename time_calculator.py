def add_time(start, duration,starting_day=""):
	#armamos una lista con las horas para acceder a ellas y sumarlas
	semana=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	horas=[]
	horas.append(start.split(':')[0])
	horas= horas+start.split(":")[1].split()
	horas= horas+duration.split(':')
	new=horas[2]
	#realizamos las sumas
	#primero los minutos
	min=(int(horas[1])+int(horas[4]))%60
	desborde= (int(horas[1])+int(horas[4]))//60
	hor=(int(horas[0])+int(horas[3])+desborde)%12
	desb_dias=(int(horas[0])+int(horas[3])+desborde)//12
	#print(start,duration)
	if hor==0:
		hor=12
	dias_extra=desb_dias//2
	#print(dias_extra)
	cambio_hora=desb_dias%2
#	if horas[2]=="PM" and dias_extra>0:
#		dias_extra += 1
	if cambio_hora>0:
		if horas[2]=="PM":
			new="AM"
			dias_extra += 1
		else: new="PM"
	new_time=str(hor)+":"+str(min).rjust(2,'0')+" "+new
	if starting_day and dias_extra==0:
		new_time += ", "+starting_day.capitalize()
	elif starting_day and dias_extra>0:
		indice=semana.index(starting_day.capitalize())+dias_extra
		new_day= semana[indice%7]
		new_time += ", "+ new_day

	if dias_extra>1:
		new_time += " (%d days later)" %dias_extra
	elif dias_extra==1:
		new_time += " (next day)"

	#print(start, duration,starting_day)

	return new_time