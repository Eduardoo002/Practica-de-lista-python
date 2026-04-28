productos = ["Jabon", "Deterente", "Papel higienico"]

otros_productos = ["Jabon de platos", "Cloro" ]

productos.extend(otros_productos)

productos.remove("Deterente")

print(productos)

productos.insert(1, "Desinfectante")

productos.sort(reverse=True)

print(productos)

