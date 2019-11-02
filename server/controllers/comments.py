from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from server import api
from server.models import Comments


class CommentsAll(Resource):
    def get(self):
        return {'comments': list(map(lambda x: x.get_self_representation(), Comments.get_all()))}, 200

    def post(self):
        data = get_parser_data(check=True)
        new_comment = Comments(
            commentators_name=data['commentators_name'],
            value=data['value'],
            rate=data['rate']
        )
        new_comment.save_to_db()
        return {
            'message': 'Comment was successfully created',
            'comment': new_comment.get_self_representation(),
        }, 201


class Comment(Resource):
    def get(self, id):

        comment = Comments.get_by_id(id)
        if not comment:
            return {'message': f'Comment with id {id} does not exist'}, 400

        return {'comment': comment.get_self_representation()}, 200

    @jwt_required
    def put(self, id):
        data = get_parser_data(check=False)
        comment = Comments.get_by_id(id)
        if not comment:
            return {'message': f'Comment with id {id} does not exist'}, 400

        for key, value in data.items():
            if not value:
                continue
            if key == 'is_checked':
                value = True if value in ('true', 'True', 1) else False
            comment.update(key, value)

        return {
                   'message': 'Comment was successfully updated',
                   'comment': comment.get_self_representation()
        }, 200

    @jwt_required
    def delete(self, id):
        comment = Comments.get_by_id(id)
        if not comment:
            return {'message': f'Comment with id {id} does not exist'}, 400

        comment.delete_from_db()
        return {}, 202


def get_parser_data(check=False):
    parser = reqparse.RequestParser()
    parser.add_argument('commentators_name', required=check)
    parser.add_argument('value', help='This field cannot be blank', required=check)
    parser.add_argument('rate', type=int, help='This field cannot be blank and should be integer', required=check)
    parser.add_argument('is_checked', required=False)
    return parser.parse_args()


api.add_resource(CommentsAll, '/api/comments', methods=['GET', 'POST'])
api.add_resource(Comment, '/api/comments/<id>', methods=['GET', 'PUT', 'DELETE'])
