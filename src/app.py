import csv
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='../templates', static_folder='../static')
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_transactions.csv')

def load_transactions():
    transactions = []
    total_income = 0
    total_expense = 0
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                transactions.append(row)
                amount = int(row["Amount"])
                if row["Type"] == "収入":
                    total_income += amount
                else:
                    total_expense += amount
    return transactions, total_income, total_expense

@app.route('/')
def index():
    transactions, income, expense = load_transactions()
    return render_template('index.html', transactions=transactions,
                           income=income, expense=expense, balance=income-expense)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        description = request.form['description']
        ttype = request.form['type']
        amount = request.form['amount']

        with open(DATA_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(["Date", "Category", "Description", "Type", "Amount"])
            writer.writerow([date, category, description, ttype, amount])

        return redirect(url_for('index'))

    return render_template('add_transaction.html')

if __name__ == '__main__':
    app.run(debug=True)
