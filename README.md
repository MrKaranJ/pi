# Pi Calculator

Pi was originally defined as the ratio of the circumference of a circle to its diameter. But calculating it mathematically is quite tricky. There have been multiple definitions since then and various ways of calculating it. Originally Archimedes approximated it using polygons as shown below but the definition uses the sine of the angle which in itseld provides quite a lot of complications to calculate such as the Taylor expansion or the CORDIC method. 

![Archimedes Formula](/images/archimedes.png)

As n increases, the polygon will be a better approximate of a circle and will we get a better estimate of Pi.

Here a simple program has been written to calculate Pi using the [**Bailey–Borwein–Plouffe**](https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula) (BBP) formula. Which is defined as shown below:

![BBP Formula](/images/bbp.png)

To use the program. Use the defined function 'getpi' in main.py with an argument N for the precision required. With N = 100, the function returns Pi upto 100 decimal places. Run main.py to check the function.