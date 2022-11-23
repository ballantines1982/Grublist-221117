from flask import Flask, request, render_template, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = "AliceEllenHugo"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meals.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ymaqlnniohhywp:05eea2eefa5f47549021243b8af0704dc4babd1eebb3128d79241646c618a16f@ec2-54-86-214-124.compute-1.amazonaws.com:5432/d5a7qds2o2ij75'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

    
today = datetime.today().date()
week = today.isocalendar()[1]

migrate = Migrate(app, db)
class Meal(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quant = db.Column(db.Integer, nullable=False)
    meal_type = db.Column(db.String(100), nullable=False)
    protein = db.Column(db.String(100))
    last_ate = db.Column(db.String(100))
    created = db.Column(db.String(100))
    child_ok = db.Column(db.Boolean)

    
    def __repr__(self):
        return f'{self.id} {self.name} {self.quant} {self.meal_type} {self.protein} {self.last_ate} {self.created} {self.child_ok}'


@app.route('/', methods = ['POST', 'GET'])
def index():
    today = datetime.today().date()
    meals = Meal.query.all()
    if request.method == 'POST':
        if request.form['btn'] == 'Addera':
            name = request.form['meal']
            quant = request.form['no_of_meals']
            #meal_type = request.form['meal_type']
            protein = request.form['protein']
            
            meal = Meal(name=name, quant=quant, meal_type="", last_ate="", created=today, protein=protein)

            db.session.add(meal)
            db.session.commit()
    
            return redirect(url_for('index'))
        # elif request.form['btn'] == 'Middag':
        #     meal = Meal.query.get_or_404(meal_id)
        #     meal.last_ate = today
            
        #     db.session.add(meal)
        #     db.session.commit()
        #     return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
    return render_template('index.html', meals=meals)
            
@app.route('/<int:meal_id>/edit/', methods=['POST', 'GET'])
def edit(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    
    if request.method == 'POST':
        if request.form['btn'] == 'Spara':
            name = request.form['meal']
            quant = request.form['no_of_meals']
            protein = request.form['protein']
            last_ate = request.form['last_ate']
            
            meal.name = name
            meal.quant = quant
            meal.protein = protein
            meal.last_ate = last_ate
            
            db.session.add(meal)
            db.session.commit()
            return redirect(url_for('index'))

        else:
            meal = Meal.query.get_or_404(meal_id)
            db.session.delete(meal)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('edit.html', meal=meal)

@app.route('/<int:meal_id>/delete/', methods=['POST', 'GET'])
def delete(meal_id):
    if request.method == 'GET':
        meal = Meal.query.get_or_404(meal_id)
        db.session.delete(meal)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/<int:meal_id>/select/', methods = ['POST', 'GET'])
def select(meal_id):
    if request.method == 'POST':
        if request.form['btn'] == 'Middag':
            meal = Meal.query.get_or_404(meal_id)
            meal.last_ate = today
            
            db.session.add(meal)
            db.session.commit()
            
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)

