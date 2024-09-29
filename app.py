from flask import Flask, render_template
import csv

app = Flask(__name__, template_folder='.')

# Function to read URLs from the CSV file
def read_urls_from_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append({
                'Website': row['Website'].strip(),
                # 'Description': row['Description'].strip()
            })
    return data

# Route to display the home page
@app.route('/')
def home():
    # data = read_urls_from_csv('companies.csv')  # Ensure the path is correct
    # return render_template('index.html', data=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
