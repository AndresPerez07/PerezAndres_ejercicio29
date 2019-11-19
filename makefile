diffusivity_equation.png: datos_diff.dat plot_DE.py
	python plot_DE.py
datos_diff.dat: DE.x
	./DE.x
DE.x: DE.cpp
	g++ DE.cpp -o DE.x

clean:
	rm DE.dat DE.x 
