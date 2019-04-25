from flask import Flask, render_template, redirect
import os
import urllib


BASEPATH = '/Users/anto/src/gnegnu/'

app = Flask(__name__)
app.jinja_env.filters['quoteplus'] = lambda u: urllib.parse.quote(u)

@app.template_filter('basename')
def basename(path):
    return os.path.basename(path)

def get_item_list(path):
    with os.scandir(path) as it:
        return [entry.name.replace('.md', '')
                for entry in it if entry.is_dir() or
                (entry.is_file() and entry.name.endswith('.md'))]

@app.route('/')
def home():
    path = ''
    fullpath = BASEPATH
    if os.path.isdir(fullpath):
        items = get_item_list(fullpath)
        return render_template('listdir.html',
                path=path, items=items)

@app.route('/<path:path>')
def path(path):
    fullpath = os.path.join(BASEPATH, path)
    try:
        mdcontent = open(f'{fullpath}.md').read()
    except FileNotFoundError:
        if os.path.isdir(fullpath):
            items = get_item_list(fullpath)
            return render_template('listdir.html',
                    path=path, items=items)
        else:
            print('notdir')
            parent_path = '/'+os.path.dirname(path)
            return redirect(parent_path)
            #print('/'.join(path.split('/')[:-1]))
            #return redirect('/'+'/'.join(path.split('/')[:-1]))
    # The path can either be a markdown document or a directory path
    return render_template('simple.html',
            path=path, mdcontent=mdcontent)

def main():
   app.run(debug=True)