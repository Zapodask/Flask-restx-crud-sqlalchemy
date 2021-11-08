from flask_restx import Namespace, Resource, fields
from flask import request
from db import db

from models import Books

books = Namespace('books/', description='Books')

BookModel = books.model('Book', {
    'id': fields.Integer(readonly=True),
    'title': fields.String(required=True),
    'author': fields.String(required=True)
})

@books.route('/')
class Index(Resource):
    @books.doc('List_books')
    @books.marshal_list_with(BookModel)
    def get(self):
        response = Books.query.all()
        books = [res.to_json() for res in response]

        return books

    @books.doc('Register_book')
    @books.expect(BookModel)
    def post(self):
        req = request.get_json()

        book = Books(title=req['title'], author=req['author'])
        
        db.session.add(book)
        db.session.commit()

        return 'Book registered', 200


@books.route('/<int:id>')
@books.param('id', 'Book identifier')
@books.response(404, 'Book not found')
class Id(Resource):
    @books.doc('show_book')
    @books.marshal_with(BookModel)
    def get(self, id):
        response = Books.query.filter_by(id=id).first()
        book = response.to_json()

        return book


    @books.doc('update_book')
    @books.marshal_with(BookModel)
    def put(self, id):
        req = request.get_json()
        book = Books.query.filter_by(id=id).first()
        
        if 'title' in req:
            book.title = req['title']
        if 'author' in req:
            book.author = req['author']
        
        db.session.add(book)
        db.session.commit()

        return book


    @books.doc('delete_book')
    def delete(self, id):
        book = Books.query.filter_by(id=id).first()

        db.session.delete(book)
        db.session.commit()

        return 'Book deleted', 200
