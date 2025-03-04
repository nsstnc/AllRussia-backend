import unittest
import json
from unittest.mock import patch, MagicMock
from flask import Flask
from get_data import get_data_app

class TestGetDataRoutes(unittest.TestCase):
    def setUp(self):
        self.flask_app = Flask(__name__)
        self.flask_app.register_blueprint(get_data_app)
        self.app = self.flask_app.test_client()
        self.app.testing = True
        
    def test_data_news_sorted_by_date(self):
        with patch('get_data.database') as mock_db:
            mock_data = [
                {"id": 1, "title": "Test News 1", "date": "2025-03-04"},
                {"id": 2, "title": "Test News 2", "date": "2025-03-03"}
            ]
            mock_db.get_news.return_value = mock_data
            
            response = self.app.get('/data_all_news')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), mock_data)
            mock_db.get_news.assert_called_with(sort_by_date_descending=True)

    def test_data_news_politics(self):
        with patch('get_data.database') as mock_db:
            mock_data = [
                {"id": 1, "title": "Politics News", "tag": "Политика"}
            ]
            mock_db.get_news.return_value = mock_data
            
            response = self.app.get('/data_news_politics')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), mock_data)
            mock_db.get_news.assert_called_with(tag='Политика', sort_by_date_descending=True)

    def test_main_page(self):
        with patch('get_data.database') as mock_db:
            mock_main_article = [{"id": 1, "title": "Main Article"}]
            mock_news = [{"id": 2, "title": "News Article"}]
            mock_similar = [{"id": 3, "title": "Similar Article"}]

            mock_db.get_main_article.return_value = mock_main_article
            mock_db.get_news.return_value = mock_news
            mock_db.get_news_by_id.return_value = mock_similar

            with patch('get_data.get_nearest_neighbours') as mock_neighbours:
                mock_neighbours.return_value = [2, 3, 4]

                response = self.app.get('/data_main_page')

                self.assertEqual(response.status_code, 200)
                data = json.loads(response.data)
                
                expected_keys = [
                    'main_article', 'same_as_main', 'last_news',
                    'politics', 'economics', 'science_education',
                    'culture_history', 'sport', 'tourism',
                    'partners', 'projects'
                ]
                for key in expected_keys:
                    self.assertIn(key, data)

                self.assertEqual(data['main_article'], mock_main_article)
                self.assertEqual(data['same_as_main'], mock_similar)
                
                mock_db.get_main_article.assert_called_once()
                mock_neighbours.assert_called_once_with(
                    main_article_id=mock_main_article[0]['id'],
                    count_neighbours=6
                )

    def test_get_partners(self):
        with patch('get_data.database') as mock_db:
            mock_data = [{"id": 1, "name": "Test Partner"}]
            mock_db.get_partners.return_value = mock_data
            
            response = self.app.get('/get_partners')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), mock_data)

    def test_get_contacts(self):
        with patch('get_data.database') as mock_db:
            mock_data = {"phone": "123456", "email": "test@test.com"}
            mock_db.get_contacts_info.return_value = mock_data
            
            response = self.app.get('/get_contacts')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), mock_data)

if __name__ == '__main__':
    unittest.main()