Есть два поля ввода:


1 f(x):
    
   
   Сюда можно ввести функцию, зависимую от переменной Х, реализованы стандартные арифметические операции, а также несколько
математических функций, таких как:
     
   1. ^ - возведение в степень ( x^2 - икс в степени 2)
     
   2. cos() - косинус ( cos(x) - косинус от х)
     
   3. sin() - синус (sin(x) - синус от х)
     
   4. tan() - танганс (tan(x) - тангенс от х)
     
   5. cot() - котангенс (cot(x) - котаненс от х)
     
   6. exp() - экспонента (exp(x) - e в степени х)
     
   7. log() - логарифм (2log(x) - логарифм х по основанию 2)
     
   8. ln() - натуральный логарифм (ln(x) - натуральный логарифм от х)
     
   9. sqrt() - квадратный корень (sqrt(x) - квадратный корень от х)
   
   Все эти функции и операции можно объединять в более сложные функции, однако не исключено
наличие багов, связанных с парсингом математических операций. От большинства багов
позволяет избавится логичное расставление скобок.
   После ввода функции можно указать один или несколько аргументов через символ ";".
   Первые два аргумента - начало и конец контрольных точек Х, третий аргумент - количество
точек. По умолчанию аргументы равны (0;50;1000)

2 Массив значений:
    
   Сюда можно ввести массив значений в формате [<значения на оси Х>][<значения на оси Y>]
    Значений должно быть одинаковое количество в обоих списках! Иначе это приведет к вылету.

Если вы указываете функцию, а затем массив значений - по нажатию кнопки "нарисовать" будет выведен график массива значений,
поле ввода функции же сотрется
