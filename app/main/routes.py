from app.main import main
from flask import render_template, request, session, redirect, url_for, send_from_directory
from config import Config


@main.route('/')
def index():
    return render_template('site/index.html')


@main.route('/contact')
def contact():
    return render_template('site/contact.html')


@main.route('/founder')
def founder():
    return render_template('site/founder.html')


@main.route('/faq')
def faq():
    return render_template('site/faq.html')


@main.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(Config.FILE_FOLDER, filename, as_attachment=True)


@main.route('/walk-with-us')
def walk():
    return render_template('site/walk.html')


@main.route('/what-we-do')
def what_we_do():
    return render_template('site/what-we-do.html')


@main.route('/special-education')
def special_education():
    return render_template('site/special-education.html')


@main.route('/rehabilitation')
def rehab():
    return render_template('site/rehabilitation.html')


@main.route('/vocational')
def vocational():
    return render_template('site/vocational.html')


@main.route('/community')
def community():
    return render_template('site/community.html')


@main.route('/donate')
def donate():
    return render_template('site/donate.html')


@main.route('/news')
def blog():
    return render_template('site/blog.html')


@main.route('/news/OCT-Kenya-response-to-COVID-19-pandemic')
def blog_details():
    return render_template('site/blog-details.html')


@main.route('/news/graduation-ceremony-2018')
def blog_graduation():
    return render_template('site/blog-graduation.html')


@main.route('/news/disability-expo-2019')
def blog_disability_expo():
    return render_template('site/blog-disability-expo.html')


@main.route('/news/feed-the-future')
def blog_feeding():
    return render_template('site/blog-feeding.html')


@main.route('/news/a-visit-by-joseph-ole-lenku')
def blog_lenku():
    return render_template('site/blog-lenku.html')


@main.route('/news/our-5th-anniversary')
def blog_anniversary():
    return render_template('site/blog-anniversary.html')


@main.route('/news/ongoing-project')
def blog_ongoing():
    return render_template('site/blog-ongoing-project.html')


@main.route('/news/mou-signing')
def blog_mou():
    return render_template('site/mou-signing.html')


@main.route('/news/joint-emergency-intervention-plan')
def blog_emergency_intervention():
    return render_template('site/emergency-intervention.html')


@main.route('/news/international-day-of-disabled-persons')
def blog_disability_day():
    return render_template('site/disability-day.html')


@main.route('/events')
def events():
    return render_template('site/events.html')


@main.route('/event/<int:post_id>')
def event_details(event_id):
    return render_template('site/walk.html')


@main.route('/about')
def about():
    return render_template('site/about.html')


@main.route('/board')
def board():
    return render_template('site/board.html')


@main.route('/gallery')
def gallery():
    return render_template('site/gallery.html')


@main.route('/careers')
def careers():
    return render_template('site/careers.html')


@main.route('/language/<language>')
def set_language(language=None):
    session['language'] = language
    return redirect(url_for('main.index'))


@main.context_processor
def inject_conf_var():
    return dict(
        AVAILABLE_LANGUAGES=Config.LANGUAGES,
        CURRENT_LANGUAGE=session.get('language', request.accept_languages.best_match(Config.LANGUAGES.keys())))
