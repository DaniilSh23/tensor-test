# Тестовый проект для вакансии "Тензор"

## Используемые библиотеки
* pytest==6.2.5
* selenium==4.1.3
* loguru==0.6.0

## Краткое описание
Данный проект выполнен в качестве тестового задания для вакансии компании "Тензор". Реализован на основе паттерна PageObject.
Код обеспечивает выполнение следующих манипуляций с браузером Google Chrome:

### Поиск в яндексе
* Зайти на yandex.ru
* Проверить наличия поля поиска
* Ввести в поиск Тензор
* Проверить, что появилась таблица с подсказками (suggest)
* При нажатии Enter появляется таблица результатов поиска
* Проверить 1 ссылка ведет на сайт tensor.ru
### Картинки на яндексе
* Зайти на yandex.ru
* Проверить, что ссылка «Картинки» присутствует на странице
* Кликаем на ссылку
* Проверить, что перешли на url https://yandex.ru/images/ (пункт реализован, как поиск подстроки в строке, т.к. текущая ссылка Яндекса не соответствует в точности той, что указана в задании)
* Открыть первую категорию изображений
* Проверить, что название категории отображается в поле поиска
* Открыть 1 картинку
* Проверить, что картинка открылась
* Нажать кнопку вперед
* Проверить, что картинка сменилась
* Нажать назад
* Проверить, что картинка осталась из шага 8