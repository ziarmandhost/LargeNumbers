# Large numbers

### Що скоїться після виконання?
Зрозумієте, чому математика добре працює для використання забезпечення базових властивостей безпеки. І навіщо використовувати ключі та секрети великого розміру.

### Задача: 
Використовуючи одну з існуючих бібліотек (можете зробити самостійно, але краще все-таки використовувати існуючу для економії часу) вивести кількість варіантів ключів, які можна задати 8-,16-,32-,64-,128-, 256-, 512- , 1024-, 2048-, 4096-бітною послідовністю.
Приклад: Якщо довжина ключа дорівнює 16 біт - то простір ключів дорівнює 65,536.
Простір ключів – кількість унікальних ключів, які знаходяться у заданому діапазоні.
Для кожного з варіантів необхідно згенерувати випадкове значення ключа, яке знаходиться в діапазоні 0x00…0 до 0xFF…F залежно від обраної довжини ключа.
Написати функцію для брутфорсу значень з діапазону з метою знаходження ключа. Мета функції перебирати значення ключа від 0x00 ... 0 до тих пір, поки буде не знайдено значення, рівне попередньо згенерованого ключового. Функція повинна виводити кількість часу в мілісекундах, яка була витрачена для знаходження ключа.

https://peps.python.org/pep-0237/ - Python (bignum type)
