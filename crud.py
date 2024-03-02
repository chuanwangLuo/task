from flask import Flask, render_template, request, redirect, url_for
from models import db, Task  # 导入数据库模型和任务模型

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)

# 创建任务
@app.route('/create', methods=['POST'])
def create_task():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_task = Task(title=title, content=content)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))

# 读取任务列表
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# 更新任务
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.content = request.form['content']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', task=task)

# 删除任务
@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
