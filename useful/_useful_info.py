async def useful_info_f(app, msg):
    await msg.edit("""Вот что я могу:
    <code>/calk</code> калькулятор
    (В калькуляторе sqrt(x) это квадратный корень из x, а ** степень)
    <code>/bomb</code> {n} {i} телефон-бомбер
    
    {i} - любое количество итераций
    {n} - номер телефона
    
    Made by: @vapgsv
    Tester: @real_azart
    Version: 2.11 (04.02.23)
    """, parse_mode="html")
