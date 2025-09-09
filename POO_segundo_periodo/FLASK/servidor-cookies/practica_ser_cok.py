from flask import Flask, render_template, session, make_response, request

aa= Flask(__name__, template_folder='templates')
aa.secret_key = 'hola mundo'

@aa.route('/')
def index():
    return render_template(template_name_or_list = 'index.html', message ='Index')

@aa.route('/set_data')
def set_data():
    session['name'] = 'andres'
    session['other'] = 'hello world'
    return render_template (template_name_or_list= 'index.html',message = 'session data set.')

@aa.route('/get_data')
def get_data():
 if 'name' in session.keys() and 'other' in session.keys():
    name =session ['name']
    other =session ['other']
    return render_template  (template_name_or_list= 'index.html', message =f'name: {name}, other: {other}') 
 else:
    return render_template  (template_name_or_list= 'index.html', message ='no session found.')
 
@aa.route('/clear_session')
def clear_session():
   session.clear()
   return render_template (template_name_or_list= 'index.html', message = 'session cleared.')

@aa.route('/set_cookie') 
def set_cookie():
   response = make_response(render_template(template_name_or_list= 'index.html', message = 'cookie set'))
   response.set_cookie( key= 'cookie_name', value= 'cookie_value')
   return  response 


@aa.route('/get_cookie') 
def get_cookie():
   cookie_value = request.cookies['cookie_name']
   return render_template(template_name_or_list= 'index.html', message=f'cookie_value:{cookie_value}') 
   
@aa.route('/remove_cookie') 
def remove_cookie():
   response = make_response(render_template (template_name_or_list='index.html', message = 'cookie removed.'))
   response.set_cookie(key = 'cookie_name', expires= 0)
   return response
   

if __name__=='__main__':
    aa.run (host='0.0.0.0',debug=True)