ingreso_mensual = 20000
gasto_mensual = 17000

# if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:         # pertenece a if
        print("estas en deficit")                   # pertenece a if
    elif ingreso_mensual - gasto_mensual > 3000:    # pertenece a if
        print("bien pa, estas bien")                # pertenece a if
    else:
        print("y pa, estas gastando una banda, hay que ver si te alcanza")  # pertenece a if
        
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
    
elif ingreso_mensual > 500:
    print("estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("estas bien en venezuela")

else:
    print("eres pobre")