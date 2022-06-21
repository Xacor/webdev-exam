from flask import flash
from models import Image
import hashlib
from werkzeug.utils import secure_filename
import uuid
from app import db, app
import os
from sqlalchemy.exc import SQLAlchemyError


class ImageSaver():
    def __init__(self, file):
        self.file = file

    def save(self, book_id):
        self.img = self.__find_by_md5_hash()
        if self.img is not None:
            return self.img
        
        file_name = secure_filename(self.file.filename)
        self.img = Image(id=str(uuid.uuid4()), 
                        file_name=file_name, 
                        mime_type=self.file.mimetype, 
                        md5_hash=self.md5_hash,
                        book_id=book_id)
        print('brfore try')
        try:
            print(self.img)
            db.session.add(self.img)
            db.session.commit()
            print('after commit')
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Не удалось сохранить изображение!\n{e}', category='danger')
            return None

        self.file.save(os.path.join(app.config['UPLOAD_FOLDER'], self.img.storage_filename))
        return self.img


    def __find_by_md5_hash(self):
        self.md5_hash = hashlib.md5(self.file.read()).hexdigest()
        self.file.seek(0)
        return Image.query.filter(Image.md5_hash == self.md5_hash).first()