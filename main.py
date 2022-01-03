from flask import Flask, render_template, redirect
from form import TaskForm
from config import Config

app = Flask(
  'app',
  template_folder='templates'
)
app.config.from_object(Config)

my_list = []
def add_to_list(task):
  my_list.append(task)
  print(my_list)

@app.route('/')
def hello_world():
  return render_template('basic.html')

@app.route('/todo', methods=['GET','POST'])
def todo():
  form = TaskForm()
  if form.is_submitted():
    print("made it")
    add_to_list(form.task.data)
    return redirect('/mylist')
  return render_template('todo.html', form=form)
 

@app.route('/mylist')
def mylist():
  return render_template('mylist.html', my_list=my_list)

app.run(host='0.0.0.0', port=8080)