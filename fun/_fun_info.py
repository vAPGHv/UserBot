async def fun_info_f(app, msg):
    await msg.edit("""Вот что я могу:
    <code>/hack</code> {t} эффект хакинга
    <code>/nohack</code> {t} эффект хакинга (неудача)
    <code>/inp</code> {t} эффект ввода текста
    <code>/spam</code> {i} спам
    
    {i} - любое количество итераций
    {t} - время в секундах
    
    Made by: @vapgsv
    Tester: @real_azart
    Version: 2.11 (04.02.23)
    """, parse_mode="html")
