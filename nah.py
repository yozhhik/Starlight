from flask import Flask, url_for, request
import sqlite3
app = Flask(__name__)


@app.route('/')
def main():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Коллонизация.mp3</title>
                      </head>
                      <body>
                        <img src="{url_for('static', filename='Starlight.png')}" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        <h1 style="color: purple">Это главная страница нашего сайта!!!</h1>
                        <h4 style="color: purple">Я эще не знаю что тут писать но потом тут что-то будет</h4>
                        <h4 style="color: purple">Представьте пожалуйста что тут разные фотки а не одна и та же</h4>
                        <img src="{url_for('static', filename='Картинка.png')}" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        <h2>
                        <div class="alert alert-danger" role="alert">
                          Я с друзьями делаем фоточку на память! Мы добрались до важной части нашей миссии поэтому все очень счасливы.
                        </div>
                        <img src="{url_for('static', filename='КартСвет.png')}" style="margin-left: 298px;"
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        <div class="alert alert-warning" role="alert">
                          В последнее время Света постоянно забывает включать все уровни защиты на корабле. Она оправдывается 
                          что это экономит энергию, но я считаю что на безопасности экономить нельзя да и энергии должно хватить так как она хорошо рассчитана базой.
                          Так что Свете стоит перестать придумывать оправдания и начать лучше делать свою работу.
                        </div>
                        <img src="{url_for('static', filename='синкарт.png')}" style="margin-left: 298px;" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        <div class="alert alert-success" role="alert">
                          Синий опять нарушает условия безопасности. Если бы он не был моим братом, я бы предложила 
                          закрыть его в его лаборатории, отчасти из-за его девиантного поведения, отчасти для того чтобы 
                          он сосредоточился на том чтобы успеть закончить основной проект перед возвращением, потому что 
                          недавно скорость его исследований заметно уменьшилась, кажется что-то сильно его беспокоит, но 
                          я практически уверена что он мне не расскажет, потому что не хочет ввязывать меня в его 
                          проблемы, в которые даже здесь он умудрился ввязаться. Я думаю что нужно попросить кого-нибудь 
                          из девчонок с ним поговорить(скорее всего Верочку), потому что они лучше меня общаются  с 
                          людьми, потому что когда я с людьми говорю, я прям вижу как им хочется назвать меня душнилой. 
                          Эх, не понимают они важности моей задачи.
                        </div>
                        <img src="{url_for('static', filename='Foto.png')}" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        <div class="alert alert-info" role="alert">
                          Андрей слишком редко проводит инвентаризацию. Доступность многих вещей не соответствует 
                          указанным в документациях. Интересно он их вообще читал? Если честно я не знаю читал ли он их 
                          мы с Синим и Верочкой читаем каждую новую документацию, я уверена что Вика заставляет 
                          их читать Свету, а Катрина Егора, Мари иногда читает их с нами, но во время когда мы их читаем 
                          она часто занята, так что она наверняка читает их сама, потому что они очень важны для ее 
                          работы и я не могу себе представить чтобы она их не читала. С Ромой то же самое, да и он очень 
                          часто на них ссылается, Мари тоже так делает, но реже Но Андрея я никогда не видела читающим 
                          документации, он никогда на них не ссылается и я могу себе представить что ему просто скучно 
                          их читать и он просто этого не делает, нужно будет пригласить его почитать их с нами, я 
                          уверена Синий сможет подать инфомацию в ней интересно, он в этом действительно хорош. Но а п
                          ока я только могу надеяться что он их все же читает и не будет нарушать рекомендаций.
                        </div>
                        <img src="{url_for('static', filename='Foto.png')}" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        <div class="alert alert-primary" role="alert">
                          Подпись к фотке. Тут что-то про безопасность.
                        </div>
                        <img src="{url_for('static', filename='Foto.png')}" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        <h2>
                        <div class="alert alert-danger" role="alert">
                          Подпись к фотке. Тут что-то про безопасность.
                        </div>
                        <img src="{url_for('static', filename='Foto.png')}" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        <div class="alert alert-warning" role="alert">
                          Подпись к фотке. Тут что-то про безопасность.
                        </div>
                        <img src="{url_for('static', filename='Foto.png')}" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        <div class="alert alert-success" role="alert">
                          Подпись к фотке. Тут что-то про безопасность.
                        </div>
                        <img src="{url_for('static', filename='Foto.png')}" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        <div class="alert alert-info" role="alert">
                          Подпись к фотке. Тут что-то про безопасность.
                        </div>
                        <img src="{url_for('static', filename='Foto.png')}" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        <div class="alert alert-primary" role="alert">
                          Подпись к фотке. Тут что-то про безопасность.
                        </div>

                        <div class="alert alert-dark" role="alert">
                          Тут будет больше фоток потом :(
                        </div>
                        </h2>
                      </body>
                    </html>'''


@app.route('/rules')
def rules():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Коллонизация.mp3</title>
                      </head>
                      <body>
                        <div class="alert alert-dark" role="alert">
                        Привет поситители моего сайта!
                        Это правила нашего сайта.
                        Правила просты. Непишите в комменты то что мне сильно не понравится - забаню.
                        Хрень не пишем. Инциндент не упоминаем. Упомянете - сразу забаню.'''


@app.route('/blocked/39030932')
def blocked():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Коллонизация.mp3</title>
                      </head>
                      <body>
                        <div class="alert alert-dark" role="alert">
                        Убирайтесьизмоейголовы
                        {'убирайтесьизмоейголовыубирайтесьизмоейголовыубирайтесьизмоейголовыубирайтесьизмоейголовыубирайтесьизмоейголовыубирайтесьизмоейголовыубирайтесьизмоейголовыубирайтесьизмоейголовы<br>' * 1000}
                        {'Ядолжнавасзабытьничегонепроизошлоничегонепроизошлоячтотозабываю?почемумнетакхолодно?неужелизиманаступила?всеонизнаютчтопроизошлоитолькоянеимеюникаогопонятиягдеонигдеянеужелияпроигралачтоязабываюничегничегоничего' * 1}
                        {'ничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничегоничег<br>' * 1000}
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Воспоминания заблокированы.
                        </div>
                        </h2>
                      </body>
                    </html>'''


@app.route('/Cams')
def cam():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1 style="color: red">Камера №73</h1>


                        <img src="{url_for('static', filename='Mars.jpg')}" 
                        alt="!Error!129 Ошибка камеры">
                      <h4>Субьект №73</h4>
                      <p>Описание:</p>
                      <p>Имя: Полина Леонова</p>
                      <p>Дата рождения:07.03.3644</p>
                      <p>Место рождения:Планета Земля, Объедененный мир, Квантовская область, город Кваквовск</p>
                      <p>Пол: Женский</p>
                      <p>Причина попадания: Единственная выжившая после инциндента 3667. <br>
                      Находится в состоянии комы после неудачного анабиоза. <br>
                      Её мозг функционирует стабильно, но кажется она не планирует просыпаться. <br>
                      Она способна общаться через чат и активно пишет на свой сайт, <br>
                      но не понимает что происходит и не осознает что она спит.<br>
                      У нее велики шансы проснуться и восстоновиться если она сможет полностью осознать ситуацию, <br>
                      хоть это осознание и будет для нее болезненно.</p>
                      </body>


                    </html>"""


@app.route('/arhives/3662')
def arhives3662():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Коллонизация.mp3</title>
                      </head>
                      <body>
                        <h1>Марсианская миссия 3662.</h1>

                        <img src="{url_for('static', filename='Foto.png')}" 
                        alt="!Error!271 Изображение отсутствует в памяти">
                        <h2>
                        <div class="alert alert-danger" role="alert">
                          Мы, ООКМ представляем замечательную экспедицию на Марс под кодовым названием Starlight
                        </div>
                        <div class="alert alert-warning" role="alert">
                          10 молодых экспертов прошедших нашу продвинутую подготовку и уже имеющих огромное количество заслуг отправятся 
                        </div>
                        <div class="alert alert-success" role="alert">
                          Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-info" role="alert">
                          И начнем с Марса!
                        </div>
                        <div class="alert alert-primary" role="alert">
                          Присоединяйся!
                        </div>
                        </h2>
                      </body>
                    </html>'''


@app.route('/arhives/3667')
def arhives3667():
    return '''f<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Коллонизация.mp3</title>
                      </head>
                      <body>
                        <h1>Миссия на Энцелад 3667.</h1>

                        <img src="{url_for('static', filename='Foto.png')}" 
                        alt="!Error!271 Изображение отсутствует в памяти">
                        <h2>
                        <div class="alert alert-dark" role="alert">
                          Звездная команда собирается вновь для исследований далекого космоса.
                        </div>
                        <div class="alert alert-dark" role="alert">
                          На космическом корабле новой модели "Звезда-2" 
                        </div>
                        <div class="alert alert-dark" role="alert">
                          команда наших лучших исследователей вернется к исследованию бескрайного космоса.
                        </div>
                        <div class="alert alert-dark" role="alert">
                          К 5-летнему юбилею Марсианской миссии 3662 весь сосатав успешной миссии был снова созван и в 
                        </div>
                        <div class="alert alert-dark" role="alert">
                          полном составе полетят на далекий Энцелад, подающий надежду на нахождение большого количества чистой воды. 
                        </div>
                        <div class="alert alert-dark" role="alert">
                          Миссия, ставшая возможной из-за новых технологий, которые еще недавно казались фантастикой.
                        </div>
                        <div class="alert alert-dark" role="alert">
                          Технология анабиоза и проднинутый ИИ автопилота позволит учасникам лучше перенести долгий полет.
                        </div>
                        <div class="alert alert-dark" role="alert">
                          И пускай условия полета несомненно отличаются от предыдущего наши космические рейнжеры определенно принесут нам еще один оглушительный успех.
                        </div>
                        <div class="alert alert-dark" role="alert">
                          3667 Организация общемировых космических миссий.
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Ничего не могло пойти не так. Ничего не должно было пойти не так. Почему? ПОЧЕМУ?
                        </div>
                        </h2>
                      </body>
                    </html>'''


@app.route('/void')
def void():
    return f'''<!doctype html>
                        <html lang="en">
                        <body>
                    <<img src="{url_for('static', filename='n0thing.png')}" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                    <<img src="{url_for('static', filename='Без имени.png')}" 
                        alt="!Error!271 Изображение забыло сгенерироваться">
                        </body>'''



@app.route('/registration', methods=['POST', 'GET'])


def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Регистрвция в нашей системе</h1>
                            <h4>вставьте текст</h4>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите логин" name="surname">
                                    <input type="password" class="form-control" id="name" placeholder="Введите пароль" name="name">
                                    <label>  </label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <label>  </label>
                                    <input type="tel" class="form-control" id="tel" aria-describedby="telHelp" placeholder="Введите номер телефона" name="tel">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Пятое</option>
                                          <option>Десятое</option>
                                          <option>А тебе зачем знать?</option
                                    </select>
                                     </div>
                                     </div>
                                        <div class="form-group form-check">
                                        <input type="color" class="form-check-input" id="color" name="color">
                                        <label class="form-check-label" for="acceptRules">Какой твой любимый цвет?</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male">
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="kafel" value="kafel">
                                          <label class="form-check-label" for="female">
                                            Кафельный
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="parket" value="parket">
                                          <label class="form-check-label" for="female">
                                            Паркетный
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="neskagy" value="neskagy">
                                          <label class="form-check-label" for="female">
                                            Что за вопросы?
                                          </label>
                                        
                                        </div>
                                        <label>  </label>
                                    </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="candy" name="candy">
                                        <label class="form-check-label" for="candy">Вам больше 18 конфет?</label>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию табурета*</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="classSelect">Зачем вы здесь?</label>
                                        <select class="form-control" id="why" name="why">
                                          <option>Да</option>
                                          <option>Нет</option>
                                          <option>Жареный скелет</option>
                                          <option>Оранжевый медвед</option>
                                          <option>Сладкий рулет и свежий омлет</option>
                                          <option>Калий</option>
                                    </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Напишите сочинение-описание данной картинки: Файл не найден</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="classSelect">Выберете вашу любимую строчку данной песни</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Never gonna give you up</option>
                                          <option>Never gonna let you down</option>
                                          <option>Never gonna run around and desert you</option>
                                          <option>Never gonna make you cry</option>
                                          <option>Never gonna say goodbye</option>
                                          <option>Never gonna tell a lie and hurt you</option>
                                    </select>
                                    </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Тест на табурет** Нажми на коробку если нет</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                                </p>
                                        *табурет:
                                        телескопическая
                                        аэродинамичная
                                        балансировочная
                                        увеличительная
                                        равноугольная
                                        единовременная
                                        табуретка
                                        </br>
                                        **Проходя этот тест вы автоматически соглашаетесь с правилами пользовательского соглашения*** А табуретов мы не регестрируем.
                                        </br>
                                        ***(Его нет)
                                </p>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        if request.form['name'] == '0':
            return "00000000000000000000000"
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['email'])
        print(request.form['tel'])
        print(request.form['class'])
        print(request.form['color'])
        print(request.form['sex'])
        print(request.form['candy'])
        print(request.form['file'])
        print(request.form['why'])
        print(request.form['about'])
        print(request.form['accept'])
        if request.form['accept'] != 'on':
            return "Табуретов не регестрируем"
        else:
            con = sqlite3.connect('db/regs.db')
            cur = con.cursor()
            oi = '\n'.join([request.form['email'], request.form['tel'], request.form['class'], request.form['color'], request.form['sex'], request.form['candy'], request.form['file'], request.form['why'], request.form['about'], request.form['accept']])
            result = cur.execute(f"""INSERT INTO regs(login, password, level, otherinfo) VALUES({request.form['name']}, {request.form['surname']}, {1}, {oi})""").fetchall()
            con.close()
            return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

'''
saddy0056_sv
s3640eltusvmis28
'''