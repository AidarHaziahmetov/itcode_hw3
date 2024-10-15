﻿# hw4
`Python 3.12.4`
## Задание 1
#### Добавил категорию Джинсы и вывел все категории
![img.png](images/img.png)
#### Добавил категорию Носки и вывел все категории
![img_1.png](images/img_1.png)
#### Добавил категорию Шорты и вывел все категории
![img_2.png](images/img_2.png)
## Задание 2
### filter
#### Фильтр по цене <= 2500
![img_3.png](images/img_3.png)
#### Фильтр по цене >= 2500
![img_4.png](images/img_4.png)
#### Фильтр товаров содержащих категорию "Футболки, майки"  
![img_5.png](images/img_5.png)
### exclude
#### Исключаем товары дороже или равные 2000
![img_6.png](images/img_6.png)
#### Исключаем товары дешевле или равные 3000
![img_7.png](images/img_7.png)
#### Исключаем товары категории "Футболки, майки"
![img_8.png](images/img_8.png)
### order_by
#### Сортировка по цене по возрастанию
![img_9.png](images/img_9.png)
#### Сортировка по цене по убыванию
![img_10.png](images/img_10.png)
#### Сортировка по алфавиту в обратном порядке
![img_11.png](images/img_11.png)
### Пример сложного запроса
#### Товары дороже 2000 не из категории "Футболки, майки" отсортированные по убыванию цены
![img_12.png](images/img_12.png)
## Задание 3

#### Заказы сделанные пользователем Aidar
![img_22.png](images/img_22.png)
#### Заказы сделанные всеми кроме пользователя Damir
![img_23.png](images/img_24.png)
#### Пользователи у которых в профиле есть аватар
![img_15.png](images/img_15.png)

### values()
#### Заказы сделанные пользователем Aidar
![img_13.png](images/img_13.png)
#### Заказы сделанные всеми кроме пользователя Damir
![img_34.png](images/img_34.png)
#### Пользователи у которых в профиле есть аватар
![img_25.png](images/img_25.png)

### values_list()
#### Заказы сделанные пользователем Aidar
![img_26.png](images/img_26.png)
#### Заказы сделанные всеми кроме пользователя Damir
![img_14.png](images/img_14.png)
#### Пользователи у которых в профиле есть аватар
![img_27.png](images/img_27.png)

## Задание 4
### AND
#### Цена от 2000 до 4000
![img_16.png](images/img_16.png)
#### В наличии больше 10 и цена меньше 4000
![img_17.png](images/img_17.png)
#### В наличии больше 20 и нет описания
![img_18.png](images/img_18.png)
### OR
#### Заказы от пользователей Aidar и Rina
![img_19.png](images/img_19.png)
#### Товары не из категорий Платья и Трусы
![img_20.png](images/img_20.png)
#### Товары из категорий Платья и Трусы
![img_21.png](images/img_21.png)
### and & or
#### Товары не из категории Платья в наличии с ценой от 2000 до 5000
![img_28.png](images/img_28.png)
#### Товары из категорий "Футболки, майки" или "Рубашки и блузы" исключая товары кол-во которых < 5 или > 50  
![img_29.png](images/img_29.png)
#### Товары из категорий "Футболки, майки" или "Рубашки и блузы" исключая товары цена которых < 2000 или > 5000
![img_30.png](images/img_30.png)
## Задание 5
### annotate
#### Катерогия и цена самого дорогого товара в категории
![img_31.png](images/img_31.png)
#### Катерогия и цена самого дешевого товара в категории
![img_32.png](images/img_32.png)
#### Катерогия и средняя цена товара в категории
![img_33.png](images/img_33.png)
### aggregate
#### Максимальная цена товара во всех категориях
![img_35.png](images/img_35.png)
#### Средняя цена товара во всех категориях
![img_36.png](images/img_36.png)
#### Минимальная цена товара во всех категориях
![img_37.png](images/img_37.png)