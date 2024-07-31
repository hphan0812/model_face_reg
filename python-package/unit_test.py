import unittest
import json
import os
from face_db import read_face_db, get_face_by_name, add_face

class TestFaceDB(unittest.TestCase):

    def setUp(self):
        # Thiết lập dữ liệu kiểm thử
        self.test_db_path = 'test_face_db.json'
        self.test_data = [
            {"name": "Alice", "age": 25, "image_path": "images/alice.jpg"},
            {"name": "Bob", "age": 30, "image_path": "images/bob.jpg"}
        ]
        with open(self.test_db_path, 'w') as f:
            json.dump(self.test_data, f)

    def tearDown(self):
        # Xóa file kiểm thử sau khi kiểm thử xong
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)

    def test_read_face_db(self):
        # Kiểm thử hàm read_face_db
        face_data = read_face_db(self.test_db_path)
        self.assertEqual(face_data, self.test_data)

    def test_get_face_by_name(self):
        # Kiểm thử hàm get_face_by_name
        face_data = read_face_db(self.test_db_path)
        alice = get_face_by_name("Alice")
        self.assertEqual(alice, self.test_data[0])

        bob = get_face_by_name("Bob")
        self.assertEqual(bob, self.test_data[1])

        non_existent = get_face_by_name("Charlie")
        self.assertIsNone(non_existent)

    def test_add_face(self):
        # Kiểm thử hàm add_face
        new_face = {"name": "Charlie", "age": 35, "image_path": "images/charlie.jpg"}
        add_face(new_face)

        face_data = read_face_db(self.test_db_path)
        self.assertIn(new_face, face_data)

if __name__ == '__main__':
    unittest.main()
