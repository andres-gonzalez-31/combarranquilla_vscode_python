from flask import Flask, render_template, session

app=Flask(__name__, template_folder='templates')
app.secret_key = 'SOME KEY '

@app.route('/')
def inicio():
    return render_template(template_name_or_list='index.html',message='Index')

@app.route('/set_data')
def set_data():
    session['name']='mike'
    session['other']='hello world'
    return render_template(template_name_or_list='index.html',message='session data set.')
    

@app.route('/get_data')
def get_data():
    if 'name' in  session.key() and 'other' in session.key():
        name = session['name']
        other = session['other']
        return render_template(template_name_or_list='index.html',message=f'name: {name}, other: {other}')
    else:
        return render_template(template_name_or_list='index.html',message=f'No Session no Found')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)