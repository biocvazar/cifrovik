#!/usr/bin/env python3
print("Content-Type: text/html\n\n")

from footer import footer
from header import header

title = "Про мене"
print(header % title)
print('''
<div class="text">
    <h1>Інформація про мене</h1>
</div>
	<div id="data">
		<div id="data2">
		<img src="..\images\\face.png">
		</div>
		<div id="data3" >
			Cтудент гр. Кнм-14.
			<br>
			Виконання лаб. роботи №1 з курсу
			<br>
			"Семантичні веб- та грід-мережі"
			<br>
			Розробка макету інтернет магазину
		</div>
	
	
		<div class="techs" align="right">
			Використані технології
			<br>
			<img class="tech_img" align="right" src="..\images\\css.png">
			<img class="tech_img" align="right" src="..\images\\html.png">
			<img class="tech_img" align="right" src="..\images\\python.jpg">
		</div>
	</div>





'''
)
print(footer)