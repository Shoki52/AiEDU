from flask import Flask, render_template, request

app = Flask(__name__)

# Главная страница
@app.route('/')
def hello_page():
    return render_template('index.html')

# Страница лекции
@app.route('/lecture', methods=['GET', 'POST'])
def lecture_page():
    if request.method == 'POST':
        # Получаем ответы теста из формы
        answer_1 = request.form.get('q1')
        answer_2 = request.form.get('q2')
        answer_3 = request.form.get('q3')
        answer_4 = request.form.get('q4')
        answer_5 = request.form.get('q5')

        # Правильные ответы
        correct_answers = {
            'q1': 'b',  # Правильный ответ для вопроса 1
            'q2': 'b',  # Правильный ответ для вопроса 2
            'q3': 'c',  # Правильный ответ для вопроса 3
            'q4': 'a',  # Правильный ответ для вопроса 4
            'q5': 'a',  # Правильный ответ для вопроса 5
        }

        # Логика проверки правильности
        results = {
            'q1': answer_1 == correct_answers['q1'],
            'q2': answer_2 == correct_answers['q2'],
            'q3': answer_3 == correct_answers['q3'],
            'q4': answer_4 == correct_answers['q4'],
            'q5': answer_5 == correct_answers['q5'],
        }

        # Передаем результаты в шаблон
        return render_template('results.html', results=results)

    return render_template('lecture.html')

# Страница чтения
@app.route('/reading')
def reading_page():
    return render_template('reading.html')

# Страница практики
@app.route('/practical', methods=['GET', 'POST'])
def practical_page():
    if request.method == 'POST':
        # Получаем ответ из формы
        user_answer = request.form.get('answer')
        # Здесь можно добавить логику обработки ответа
        return render_template('practical.html', user_answer=user_answer)
    return render_template('practical.html')

if __name__ == "__main__":
    app.run(debug=True)
