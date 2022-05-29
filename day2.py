import os
import json
import re
import copy
import uuid
import datetime

filename = 'my_database.txt'
current_login_user = {}


def load_database():
    try:
        with open(os.path.join(filename), 'r+') as f:
            d = f.read()
            return json.loads(d)
    except:
        return {}


def update_database(data):
    with open(os.path.join(filename), 'w') as f:
        json.dump(data, f, indent=4)


def show_menu():
    project_menu = input("""\n 
    1) press 1 to add project
    2) press 2 to view all projects
    3) press 3 to edit project
    4) press 4 to delete project by id
    5) press 5 to search for project by date
    """).lower()
    if project_menu not in "12345":
        print("\n Error: You must select one of 1,2,3,4,5  !!\n")
        show_menu()
    elif project_menu == "1":
        add_project()
    elif project_menu == "2":
        view_all_projects()
    elif project_menu == "3":
        edit_project()
    elif project_menu == "4":
        delete_project()
    elif project_menu == "5":
        search_project_by_date()

    show_menu()


def add_project(project_id=None):
    title = input("Title: ").lower()
    details = input("Details: ").lower()
    total = input("Total Traget: ").lower()
    start_date = input("start date: ").lower()
    end_date = input("end date: ").lower()
    if validate_project_date_format(start_date, end_date):
        start_date = str(datetime.datetime.strptime(start_date, '%Y-%m-%d'))
        end_date = str(datetime.datetime.strptime(end_date, '%Y-%m-%d'))
        add_edit_project_to_current_user(project_id, title, details, total, start_date, end_date)


def add_edit_project_to_current_user(project_id, title, details, total, start_date, end_date):
    global current_login_user
    project_obj = dict(title=title, details=details, total=total, start_date=start_date, end_date=end_date)
    if not project_id:
        # add new project
        project_obj['id'] = str(uuid.uuid1().int)
        current_login_user["projects"].append(project_obj)
    else:
        # update project by project_id
        for i in range(0, len(current_login_user["projects"])):
            if current_login_user["projects"][i]['id'] == project_id:
                project_obj['id'] = project_id
                current_login_user["projects"][i] = project_obj
                break

    update_after_any_modificatin()


def update_after_any_modificatin():
    global current_login_user
    data = load_database()
    data[current_login_user['email']] = current_login_user
    update_database(data)
    show_menu()


def validate_project_date_format(start_date, end_date):
    if not validate_date_formate(start_date) or not validate_date_formate(end_date):
        print("\n Please enter a valid date formate  !!\n")
        add_project()
    else:
        return True


def print_poroject(project):
    print(f""" 
        ID: {project['id']} 
            Title: {project['title']}
            Details: {project['details']}
            Total: {project['total']}
            Start Date: {project['start_date']}
            End Date: {project['end_date']}
        
    """)


def view_all_projects():
    data = load_database()
    if data:
        for user_obj in data.values():
            for project in user_obj["projects"]:
                print_poroject(project)
    else:
        print(" \n  no project found !!! \n ")


def edit_project():
    project_id = input("Id: ").lower()
    is_owner = False
    for project in current_login_user['projects']:
        if project_id == project['id']:
            add_project(project_id)
            is_owner = True
            break
    if not is_owner:
        print("\n You are not the owner of this project  !!\n")
        edit_project()


def delete_project():
    global current_login_user
    exist_data = False
    project_id = input("Enter project id: ").lower()
    for i in range(0, len(current_login_user['projects'])):
        if int(project_id) == current_login_user['projects'][i]['id']:
            print(f"\n Project with id {project_id} is deleted successfully  !!\n")
            exist_data = True
            current_login_user['projects'].pop(i)
            update_after_any_modificatin()
            break

    if not exist_data:
        print("\n You are not the owner of this project  !!\n")


def validate_date_formate(valid_date):
    if not re.match('^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$', valid_date):
        print("\n Please enter a valid date formate  !!\n")
        return False
    else:
        return True


def search_project_by_date():
    start_end_date = input("Enter project start/end date to search: ").lower()
    if not validate_date_formate(start_end_date):
        search_project_by_date()
    else:
        get_project_by_date(start_end_date)


def get_project_by_date(start_end_date):
    global current_login_user
    for project in current_login_user['projects']:
        start_end_date = datetime.datetime.strptime(start_end_date, '%Y-%m-%d')
        start_date = datetime.datetime.strptime(project['start_date'], '%Y-%m-%d %H:%M:%S')
        end_date = datetime.datetime.strptime(project['end_date'], '%Y-%m-%d %H:%M:%S')
        if start_end_date >= start_date and start_end_date <= end_date:
            print_poroject(project)


def login_menu():
    menu_choice = input("""
    a) press a to login
    b) press b to sing up
    """).lower()
    if menu_choice not in "ab":
        print("\n Error: You must select `a` or `b`  !!\n")
        login_menu()

    if menu_choice == "a":
        login_user()

    if menu_choice == "b":
        add_user()


def add_user():
    first_name = input("First Name: ").lower()
    last_name = input("Last Name: ").lower()
    email = input("Email: ").lower()
    user_password = input("Password: ").lower()
    user_confirm_passord = input("Confirm Passowrd: ").lower()
    mobile = input("Mobile Number: ").lower()
    validate_user_obj(first_name, last_name, email, user_password, user_confirm_passord, mobile)


def check_unique_email(email):
    if email in load_database():
        print("\n Error: This email is already exist  !!\n")
        add_user()


def check_matched_passwrord(user_password, user_confirm_passord):
    if user_password != user_confirm_passord:
        print("\n Error: your password and confirmed password are not matched  !!\n")
        add_user()


def check_egypt_mobile_number(mobile):
    if not re.match('^(\+201|01|00201)[0-2,5]{1}[0-9]{8}$', mobile):
        print(""" Error: Moible number must be correct Egypt number \n 
        ex: (+2 | 002)(010 | 011 | 012 | 015) xxxxxxxx \n
        """)
        add_user()


def validate_user_obj(first_name, last_name, email, user_password, user_confirm_passord, mobile):
    global current_login_user
    check_unique_email(email)
    check_matched_passwrord(user_password, user_confirm_passord)
    check_egypt_mobile_number(mobile)
    # add user to data
    data = load_database()
    current_login_user = copy.deepcopy(dict(first_name=first_name, last_name=last_name, email=email,
                                            user_password=user_password, mobile=mobile, projects=[]))
    # update database
    update_after_any_modificatin()
    # show menu


def login_user():
    email = input("Email: ").lower()
    user_password = input("Password: ").lower()
    check_email_password(email, user_password)


def check_email_password(email, user_password):
    global current_login_user
    data = load_database()
    if email in data:
        if data[email]["user_password"] != user_password:
            print("\n Error: Email or password is not correct !!\n")
            login_user()
        else:
            print("\n You are successfully login !!\n")
            current_login_user = copy.copy(data[email])
            show_menu()
    else:
        print("\n Error: Email is not exist, please sing up first: choose (b) !!\n")
        login_menu()


def process_login_value(val):
    val = val.lower
    if val in "ab":
        if val == "b":
            add_user()
        if val == "a":
            login_user()
    else:
        print("\n Error Choice: you must select `a` or `b` !!\n")
        login_menu()


def main():
    print("\n    Crowd-Funding console app   ")
    login_menu()


if __name__ == "__main__":
    main()
