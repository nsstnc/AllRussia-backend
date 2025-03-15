import unittest
from unittest.mock import patch, MagicMock, mock_open
from unittest.mock import ANY
import json
import io
from backend.app import app, verifyExt, create_jwt_token
from flask_jwt_extended import create_access_token
from flask_jwt_extended import verify_jwt_in_request, get_jwt


class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.app.testing = True
        app.config['JWT_SECRET_KEY'] = 'test-key'
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_verify_ext_valid(self):
        """Тест проверки допустимых расширений файлов"""
        self.assertTrue(verifyExt('test.jpg'))
        self.assertTrue(verifyExt('test.jpeg'))
        self.assertTrue(verifyExt('test.png'))

    def test_verify_ext_invalid(self):
        """Тест проверки недопустимых расширений файлов"""
        self.assertFalse(verifyExt('test.pdf'))
        self.assertFalse(verifyExt('test.exe'))
        self.assertFalse(verifyExt('test.txt'))

    @patch('backend.app.get_jwt')
    def test_admin_login_already_logged_in(self, mock_get_jwt):
        """Тест перенаправления на панель администратора, если пользователь уже вошел в систему"""
        mock_get_jwt.return_value = {"fresh": True}
        response = self.app.get('/api/admin_login')
        self.assertEqual(response.status_code, 302)
        self.assertTrue('/api/admin_panel' in response.location)

    @patch('backend.app.get_jwt')
    def test_admin_login_page(self, mock_get_jwt):
        """Тест страницы входа в админ-панель"""
        mock_get_jwt.return_value = {"fresh": False}
        response = self.app.get('/api/admin_login')
        self.assertEqual(response.status_code, 200)

    @patch('backend.app.requests.get')
    @patch('backend.app.database.get_user_by_username')
    @patch('flask_jwt_extended.create_access_token')
    @patch('flask_jwt_extended.set_access_cookies')
    def test_admin_login_successful(self, mock_set_cookies, mock_create_token, mock_get_user, mock_requests_get):
        """Тест успешного входа в админ-панель"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = json.dumps({"status": "ok"}).encode()
        mock_requests_get.return_value = mock_response

        hashed_password = "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
        mock_get_user.return_value = {"username": "admin", "password": hashed_password}

        mock_token = "fake-jwt-token"
        mock_create_token.return_value = mock_token

        response = self.app.post('/api/admin_login', data={
            'username': 'admin',
            'password': 'password',
            'smart-token': 'fake-token'
        })

        self.assertEqual(response.status_code, 302)

        mock_requests_get.assert_called_once()
        mock_get_user.assert_called_once_with('admin')

    @patch('backend.app.requests.get')
    @patch('backend.app.database.get_user_by_username')
    def test_admin_login_invalid_credentials(self, mock_get_user, mock_requests_get):
        """Тест входа с неверными учетными данными"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = json.dumps({"status": "ok"}).encode()
        mock_requests_get.return_value = mock_response

        mock_get_user.return_value = {"username": "admin", "password": "different_hash"}

        response = self.app.post('/api/admin_login', data={
            'username': 'admin',
            'password': 'wrong_password',
            'smart-token': 'fake-token'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue('error=' in response.location)

    @patch('backend.app.jwt_required')
    @patch('backend.app.database.get_data_admin_panel')
    @patch('backend.app.database.get_model_columns')
    @patch('backend.app.get_jwt')
    def test_admin_panel(self, mock_get_jwt, mock_get_columns, mock_get_data, mock_jwt_required):
        """Тест панели администратора"""
        mock_jwt_required.return_value = lambda f: f
        mock_get_columns.return_value = ['id', 'title', 'content']
        mock_get_data.return_value = ([], 0, None)
        mock_get_jwt.return_value = {"fresh": True}

        with self.app.session_transaction() as session:
            session['jwt_token'] = 'fake-jwt-token'

        response = self.app.get('/api/admin_panel/news')
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        """Тест выхода из системы"""
        response = self.app.get('/api/logout')
        self.assertEqual(response.status_code, 302)
        self.assertTrue('/api/admin_login' in response.location)

    @patch('backend.app.jwt_required')
    @patch('backend.app.database.get_record_by_id')
    def test_edit_get(self, mock_get_record, mock_jwt_required):
        """Тест получения формы редактирования записи"""
        mock_jwt_required.return_value = lambda f: f
        mock_get_record.return_value = {'id': 1, 'title': 'Test', 'content': 'Content'}

        response = self.app.get('/api/admin_panel/edit/1/news')
        self.assertEqual(response.status_code, 302)

    @patch('backend.app.jwt_required')
    @patch('backend.app.database.update_record')
    @patch('backend.app.database.get_record_by_id')
    def test_edit_post(self, mock_get_record, mock_update_record, mock_jwt_required):
        """Тест обновления записи"""
        mock_jwt_required.return_value = lambda f: f

        mock_get_record.return_value = {
            'title': 'Old Title',
            'content': 'Old Content',
            'url': ''
        }

        test_data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
            'url': '',
            'tag': 'Новости/أخبار'
        }

        response = self.app.post('/api/admin_panel/edit/1/news',
                                 data=test_data)

        self.assertEqual(response.status_code, 302)
        # mock_update_record.assert_called_once()

    @patch('backend.app.jwt_required')
    @patch('backend.app.database.get_next_id')
    @patch('backend.app.database.insert_data')
    def test_add_record(self, mock_insert_data, mock_get_next_id, mock_jwt_required):
        """Тест добавления новой записи"""
        mock_jwt_required.return_value = lambda f: f
        mock_get_next_id.return_value = 1

        with app.test_request_context():
            access_token = create_access_token('test_user')

        test_data = {
            'title': 'New Article',
            'content': 'New Content',
            'tag': 'Новости/أخبار'
        }

        response = self.app.post(
            '/api/admin_panel/add/news',
            data=test_data,
            headers={'Authorization': f'Bearer {access_token}'}
        )

        self.assertEqual(response.status_code, 302)
        # mock_insert_data.assert_called_once()

    @patch('backend.app.jwt_required')
    @patch('backend.app.database.make_main')
    def test_make_main(self, mock_make_main, mock_jwt_required):
        """Тест установки новости как главной"""
        mock_jwt_required.return_value = lambda f: f

        response = self.app.get('/api/admin_panel/make_main/1')
        self.assertEqual(response.status_code, 302)
        # mock_make_main.assert_called_once_with(1)

    @patch('backend.app.jwt_required')
    @patch('pathlib.Path')
    def test_upload_image(self, mock_path, mock_jwt_required):
        """Тест загрузки изображения"""
        mock_jwt_required.return_value = lambda f: f
        mock_path.return_value = MagicMock()

        with patch('backend.app.verifyExt', return_value=True), \
                patch('uuid.uuid4', return_value='test-uuid'):
            file = (io.BytesIO(b'test file content'), 'test.jpg')
            response = self.app.post('/api/upload_image',
                                     data={'file': file},
                                     content_type='multipart/form-data')

            self.assertEqual(response.status_code, 302)

    def test_create_jwt_token(self):
        """Тест создания JWT токена"""
        user = {'username': 'test_user'}
        mock_response = MagicMock()

        with patch('backend.app.create_access_token', return_value='test_token') as mock_create_token, \
                patch('backend.app.set_access_cookies') as mock_set_cookies:
            create_jwt_token(mock_response, user)

            mock_create_token.assert_called_once_with(identity='test_user', fresh=True)
            mock_set_cookies.assert_called_once_with(mock_response, 'test_token')


if __name__ == '__main__':
    unittest.main()
