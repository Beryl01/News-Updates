from flask import render_template, url_for, flash, redirect
# from forms import RegistrationForm, LoginForm
from . import main
from ..request import get_news, search_news, sources_news

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)


# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)     

@main.route("/")
def index():
    '''
    View root page function that returns the index page and its data
    '''
    top_headlines = get_news("top-headlines")

    title = "News headlines"

    search_news = request.args.get("news_query")
    search_sources = request.args.get("news_sources")
    if search_news:
        return redirect(url_for(".search", news_name=search_news))

    if search_sources:
        return redirect(url_for(".sources", sources_name=search_sources))

    return render_template("index.html", title=title, top=top_headlines)


@main.route("/search/<news_name>")
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f" Search results for {news_name}"

    return render_template("search.html", news=searched_news)


@main.route("/sources")
def sources():
    '''
    View function to display sources of news
    '''
    source = sources_news()
    title = f"{sources} news "

    return render_template("sources.html", source=source)

