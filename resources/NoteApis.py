from flask import request, jsonify,session
from sqlalchemy.exc import SQLAlchemyError
from database import app, db
from models.NoteModel import Note
from resources.UserLoginapi import login_required








@app.route('/CreateNote', methods=['POST'])
@login_required
"""
This function takes note title , category , description as input and put the all these details in database in order to create a new Note.


"""

def create():
    try:
        note_title = request.json['note_title']
        category = request.json['category']
        desc = request.json['description']
        U_id=session['user_id']
        new_Note = Note(name, category, desc,U_id)
        db.session.add(new_Note)
        db.session.commit()
        db.session.close()

        resp = jsonify({"Action": 'Note Added Successfully'})
        resp.status_code = 201
        return resp

    except SQLAlchemyError as e:
        resp = jsonify({"error": 'Oooouch!There is a problem'})
        resp.status_code = 500
        return resp




@app.route('/UpdateNote/<int:note1_id>', methods=['PATCH'])

"""
This function takes Id as input to update the note details include category description and note_title.



"""
def update(note1_id):
    try:
        note_title = request.json['note_title']
        category = request.json['category']
        desc = request.json['description']
        new_Note = Note(name, category, desc)
        Note12 = db.session.query(Note).filter(Note.id == note1_id).one()
        new_Note.update_Note(Note12)
        db.session.commit()
        db.session.close()
        resp = jsonify({"Action": 'Note Updated Successfully'})
        resp.status_code = 200
        return resp

    except SQLAlchemyError:
        resp = jsonify({"error": 'Oouch ! There is a problem ?'})
        resp.status_code = 500
        return resp
# ye wali api item delete krne k liye

@app.route('/items/<int:note1_id>', methods=['DELETE'])
"""
This functions takes the id delete the required item 

"""

def delete_item(note1_id):
    try:
        result = db.session.query(Note).filter(Note.id == note1_id).delete()
        db.session.commit()
        db.session.close()
        if result:
            resp = jsonify({"Action": 'Item Deleted Successfully {}'.format(note1_id)})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action": 'Item Not Found with id {}'.format(note1_id)})
            resp.status_code = 400
            return resp
    except SQLAlchemyError as e:
        resp = jsonify({"error": 'something went wrong'})
        resp.status_code = 500
        return resp