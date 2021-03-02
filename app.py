import os
from flask import( 
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/aboutus")
def aboutus():
    return render_template('about.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/depart")
def depart():
    return render_template('departments.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/chatbot")
def chatbot():
    return render_template('chatbot.html')


@app.route("/prescript", methods=["GET", "POST"])
def prescript():
    if request.method == "POST":
        proc = {
            "name": request.form.get("name").lower(),
            "title":request.form.get("title").lower(),
            "prescription_date": request.form.get("due_date").lower(),
            "pat_name":request.form.get("pat_name").lower(),
            "pat_idnum": request.form.get("id_num").lower(),
            "pharmarcy_location": request.form.get("pharmarcy_location").lower(),
            "medication_details": request.form.get("medication_details").lower(),
            "additional_information": request.form.get("additional_information").lower(),
            "created_by": session["user"]
        }
        mongo.db.prescriptions.insert_one( proc)
        flash("Prescription Submited")
        return redirect(url_for("prescript"))

    categories = mongo.db.prescriptions.find().sort("name", 1)
    role = mongo.db.users.find_one(
        {"username": session["user"]})["role"]

    return render_template("prescriptions.html", categories=categories, role=role)    



@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        task = {
            "name": request.form.get("name"),
            "title":request.form.get("title"),
            "test_date": request.form.get("due_date"),
            "pat_name":request.form.get("pat_name"),
            "pat_idnum": request.form.get("id_num"),
            "basic_metabolic_panel": request.form.get("bmp"),
            "brain_nautriuretic_peptide": request.form.get("bnp"),
            "complete_blood_count": request.form.get("cbc"),
            "glycated_hemoglobin": request.form.get("gh"),
            "lipid_panel": request.form.get("lp"),
            "liver_function_test": request.form.get("lft"),
            "tyroid_function_test": request.form.get("tft"),
            "created_by": session["user"]
        }
        mongo.db.medtest.insert_one( task)
        flash("Test Sucessfully Submited")
        return redirect(url_for("test"))

    categories = mongo.db.medtest.find().sort("name", 1)
    role = mongo.db.users.find_one(
        {"username": session["user"]})["role"]
    return render_template("labwork.html", categories=categories, role=role)


@app.route("/procedure", methods=["GET", "POST"])
def procedure():
    if request.method == "POST":
        proc = {
            "name": request.form.get("name").lower(),
            "title":request.form.get("title").lower(),
            "procedure_date": request.form.get("due_date").lower(),
            "pat_name":request.form.get("pat_name").lower(),
            "pat_idnum": request.form.get("id_num").lower(),
            "procedure_name": request.form.get("procedure_name").lower(),
            "created_by": session["user"]
        }
        mongo.db.procedures.insert_one( proc)
        flash("Procedure Sucessfully Submited")
        return redirect(url_for("procedure"))

    categories = mongo.db.procedures.find().sort("name", 1)
    role = mongo.db.users.find_one(
        {"username": session["user"]})["role"]

    return render_template("procedure.html", categories=categories, role=role)    


@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    role = mongo.db.users.find_one(
        {"username": session["user"]})["role"]
    return render_template("tasks.html", tasks=tasks, role=role)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #check if existing username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "name": request.form.get("name").lower(),
            "email": request.form.get("email").lower(),
            "bdate": request.form.get("bdate").lower(),
            "id_num": request.form.get("id_num").lower(),
            "role": request.form.get("role").lower(),
            "address": request.form.get("address").lower(),
            "town": request.form.get("town").lower(),
            "city": request.form .get("city").lower()

        }
        mongo.db.users.insert_one(register)

        #put the new user into 'session' cookie
        session["user"]= request.form.get("username").lower()
        flash("Registration Succesfull")
        return redirect(url_for('profile', username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            #ensure hased password matches user input
            if check_password_hash(
                existing_user["password"],request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                #invalid user name
                flash("Incorrect Username and/or Password")
                return redirect(url_for('login'))
        else:
            #username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for('login'))
    return render_template("login.html")
        



@app.route("/profile/<username>", methods=["GET","POST"])
def profile(username):
    # grab the session user's username from db
    existing_user = mongo.db.users.find_one(
        {"username": session["user"]})
    
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    role = mongo.db.users.find_one(
        {"username": session["user"]})["role"]

    if existing_user:
        return render_template("profile.html", username = username, role = role)
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/add_task",  methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        task = {
            "category_name": request.form.get("category_name").lower(),
            "task_name": request.form.get("task_name").lower(),
            "task_description": request.form.get("task_description").lower(),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date").lower(),
            "dr_name": request.form.get("dr_name").lower(),
            "pat_name": request.form.get("pat_name").lower(),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one( task)
        flash("Task Sucessfully Added")
        return redirect(url_for("get_tasks"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    role = mongo.db.users.find_one(
        {"username": session["user"]})["role"]
    return render_template("add_task.html", categories=categories, role=role)


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.get("category_name").lower(),
            "task_name": request.form.get("task_name").lower(),
            "task_description": request.form.get("task_description").lower(),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date").lower(),
            "created_by": session["user"]
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)},submit)
        flash("Task Sucessfully Updated")
        

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)

    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    role = mongo.db.users.find_one(
        {"username": session["user"]})["role"]
    return render_template("categories.html", categories=categories, role = role)

@app.route("/add_category", methods=["GET","POST"])
def add_category():
    if request.method == "POST":
        category = {
           "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
       
        return redirect(url_for('get_categories'))
    role = mongo.db.users.find_one(
        {"username": session["user"]})["role"]
    return render_template("add_category.html", role=role)


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit ={
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Update ")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
           port=int(os.environ.get("PORT")),
           debug=True)